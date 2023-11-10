### need to change import libararies
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from fastapi import FastAPI
app = FastAPI()

@app.post('/')
async def predict(json_body: dict):
    ### add code here
    with open('imagenet_labels.txt', 'r') as f:
        labels = f.read().splitlines()

    predictions = np.array(json_body['body'])
    predicted_class_index = np.argmax(predictions)

    predicted_label = labels[predicted_class_index]
    predicted_score = predictions[0][predicted_class_index]

    response = {
        'result': predicted_label
    }

    return response