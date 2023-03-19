import json
import pandas as pd
import numpy as np





weatherfile = open('data/raw/weather/neobdelani.json')
podatki = json.load(weatherfile)

df = pd.DataFrame.from_records(podatki['data'])

df['snow'] = pd.to_numeric(df['snow'], errors='coerce')
df['wpgt'] = pd.to_numeric(df['wpgt'], errors='coerce')
df['tsun'] = pd.to_numeric(df['tsun'], errors='coerce')

df=df.replace(np.nan,0)

df["time"] = pd.to_datetime(df["time"])

df.to_csv('data/processed/obdelaniweather.csv')

print(df)






