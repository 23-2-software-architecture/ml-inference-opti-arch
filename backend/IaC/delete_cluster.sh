#!/bin/bash
export KOPS_STATE_STORE="s3://mhsong-kops-state"
export CONTROL_PLANE_SIZE="t3.medium"
export NODE_SIZE="t3.medium"
export ZONES="ap-northeast-2a,ap-northeast-2c,ap-northeast-2d"

nic_version="v1.7.0"
kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-$nic_version/deploy/static/provider/aws/deploy.yaml

kops delete cluster mhsongcluster.mhsong.cc --yes