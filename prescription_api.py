import uvicorn
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

class Perscription(BaseModel):
    ligos_kodas: str
    atc_kodas: str
    dozuociu_sk: list
    recepto_galiojimas_d: list
    kompens_poz: list
    pac_savivaldybe: str
    vart_trukme_d: list
    pac_lytis: str
    pac_amziaus_gr : str

app = FastAPI()

# nurodome savo pickle'into modelio vieta kompiuteryje
with open("/Users/tautis/Downloads/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get('/')
def index():
    return {'welcome_message': ''' Welcome to Perscription Analyzer's homepage '''}

@app.get('/explain_prediction')
def index():
    return {'explain_message': 'The possible outputs for prediction are 0, meaning the perscription is unlikely to be used, and 1, meaning the perscription is likely to be used'}

@app.post('/prediction')
def get_perscription_prediction(data: Perscription):
    received = data.dict()
    received_df = pd.DataFrame(received)

    pred_name = model.predict(received_df).tolist()[0]

    return (f'Predicted value: {pred_name}')

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4000)