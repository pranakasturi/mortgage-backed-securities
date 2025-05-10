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
<pre>
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
 ``` 
</pre>
---

## Technologies Used

* **Python:** The primary programming language.
* **Flask:** A micro web framework for building the API.
* **Scikit-learn:** A comprehensive library for machine learning algorithms (Logistic Regression, Gradient Boosting, LDA).
* **XGBoost:** A gradient boosting library known for its performance and scalability.
* **Pandas:** A powerful library for data manipulation and analysis.
* **NumPy:** A fundamental package for numerical computation.
* **Docker:** A platform for containerizing applications.
* **Prometheus:** An open-source system monitoring and alerting toolkit.

## Getting Started

Follow these steps to set up and run the application:

### Prerequisites

* **Docker:** Ensure you have Docker installed on your system. You can find installation instructions for your operating system on the official Docker website: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* **Docker Compose (Optional):** If you intend to use the `docker-compose.yml` file, ensure you have Docker Compose installed: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
* **Python 3.x:** While the application will run inside a Docker container, having Python installed can be helpful for local development or inspection.

### Installation and Running with Docker

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd machine-learning-flask-docker-mbs
    ```

2.  **Build the Docker image:**
    Navigate to the `docker` directory and build the Docker image using the Dockerfile:
    ```bash
    cd docker
    docker build -t mbs-prediction-app .
    cd ..
    ```
    Alternatively, if you are at the root of the repository, you can run:
    ```bash
    docker build -f docker/Dockerfile -t mbs-prediction-app .
    ```

3.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 mbs-prediction-app
    ```
    This command will run the Docker container and map the application's port 5000 to your host machine's port 5000.

### Running with Docker Compose (Optional)

If a `docker-compose.yml` file is provided (for potential multi-container setups, e.g., with a separate Prometheus instance), you can use the following command from the root of the repository:

```bash
docker-compose up -d
```

This will build and start all the services defined in the docker-compose.yml file in detached mode.
Accessing the Application
Once the Docker container is running, you can access the Flask API at http://localhost:5000.

### API Endpoints
The application exposes the following API endpoint:

API Endpoints
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

🤝 Contributing
