from fastapi import FastAPI, UploadFile, File, Query
from typing import Optional
import time
import requests

app = FastAPI()

CLUSTER_DOMAIN = "cluster.local"

PREPROCESS_NAMESPACE = "preprocess"
PREPROCESS_MODULE_ADDRESS = f"{PREPROCESS_NAMESPACE}.svc.{CLUSTER_DOMAIN}:8081/"

POSTPROCESS_NAMESPACE = "postprocess"
POSTPROCESS_MODULE_ADDRESS = f"{POSTPROCESS_NAMESPACE}.svc.{CLUSTER_DOMAIN}:8083/"

INFERENCE_NAMESPACE = "inference"
INFERENCE_MODULE_ADDRESS = f"{INFERENCE_NAMESPACE}.svc.{CLUSTER_DOMAIN}:8082/"


def send_to_preprocess(model_name, data):
    preprocess_start_time = time.time()
    if model_name == "mobilenet_v1":
        response = requests.post(url=f"http://{model_name.replace('_','-')}.{PREPROCESS_MODULE_ADDRESS}", files={'file': data})
    preprocess_time = time.time() - preprocess_start_time

    return response.json(), preprocess_time

def send_to_inference(model_name, data):
    headers = {"content-type": "application/json"}
    inference_start_time = time.time()
    if model_name == "mobilenet_v1":
        response = requests.post(url=f"http://{model_name.replace('_','-')}.{INFERENCE_MODULE_ADDRESS}", data=data, headers=headers)
    inference_time = time.time() - inference_start_time

    return response.json(), inference_time

def send_to_postprocess(model_name, data):
    headers = {"content-type": "application/json"}
    postprocess_start_time = time.time()
    if model_name == "mobilenet_v1":
        response = requests.post(url=f"http://{model_name.replace('_','-')}.{POSTPROCESS_MODULE_ADDRESS}", data=data, headers=headers)
    postprocess_time = time.time() - postprocess_start_time

    return response.json(), postprocess_time

@app.get('/')
async def main_page():
    return "Welcome to broker!"

@app.get('/predict')
async def predict_get():
    return "Please use POST method"

@app.post('/predict')
async def predict_post(model_name: str = Query(None), file: Optional[UploadFile] = File(None)):
    if model_name == "mobilenet_v1":
        image_file = await file.read()
        preprocess_result, preprocess_time = send_to_preprocess(model_name, image_file)
        inference_result, inference_time = send_to_inference(model_name, preprocess_result)
        postprocess_result, postprocess_time = send_to_postprocess(model_name, inference_result)
    else:
        return "Not support model"
    
    response = {
        "result": postprocess_result,
        "preprocess_time": preprocess_time,
        "inference_time": inference_time,
        "postprocess_time": postprocess_time,
        "elapsed_time": preprocess_time + inference_time + postprocess_time
    }

    return response
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)