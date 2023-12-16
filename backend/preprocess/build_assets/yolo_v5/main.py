import numpy as np
from fastapi import FastAPI, UploadFile, File
from typing import Optional
import cv2
import json
from io import BytesIO

app = FastAPI()

@app.get('/')
async def preprocess_get():
    return "Welcome to preprocess module"

@app.post('/')
async def preprocess(file: Optional[UploadFile] = File(None)):
    image_file = await file.read()
    img = cv2.imread(BytesIO(image_file))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (640, 640))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    return json.dumps({"inputs": {"x": img.tolist()}})