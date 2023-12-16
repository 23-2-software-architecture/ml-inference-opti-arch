#!/bin/bash
# Create a cluster in AWS with a High Availability control plane. This cluster
# has also been configured for private networking in a kops-managed VPC.
# The bastion flag is set to create an entrypoint for admins to SSH.
export KOPS_STATE_STORE="s3://mhsong-kops-state"
export CONTROL_PLANE_SIZE="t3.medium"
export NODE_SIZE="t3.large"
export ZONES="ap-northeast-2a,ap-northeast-2c"
kops create cluster mhsongcluster.mhsong.cc \
--node-count 3 \
--zones $ZONES \
--node-size $NODE_SIZE \
--control-plane-size $CONTROL_PLANE_SIZE \
--control-plane-zones $ZONES \
--networking calico \
--topology private \
--yes
kops validate cluster --wait 10m

nic_version="v1.7.0"
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-$nic_version/deploy/static/provider/aws/deploy.yaml