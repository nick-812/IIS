import numpy as np


from fastapi import FastAPI
from fastapi.testclient import TestClient
import uvicorn

import json

from pickle import load as ld

from pydantic import BaseModel
from typing import List


import sys
print(sys.path)


app = FastAPI()
#reg = ld(open('model.pkl','rb'))
reg = ld(open('models/model.pkl','rb'))

class Item(BaseModel):
    name: float

class ItemList(BaseModel):
    features: List[float]


class podatki(BaseModel):
    pm25: float
    o3: float
    co: float
    no2: float
    temp: float
    dwpt: float
    rhum: float
    prcp: float
    snow: float
    wdir: float
    wspd: float
    wpgt: float
    pres: float
    tsun: float
    coco: float



@app.on_event("startup")
def load():
    global reg   
    #reg = ld(open('model.pkl','rb'))
    reg = ld(open('models/model.pkl','rb'))




@app.post('/air/predict') 
async def predict(
    vhod:podatki
):
    
    vnos = np.zeros([15], dtype=float)


    vnos[0] = vhod.pm25
    vnos[1] = vhod.o3
    vnos[2] = vhod.co
    vnos[3] = vhod.no2
    vnos[4] = vhod.temp
    vnos[5] = vhod.dwpt
    vnos[6] = vhod.rhum
    vnos[7] = vhod.prcp
    vnos[8] = vhod.snow
    vnos[9] = vhod.wdir
    vnos[10] = vhod.wspd
    vnos[11] = vhod.wpgt
    vnos[12] = vhod.pres
    vnos[13] = vhod.tsun
    vnos[14] = vhod.coco
    

    vnos = np.reshape(vnos, (1,vnos.shape[0]))

    #Predictanje vrednosti
    y_out = reg.predict(vnos)

    print(y_out)

    return {"prediction": y_out[0]}


client = TestClient(app)

def test_read_main():
    testdata = {"pm25":38,"o3":3.0,"co":0.8,"no2":62.0,"temp":0.4,"dwpt":-2.3,"rhum":82,"prcp":0,"snow":0,"wdir":222,"wspd":3.6,"wpgt":0,"pres":1016,"tsun":0,"coco":1}
    response = client.post('/air/predict', json=testdata)
    assert response.status_code == 200
    resp_json = json.loads(response.text)
    predikcija = int(resp_json["prediction"])
    assert predikcija > 30
    assert predikcija < 50
    assert "prediction" in response.text



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8085)
