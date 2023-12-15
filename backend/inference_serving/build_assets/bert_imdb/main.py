import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from fastapi import FastAPI
app = FastAPI()
from tensorflow.keras.models import load_model
model = load_model('./bert_imdb')

@app.post('/')
async def predict(json_body: dict):
    input_ids = np.array(json_body['inputs']['input_ids'])
    input_masks = np.array(json_body['inputs']['input_masks'])
    segment_ids = np.array(json_body['inputs']['segment_ids'])
    result = model.predict([input_masks,input_ids,segment_ids])
    response = {
        'body': result.tolist(),
    }
    return response