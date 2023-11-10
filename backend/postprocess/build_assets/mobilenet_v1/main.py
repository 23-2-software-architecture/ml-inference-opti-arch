### need to change import libararies
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from fastapi import FastAPI
app = FastAPI()

@app.post('/')
async def predict(json_body: dict):
    with open('imagenet_labels.txt', 'r') as f:
        labels = f.read().splitlines()

    predictions = np.array(json_body['body'])
    predicted_class_index = np.argmax(predictions)

    predicted_label = labels[predicted_class_index + 1]
    predicted_probability = predictions[0][predicted_class_index]

    response = {
        'result_class': predicted_label,
        'result_probability': predicted_probability
    }

    return response