import numpy as np
from fastapi import FastAPI
import pickle

app = FastAPI()

NEGATIVE = 0
POSITIVE = 1

positive_str = "이 영화 리뷰는 긍정적인 것 같습니다!"
negative_str = "이 영화 리뷰는 부정적인 것 같습니다."
neutral_str = "이 영화 리뷰는 중립적인 것 같습니다."

@app.post('/')
async def postprocess(json_body: dict):
    predictions = np.array(json_body['body'])
    predicted_class_index = np.argmax(predictions)
    probability = predictions[predicted_class_index]
    
    result_str = None
    if probability < 0.7:
        result_str = neutral_str
    elif predicted_class_index == POSITIVE:
        result_str = positive_str
    else:
        result_str = negative_str

    response = {
        "result" : result_str
    }

    return response