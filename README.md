# Azure DevOps CI/CD Pipeline — Containerized App on AKS

## Live Demo
- App: http://20.197.104.152
- Health Check: http://20.197.104.152/health

## Tech Stack
- Python Flask, Docker, Terraform, Azure DevOps, AKS, ACR, Azure Monitor, Bash

## What This Project Does
- Provisioned Azure infrastructure (AKS, ACR) using Terraform
- Containerized Flask app with Docker and pushed to Azure Container Registry
- Built Azure DevOps CI/CD pipeline — auto deploys on every code push
- Deployed to AKS with Kubernetes liveness probes for auto-restart
- Python health monitoring script integrated with Azure Monitor

## Author
Suryakanth S — suryade360@gmail.com
