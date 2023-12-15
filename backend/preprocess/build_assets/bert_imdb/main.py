import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from fastapi import FastAPI, Query
from typing import Optional
import json
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

app = FastAPI()

@app.get('/')
async def preprocess_get():
    return "Welcome to preprocess module"

@app.post('/')
async def preprocess(text: str = Query(None)):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])
    input_ids = tokenizer.texts_to_sequences([text])
    input_ids = pad_sequences(input_ids, maxlen=500, padding='post', truncating='post')
    input_masks = [[1] * len(input_ids[0])]
    segment_ids = [[0] * len(input_ids[0])]
    return json.dumps({"inputs": {"input_ids": input_ids, "input_masks": input_masks, "segment_ids": segment_ids}})