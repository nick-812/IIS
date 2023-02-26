import numpy as np


from fastapi import FastAPI
import uvicorn

from pickle import load as ld

from pydantic import BaseModel
from typing import List


import sys
print(sys.path)


app = FastAPI()


class Item(BaseModel):
    name: float

class ItemList(BaseModel):
    features: List[float]


class podatki(BaseModel):
    pm25: float
    o3: float
    benzen: float
    co: float
    no2: float
    so2: float
    mesto: str



@app.on_event("startup")
def load():
    global reg 
    #reg = ld(open('/home/runner/work/IIS/IIS/models/model.pkl','rb'))     
    reg = ld(open('../models/model.pkl','rb'))          




@app.post('/air/predict') 
async def predict(
    vhod:podatki
):
    
    vnos = np.zeros([27], dtype=float)

    vnos[0] = vhod.pm25
    vnos[1] = vhod.o3
    vnos[2] = vhod.benzen
    vnos[3] = vhod.co
    vnos[4] = vhod.no2
    vnos[5] = vhod.so2

    if(vhod.mesto == "CE Ljubljanska"):
        vnos[6] = 1
    elif(vhod.mesto == "CE bolnica"):
        vnos[7] = 1
    elif(vhod.mesto == "Hrastnik"):
        vnos[8] = 1
    elif(vhod.mesto == "Iskrba"):
        vnos[9] = 1
    elif(vhod.mesto == "Koper"):
        vnos[10] = 1
    elif(vhod.mesto == "Kranj"):
        vnos[11] = 1
    elif(vhod.mesto == "Krvavec"):
        vnos[12] = 1
    elif(vhod.mesto == "LJ Bežigrad"):
        vnos[13] = 1
    elif(vhod.mesto == "LJ Celovška"):
        vnos[14] = 1
    elif(vhod.mesto == "LJ Vič"):
        vnos[15] = 1
    elif(vhod.mesto == "MB Titova"):
        vnos[16] = 1
    elif(vhod.mesto == "MB Vrbanski"):
        vnos[17] = 1
    elif(vhod.mesto == "MS Cankarjeva"):
        vnos[18] = 1
    elif(vhod.mesto == "MS Rakičan"):
        vnos[19] = 1
    elif(vhod.mesto == "NG Grčna"):
        vnos[20] = 1
    elif(vhod.mesto == "Novo mesto"):
        vnos[21] = 1
    elif(vhod.mesto == "Otlica"):
        vnos[22] = 1
    elif(vhod.mesto == "Ptuj"):
        vnos[23] = 1
    elif(vhod.mesto == "Rečica v I.Bistrici"):
        vnos[24] = 1
    elif(vhod.mesto == "Trbovlje"):
        vnos[25] = 1
    elif(vhod.mesto == "Zagorje"):
        vnos[26] = 1
    

    vnos = np.reshape(vnos, (1,vnos.shape[0]))

    #Predictanje vrednosti
    y_out = reg.predict(vnos)

    print(y_out)

    return {"prediction": y_out[0]}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8085)
