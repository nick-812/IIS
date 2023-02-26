import requests
import json
import pandas as pd

response_API = requests.get('https://arsoxmlwrapper.app.grega.xyz/api/air/archive')


with open('../data/raw/neobdelani.json', 'w') as f:
    f.write(response_API.text)


#json_object = json.loads(response_API.text)

df = pd.read_json('../data/raw/neobdelani.json')


df1 = df['json'].iloc[0]
df2 = json.loads(df1)
df3 = df2['arsopodatki']['postaja']
df1 = pd.DataFrame(df3)


prvi = True

test = json.loads(response_API.text)
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
df = df.drop(['datum_od'], axis=1)
df = df.drop(['ge_sirina'], axis=1)
df = df.drop(['sifra'], axis=1)
df = df.drop(['datum_do'], axis=1)
df = df.drop(['ge_dolzina'], axis=1)

dummies = pd.get_dummies(df['merilno_mesto'])
df = pd.concat([df, dummies], axis=1)
df = df.drop(['merilno_mesto'], axis=1)

df['pm2.5'] = pd.to_numeric(df['pm2.5'], errors='coerce')
df['o3'] = pd.to_numeric(df['o3'], errors='coerce')
df['benzen'] = pd.to_numeric(df['benzen'], errors='coerce')
df['pm10'] = pd.to_numeric(df['pm10'], errors='coerce')
df['co'] = pd.to_numeric(df['co'], errors='coerce')
df['no2'] = pd.to_numeric(df['no2'], errors='coerce')
df['so2'] = pd.to_numeric(df['so2'], errors='coerce')

df = df.fillna(df.mean())

df.to_csv('../data/processed/obdelani.csv')