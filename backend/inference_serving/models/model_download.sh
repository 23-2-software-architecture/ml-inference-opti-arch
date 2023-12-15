#!/bin/bash
sudo apt install unzip -y
# MobilenetV1 Download
curl -O https://edge-inference.s3.us-west-2.amazonaws.com/CNN/model/mobilenet_v1/mobilenet_v1.zip
unzip -q mobilenet_v1.zip && rm mobilenet_v1.zip

# YOLOV5 Download
curl -O https://edge-inference.s3.us-west-2.amazonaws.com/CNN/model/yolo_v5/yolo_v5.zip
unzip -q yolo_v5.zip && rm yolo_v5.zip
mv yolov5/yolov5s_saved_model yolo_v5
rm -rf yolov5

# BERT Download
curl -O https://edge-inference.s3.us-west-2.amazonaws.com/NLP/bert_imdb.zip
unzip -q bert_imdb.zip && rm bert_imdb.zip