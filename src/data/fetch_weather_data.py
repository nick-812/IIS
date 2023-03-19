import requests
from datetime import date

import pytest



url = "https://meteostat.p.rapidapi.com/stations/hourly"

querystring = {"station":"14015","start":"2023-02-20","end":str(date.today()),"tz":"Europe/Berlin"}

headers = {
	"X-RapidAPI-Key": "8b10ab09bbmshc60e103331db811p1d4863jsna06aab62b046",
	"X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


with open('data/raw/weather/neobdelani.json', 'w') as f:
    f.write(response.text)

def test_api():
    assert "meta" in response.text

