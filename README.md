# 📊 System Monitor Dashboard on Kubernetes

A **real-time system monitoring dashboard** built using **Flask**, **Prometheus**, and **Grafana**, all deployed on a **Kubernetes cluster using Minikube**.

This project demonstrates **container metrics collection**, **Kubernetes orchestration**, and **visualization of live app performance** in a DevOps-style observability stack.

---

## 🚀 Live Stack Overview

| Component     | Role                                           |
|--------------|------------------------------------------------|
| **Flask App** | Exposes a basic HTTP endpoint + custom metrics |
| **Prometheus** | Scrapes metrics from the Flask app            |
| **Grafana**   | Visualizes metrics with interactive dashboards |
| **Kubernetes**| Hosts and connects all services via YAML       |

---

## 📷 Demo Screenshot

> *(![Screenshot 2025-06-29 230358](https://github.com/user-attachments/assets/e61f1a91-1a4c-4a99-987d-99d25f516b7a))
*

---

## 📁 Project Structure

```
system-monitor-dashboard/
├── app/
│   ├── app.py               # Flask app exposing metrics
│   └── Dockerfile           # Docker config for app
├── prometheus/
│   └── prometheus.yml       # Prometheus scrape config
├── k8s/
│   ├── app-deployment.yaml      # Flask app K8s config
│   ├── prometheus-deployment.yaml # Prometheus config
│   ├── grafana-deployment.yaml    # Grafana config
└── README.md
```

---

## ⚙️ How to Run Locally

### 1️⃣ Start Minikube

```bash
minikube start
```

> Optional: use resources
```bash
minikube start --memory=4096 --cpus=2
```

---

### 2️⃣ Set Docker to Use Minikube

```bash
eval $(minikube docker-env)
```

---

### 3️⃣ Build the Flask App Docker Image

```bash
cd app
docker build -t flask-metrics-app .
```

---

### 4️⃣ Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

---

### 5️⃣ Access Grafana

```bash
minikube service grafana-service
```

📍 Default login:
- **Username**: `admin`
- **Password**: `admin`

🧠 Configure Prometheus as a new data source:
```
URL: http://prometheus-service.default.svc.cluster.local:9090
```

---

## 📌 What You’ll Learn

✅ Setting up container metrics with Prometheus  
✅ Building dashboards with Grafana  
✅ Deploying multi-container apps with Kubernetes  
✅ Writing YAML manifests (Deployment, Service, ConfigMap)

---

## 🧪 Sample Metric Exposed

The Flask app exposes:

```
/metrics
```

with:

```text
request_processing_seconds_count
```

This shows how many HTTP requests were handled and their durations — fully trackable via Prometheus and visualized in Grafana!

---

## 📖 License

> ✨ Free to use, remix, or extend for fun, learning, or demo purposes.

---

## 🙌 Acknowledgments

Inspired by the DevOps community and real-world observability tools used by engineers at scale.

Built with ❤️ by [Rahul Joshi](https://github.com/Rahuljoshi07)

---

## ⭐️ If you found this helpful...

Give this repo a ⭐ and consider sharing it with a fellow DevOps learner!
