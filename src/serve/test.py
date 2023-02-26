import pytest
import requests

def test1():
    testdata = {"pm25":27.0,"o3":90.0,"benzen":0.5,"co":0.2,"no2":9.0,"so2":2.557347,"mesto":"Hrastnik"}
    output = requests.post('http://localhost:8085/air/predict', json=testdata)

    print(output.text)


    assert "prediction" in output.text


