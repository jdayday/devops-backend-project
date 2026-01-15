# DevOps Backend Project

![CI/CD Pipeline](https://github.com/<YOUR_GITHUB_USERNAME>/devops-backend-project/actions/workflows/ci-cd.yml/badge.svg)

## 📌 Overview
This project is a Python Flask backend application designed to demonstrate a complete DevOps lifecycle. It includes containerization, CI/CD automation, observability (logging/metrics), and security scanning (SAST/DAST).

The project satisfies the following requirements:
- **Backend:** Python Flask API (<150 lines).
- **Automation:** GitHub Actions for testing and security.
- **Containerization:** Docker & Docker Hub.
- **Orchestration:** Kubernetes (Minikube).
- **Observability:** Prometheus metrics & structured logging.

---

## 🛠️ Prerequisites
Before running this project, ensure you have the following installed:
- [Python 3.9+](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/)

---

## 🚀 1. Setup & Local Running Guide
Follow these instructions to run the application directly on your machine (without Docker).

### Step 1: Clone the Repository
```bash
git clone https://github.com/jdayday/devops-backend-project.git
cd devops-backend-project

