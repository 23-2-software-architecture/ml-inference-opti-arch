#!/bin/bash

# MobilenetV1 Download
curl -O https://edge-inference.s3.us-west-2.amazonaws.com/CNN/model/mobilenet_v1/mobilenet_v1.zip
unzip -q mobilenet_v1.zip && rm mobilenet_v1.zip