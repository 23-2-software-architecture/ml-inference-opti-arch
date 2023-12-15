import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from fastapi import FastAPI
app = FastAPI()
from tensorflow.keras.models import load_model
model = load_model('./yolo_v5')

@app.post('/')
async def predict(json_body: dict):
    x = json_body['inputs']['x']
    nparray = np.array(x)
    result = model.predict(nparray)
    response = {
        'body': result.tolist(),
    }
    return response