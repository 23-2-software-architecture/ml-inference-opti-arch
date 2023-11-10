import numpy as np
from fastapi import FastAPI, UploadFile, File
from typing import Optional
from PIL import Image
import json

app = FastAPI()

@app.get('/preprocess')
async def preprocess_get():
    return "Welcome to preprocess module"

@app.post('/preprocess')
async def pre_process(file: Optional[UploadFile] = File(None)):
    image_file = await file.read()
    img = Image.open(image_file)
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = img_array.astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return json.dumps({"inputs": {"input_1": img_array.tolist()}})