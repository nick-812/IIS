import json
import pandas as pd
import numpy as np

#json_object = json.loads(response_API.text)


df = pd.read_json('data/raw/air/neobdelani.json')


df1 = df['json'].iloc[0]
df2 = json.loads(df1)
df3 = df2['arsopodatki']['postaja']
df1 = pd.DataFrame(df3)


prvi = True

airfile = open('data/raw/air/neobdelani.json')
test = json.load(airfile)


for user in test:
    if(prvi):
        prvi=False
    else:
        df2 = json.loads(user['json'])
        df3 = df2['arsopodatki']['postaja']
        df4 = pd.DataFrame(df3)

        df1=pd.concat([df1, df4], axis=0)


df = df1

df = df.drop(['nadm_visina'], axis=1)
#df = df.drop(['datum_od'], axis=1)
df = df.drop(['ge_sirina'], axis=1)
df = df.drop(['sifra'], axis=1)
df = df.drop(['datum_do'], axis=1)
df = df.drop(['ge_dolzina'], axis=1)

df = df[df['merilno_mesto'] == "LJ Bežigrad"]
df = df.drop(['merilno_mesto'], axis=1)
df = df.drop(['benzen'], axis=1)
df = df.drop(['so2'], axis=1)
df = df.drop(['pm2.5'], axis=1)
df = df.drop(['o3'], axis=1)
df = df.drop(['co'], axis=1)
df = df.drop(['no2'], axis=1)

df['pm10'] = pd.to_numeric(df['pm10'], errors='coerce')

df["datum_od"] = pd.to_datetime(df["datum_od"])

#df = df.fillna(df.mean())


df = df.sort_values(by='datum_od')
df1 = df.drop_duplicates()

df1.to_csv('data/processed/obdelaniair.csv')

print(df1)

