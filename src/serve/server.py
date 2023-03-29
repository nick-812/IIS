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
    
    vnos = np.zeros([11], dtype=float)


    vnos[0] = vhod.temp
    vnos[1] = vhod.dwpt
    vnos[2] = vhod.rhum
    vnos[3] = vhod.prcp
    vnos[4] = vhod.snow
    vnos[5] = vhod.wdir
    vnos[6] = vhod.wspd
    vnos[7] = vhod.wpgt
    vnos[8] = vhod.pres
    vnos[9] = vhod.tsun
    vnos[10] = vhod.coco
    

    vnos = np.reshape(vnos, (1,vnos.shape[0]))

    #Predictanje vrednosti
    y_out = reg.predict(vnos)

    print(y_out)

    return {"prediction": y_out[0]}


client = TestClient(app)

def test_read_main():
    testdata = {"temp":0.4,"dwpt":-2.3,"rhum":82,"prcp":0,"snow":0,"wdir":222,"wspd":3.6,"wpgt":0,"pres":1016,"tsun":0,"coco":1}
    response = client.post('/air/predict', json=testdata)
    assert response.status_code == 200
    resp_json = json.loads(response.text)
    predikcija = int(resp_json["prediction"])
    assert predikcija > 0
    assert "prediction" in response.text



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8085)
