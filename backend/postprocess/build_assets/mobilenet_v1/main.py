### need to change import libararies
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from fastapi import FastAPI
import pickle
app = FastAPI()
with open('imagenet_labels.pkl', 'rb') as f:
    labels = pickle.load(f)

@app.post('/')
async def predict(json_body: dict):
    predictions = np.array(json_body['body'])
    predicted_class_index = np.argmax(predictions)

    predicted_label = labels[predicted_class_index + 1].split()
    predicted_label = predicted_label[-1]
    predicted_probability = predictions[0][predicted_class_index]

    response = {
        'result_class': predicted_label,
        'result_probability': predicted_probability
    }

    return response