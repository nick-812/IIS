import requests
from datetime import date

response_API = requests.get('https://arsoxmlwrapper.app.grega.xyz/api/air/archive')


with open('data/raw/air/neobdelani.json', 'w') as f:
    f.write(response_API.text)

def test_api():
    assert "LJ" in response_API.text