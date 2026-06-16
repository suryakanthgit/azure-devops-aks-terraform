#!/bin/bash

echo "Starting deployment..."

# Variables
RESOURCE_GROUP="surya-devops-rg"
ACR_NAME="suryadevopsacr"
AKS_CLUSTER="surya-aks-cluster"
IMAGE_NAME="health-dashboard"

# Login to ACR
echo "Logging into ACR..."
az acr login --name $ACR_NAME

# Build and push Docker image
echo "Building Docker image..."
docker build -t $ACR_NAME.azurecr.io/$IMAGE_NAME:latest ./app

echo "Pushing Docker image..."
docker push $ACR_NAME.azurecr.io/$IMAGE_NAME:latest

# Get AKS credentials
echo "Getting AKS credentials..."
az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER

# Deploy to AKS
echo "Deploying to AKS..."
kubectl apply -f kubernetes/deployment.yaml

echo "Deployment complete!"

# Check status
kubectl get pods
kubectl get services