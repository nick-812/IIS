import requests
from datetime import date
import datetime
import pandas as pd
import numpy as np

import json



url = "https://meteostat.p.rapidapi.com/stations/hourly"

querystring = {"station":"14015","start":str(date.today()),"end":str(date.today() + datetime.timedelta(days=3)),"tz":"Europe/Berlin"}

headers = {
	"X-RapidAPI-Key": "8b10ab09bbmshc60e103331db811p1d4863jsna06aab62b046",
	"X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

podatki = json.loads(response.text)

df = pd.DataFrame.from_records(podatki['data'])

df['snow'] = pd.to_numeric(df['snow'], errors='coerce')
df['wpgt'] = pd.to_numeric(df['wpgt'], errors='coerce')
df['tsun'] = pd.to_numeric(df['tsun'], errors='coerce')

df=df.replace(np.nan,0)

df["date"] = pd.to_datetime(df["time"])
df = df.drop(['time'], axis=1)

df.to_csv('data/processed/futureweather.csv')

print(df)


