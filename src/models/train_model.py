import pandas as pd
import os
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from pickle import dump
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
import mlflow

def main():

    
    mlflow.set_tracking_uri("https://dagshub.com/nick-812/IIS.mlflow")

    os.environ['MLFLOW_TRACKING_USERNAME'] = 'nick-812'
    os.environ['MLFLOW_TRACKING_PASSWORD'] = 'f37e3703f5ec08bb5db0beceeeb610ef344dc6da'

    mlflow.sklearn.autolog()
    

    df = pd.read_csv("data/processed/train.csv", sep=",", header=0)

    #locitev pm10 od ostalih pod
    pm10 = df['pm10']
    df = df.drop(['pm10'], axis=1)
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.drop(['Unnamed: 0.1'], axis=1)
    df = df.drop(['date'], axis=1)

    df_test = pd.read_csv("data/processed/test.csv", sep=",", header=0)

    #locitev pm10 od ostalih pod
    pm10_test = df_test['pm10']
    df_test = df_test.drop(['pm10'], axis=1)
    df_test = df_test.drop(['Unnamed: 0'], axis=1)
    df_test = df_test.drop(['Unnamed: 0.1'], axis=1)
    df_test = df_test.drop(['date'], axis=1)

    #priprava test in train mnozic
    X_train = df.to_numpy()
    y_train = pm10.to_numpy()
    X_test = df_test.to_numpy()
    y_test = pm10_test.to_numpy()



    cevovod = Pipeline ([
        ("preprocess", SimpleImputer(missing_values=np.nan, strategy='mean')),
        ("MLPR", MLPRegressor())
    ])

    parametri = {
        "MLPR__hidden_layer_sizes": [(64),(32),(16)],
        "MLPR__learning_rate_init": [0.001, 0.01]
    }

    gsModel = GridSearchCV (cevovod, parametri, verbose=2)

    gsModel.fit(X_train, y_train)
    print (gsModel.best_params_)


    y_out = gsModel.predict(X_test)

    mae=mean_absolute_error(y_test, y_out)
    mse=mean_squared_error(y_test, y_out)
    evs=explained_variance_score(y_test, y_out)




    mlflow.sklearn.log_model(gsModel, "model")
    mlflow.log_metric("mean_absolute_error", mae)
    mlflow.log_metric("mean_squared_error", mse)
    mlflow.log_metric("explained_variance_score", evs)

    # Load the model from the artifact path
    loaded_model = mlflow.sklearn.load_model("runs:/{run_id}/model".format(run_id=mlflow.active_run().info.run_id))

    
    # Register the model explicitly
    model_uri = "runs:/{run_id}/model".format(run_id=mlflow.active_run().info.run_id)
    model_version = mlflow.register_model(model_uri, "my_model_name")
    


    model_name = "my_model_name"
    model_stage = "Production"
    model_uri=f"models:/{model_name}/{model_stage}"


    model = mlflow.pyfunc.load_model(
        model_uri=model_uri
    )

    

    y_out2 = model.predict(X_test)
    mae2 = mean_absolute_error(y_test, y_out2)

    print(mae)
    print(mae2)

    if mae<mae2:
        client = mlflow.tracking.MlflowClient()
        client.transition_model_version_stage(
            name="my_model_name",
            version=model_version.version,
            stage="Production"
        )





    '''
    dump(search, open('models/model.pkl', 'wb'))


    #Predictanje vrednosti
    y_out = search.predict(X_test)

    with open('reports/train_metrics.txt', 'w') as f:
        f.writelines(str(reg.score(X_test, y_test))+"\n")

    with open('reports/metrics.txt', 'w') as f:
        f.writelines(str(mean_absolute_error(y_test, y_out))+"\n")
        f.writelines(str(mean_squared_error(y_test, y_out))+"\n")
        f.writelines(str(explained_variance_score(y_test, y_out))+"\n")
    '''
    
if __name__ == "__main__":
    main()
