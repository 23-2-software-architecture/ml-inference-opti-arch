import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from fastapi import FastAPI
app = FastAPI()
from tensorflow.keras.models import load_model
model = load_model('./mobilenet_v1')

@app.post('/')
async def predict(json_body: dict):
    input_1 = json_body['inputs']['input_1']
    nparray = np.array(input_1)
    result = model.predict(nparray)
    response = {
        'body': result.tolist(),
    }
    return response