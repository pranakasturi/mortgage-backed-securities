# 📈 Machine Learning Flask Docker App for Mortgage-Backed Securities with Prometheus Metrics

This repository contains a Dockerized Flask application that leverages various machine learning models (Logistic Regression, XGBoost, Gradient Boosting, and Linear Discriminant Analysis - LDA) to predict the probability of default for Mortgage-Backed Securities (MBS). The application exposes an API endpoint for making predictions and integrates Prometheus for monitoring key performance indicators.

---

## 📌 Overview

The goal of this project is to provide a scalable and easily deployable solution for MBS default prediction. It incorporates:

- **Multiple Machine Learning Models:** Logistic Regression, XGBoost, Gradient Boosting, and LDA.
- **Flask API:** RESTful API for submitting MBS data and receiving predictions.
- **Dockerization:** Containerized deployment using Docker.
- **Prometheus Metrics:** Monitoring with Prometheus-compatible metrics.

---

## 🗂️ Repository Structure

```text
├── app/
│   ├── predict_utils.py
│   ├── models/
│   │   ├── gradient_boosting.pkl
│   │   ├── lda.pkl
│   │   ├── logistic_regression.pkl
│   │   └── xgboost.pkl
│   ├── static/
│   ├── templates/
│   └── main.py         # Flask application entry point
├── data/
│   └── (optional sample data files)
├── docker/
│   └── Dockerfile
├── metrics/
│   └── metrics.py
├── notebooks/
│   └── (optional Jupyter notebooks)
├── requirements.txt
├── README.md
└── docker-compose.yml
🛠️ Technologies Used
Python

Flask

Scikit-learn

XGBoost

Pandas

NumPy

Docker

Prometheus

🚀 Getting Started
🔧 Prerequisites
Docker

Docker Compose (Optional)

Python 3.x (for local development)

🐳 Installation & Running with Docker
Clone the repository:

bash
Copy
Edit
git clone <repository_url>
cd machine-learning-flask-docker-mbs
Build the Docker image:

bash
Copy
Edit
docker build -f docker/Dockerfile -t mbs-prediction-app .
Run the Docker container:

bash
Copy
Edit
docker run -p 5000:5000 mbs-prediction-app
🧱 Running with Docker Compose (Optional)
If using docker-compose.yml, run:

bash
Copy
Edit
docker-compose up -d
🌐 Accessing the Application
Once running, access the API at:
http://localhost:5000

📬 API Endpoints
🔹 POST /predict
Description: Accepts MBS feature data and returns predicted probability of default.

Example Request Body:

json
Copy
Edit
{
  "feature1": 0.1,
  "feature2": 100000,
  "feature3": 0.05
}
Example Response:

json
Copy
Edit
{
  "model": "logistic_regression",
  "probability_of_default": 0.1532
}
🔸 Note: Ensure the feature names and data types match those used in training.

📈 Prometheus Metrics
The application exposes Prometheus metrics at:
GET /metrics

Visit:
http://localhost:5000/metrics

Example Metrics Output:

http_requests_total{method="POST", endpoint="/predict", status="200"}

model_prediction_latency_seconds_count{model="logistic_regression"}

app_uptime_seconds

To monitor with Prometheus, add a scrape config like:

yaml
Copy
Edit
scrape_configs:
  - job_name: 'ml-mbs-app'
    static_configs:
      - targets: ['localhost:5000']
🎯 Model Selection
Currently supported models:

Logistic Regression

XGBoost

Gradient Boosting

LDA

Model selection may be:

Configurable via environment variable or API input

Default set in app/main.py

🧪 Training the Models
This app uses pre-trained models saved in app/models/.

To use your own models:

Train models on your dataset.

Save them using pickle or joblib.

Replace files in app/models/ and align preprocessing in predict_utils.py.

🧱 Further Development Ideas
Model versioning & selection via API

Input validation (e.g., with Pydantic or Marshmallow)

Better error handling

Authentication/authorization

CI/CD integration

A/B testing support

Grafana integration for dashboards

Contributing
Contributions to this project are welcome. Please feel free to submit pull requests or open issues for bug fixes, feature requests, or improvements.
