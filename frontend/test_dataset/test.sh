#!/bin/bash
#mobilenet
curl -X POST http://swarch.mhsong.cc/predict?model_name=mobilenet_v1 \
-H "Content-Type: multipart/form-data" \
-F "file=@m.jpeg;type=image/jpeg"
#yolo
curl -X POST http://swarch.mhsong.cc/predict?model_name=yolo_v5 \
-H "Content-Type: multipart/form-data" \
-F "file=@y.jpg;type=image/jpeg"
#bert
curl -X POST http://swarch.mhsong.cc/predict?model_name=bert_imdb \
-H "Content-Type: multipart/form-data" \
-F "file=@test.txt;type=text/plain"
