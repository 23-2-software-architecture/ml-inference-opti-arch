import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from fastapi import FastAPI, UploadFile, File
from typing import Optional
import json
from tensorflow.keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

app = FastAPI()

@app.get('/')
async def preprocess_get():
    return "Welcome to preprocess module"

@app.post('/')
async def preprocess(file: Optional[UploadFile] = File(None)):
    text_file = await file.read()
    text_content = text_file.decode('utf-8')
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text_content])
    input_ids = tokenizer.texts_to_sequences([text_content])
    input_ids = pad_sequences(input_ids, maxlen=500, padding='post', truncating='post')
    input_masks = [[float(i != 0) for i in seq] for seq in input_ids]
    segment_ids = [[0] * len(seq) for seq in input_ids]
    return json.dumps({"inputs": {"input_ids": input_ids.tolist(), "input_masks": input_masks, "segment_ids": segment_ids}})