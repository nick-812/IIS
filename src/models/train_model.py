import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from pickle import dump
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("data/processed/obdelani.csv", sep=",", header=0)

#locitev pm10 od ostalih pod
pm10 = df['pm10']
df = df.drop(['pm10'], axis=1)
df = df.drop(['Unnamed: 0'], axis=1)
df = df.drop(['date'], axis=1)

print(df.columns.tolist())

#priprava test in train mnozic
X_train, X_test, y_train, y_test = train_test_split(df.to_numpy(), pm10.to_numpy(), test_size=0.3, random_state=1234)

print(y_train[0])
print(X_train[0])

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
    
