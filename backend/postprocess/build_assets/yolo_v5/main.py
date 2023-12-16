import numpy as np
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import pickle
import cv2
import io

app = FastAPI()

with open("yolo_label.pkl", "rb") as f:
    label_class = pickle.load(f)
        
def convert_coordinates(box, img_width, img_height):
    x_center, y_center, width, height = box
    x_min = x_center - (width / 2)
    y_min = y_center - (height / 2)
    x_max = x_center + (width / 2)
    y_max = y_center + (height / 2)
    
    x_min, x_max = x_min * img_width, x_max * img_width
    y_min, y_max = y_min * img_height, y_max * img_height
    return int(x_min), int(y_min), int(x_max), int(y_max)

def draw_bounding_boxes(image, boxes, class_probabilities, class_names):
    for i, box in enumerate(boxes):
        x_min, y_min, x_max, y_max = convert_coordinates(box, 640, 640)
        class_id = np.argmax(class_probabilities[i])
        class_name = class_names[class_id]
        confidence = class_probabilities[i][class_id]

        # 이미지에 사각형 그리기
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
        # 클래스 이름과 확률 표시
        label = f'{class_name}: {confidence:.2f}'
        cv2.putText(image, label, (x_min + 5, y_min + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

@app.post('/')
async def postprocess(json_body: dict):
    predictions = np.array(json_body['body'])
    img = np.array(json_body['image'])
    output_tensor = predictions[0]
    
    boxes = output_tensor[0, :, :4]
    class_probabilities = output_tensor[0, :, 4:]
    
    opencv_scores = [float(arr.numpy().max()) for arr in class_probabilities]
    opencv_boxes = []
    for box in boxes:
        x_center, y_center, width, height = box
        w = int(width * 640)
        h = int(height * 640)
        opencv_boxes.append([int(x_center * 640), int(y_center * 640), w, h])
    
    score_threshold = 0.99

    indices = cv2.dnn.NMSBoxes(opencv_boxes, opencv_scores, score_threshold=score_threshold, nms_threshold=0.4)

    selected_boxes = [boxes[0][i] for i in indices]
    selected_probabilities = [class_probabilities[0][i] for i in indices]
    
    image = (img[0] * 255).astype(np.uint8)

    draw_bounding_boxes(image, selected_boxes, selected_probabilities, label_class)
    
    _, encoded_img = cv2.imencode('.jpg', image)
    byte_stream = io.BytesIO(encoded_img.tobytes())
    
    result = {
        "result" : StreamingResponse(byte_stream, media_type="image/jpeg")
    }

    return result