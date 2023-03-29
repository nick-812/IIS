import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from pickle import dump
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
#import mlflow

#mlflow.set_tracking_uri("https://dagshub.com/nick-812/IIS.mlflow")

df = pd.read_csv("data/processed/train.csv", sep=",", header=0)

#locitev pm10 od ostalih pod
pm10 = df['pm10']
df = df.drop(['pm10'], axis=1)
df = df.drop(['Unnamed: 0'], axis=1)
df = df.drop(['date'], axis=1)

df_test = pd.read_csv("data/processed/test.csv", sep=",", header=0)

#locitev pm10 od ostalih pod
pm10_test = df_test['pm10']
df_test = df_test.drop(['pm10'], axis=1)
df_test = df_test.drop(['Unnamed: 0'], axis=1)
df_test = df_test.drop(['date'], axis=1)

print(df.columns.tolist())

#priprava test in train mnozic
X_train = df.to_numpy()
y_train = pm10.to_numpy()
X_test = df_test.to_numpy()
y_test = pm10_test.to_numpy()


#Linearna regresija nad train podatki
reg = LinearRegression().fit(X_train, y_train)

dump(reg, open('models/model.pkl', 'wb'))

#Predictanje vrednosti
y_out = reg.predict(X_test)


with open('reports/train_metrics.txt', 'w') as f:
    f.writelines(str(reg.score(X_test, y_test))+"\n")

with open('reports/metrics.txt', 'w') as f:
    f.writelines(str(mean_absolute_error(y_test, y_out))+"\n")
    f.writelines(str(mean_squared_error(y_test, y_out))+"\n")
    f.writelines(str(explained_variance_score(y_test, y_out))+"\n")
    
