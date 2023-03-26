import pandas as pd

df = pd.read_csv("data/processed/obdelaniweather.csv", sep=",", header=0)
df1 = pd.read_csv("data/processed/obdelaniair.csv", sep=",", header=0)



df = df.rename(columns={"time": "date"})
df1 = df1.rename(columns={"datum_od": "date"})

dfout = df.merge(df1, how='inner', on='date')

dfout = dfout.drop(['Unnamed: 0_x'], axis=1)
dfout = dfout.drop(['Unnamed: 0_y'], axis=1)

print(dfout)

dfout.to_csv('data/processed/obdelani.csv')
dfout.to_csv('data/processed/current_data.csv')