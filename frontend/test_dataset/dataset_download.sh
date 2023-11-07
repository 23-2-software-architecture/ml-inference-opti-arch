#!/bin/bash

#mobilenet v1 image
#image classification image dataset (tfrecord imagenet)
mkdir imagenet
curl -O https://edge-inference.s3.us-west-2.amazonaws.com/CNN/dataset/imagenet/imagenet_1000
mv imagenet_1000 ./imagenet
