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

API Endpoints
The application exposes the following API endpoint:

/predict (POST):
Description: Accepts JSON data representing the features of an MBS and returns the predicted probability of default.
Request Body (JSON): The JSON payload should contain the features required by the trained machine learning models. The specific features will depend on the data used for training. Example:
JSON

{
  "credit_score": 700,
  "ocltv": 83.3,
  "dti": 36.5,
  "originali_upb" : 250000,
  "original_interest_rate": 3.75
}
Note: Ensure the feature names and data types in your request match the expectations of the trained models.
Response (JSON):
JSON

{
  "logistic_regression": 1,
  "xgboost": 1,
  "gradient_boosting": 1,
  "lda": 0
}
The model field indicates which model was used for the prediction (this might be configurable or a default). The probability_of_default field contains the predicted probability.
Prometheus Metrics
The application exposes Prometheus metrics at the /metrics endpoint. You can configure Prometheus to scrape these metrics for monitoring.

To access the metrics, navigate to http://localhost:5000/metrics in your browser (while the application is running). You will see output in the Prometheus exposition format.

Example Metrics (may vary):

http_requests_total{method="POST", endpoint="/predict", status="200"}: Total number of successful prediction requests.
model_prediction_latency_seconds_count{model="logistic_regression"}: Total count of prediction requests for the Logistic Regression model.
model_prediction_latency_seconds_sum{model="logistic_regression"}: Total time spent on prediction requests for the Logistic Regression model in seconds.
model_prediction_latency_seconds_bucket{model="logistic_regression",le="0.01"}: Histogram of prediction latencies for the Logistic Regression model.
app_uptime_seconds: The total uptime of the application in seconds.
You can configure Prometheus by adding a job that targets your application's IP address and port (e.g., localhost:5000) and scrapes the /metrics endpoint.

Model Selection
The application currently implements Logistic Regression, XGBoost, Gradient Boosting, and LDA models. The specific model used for prediction might be:

Configurable via an environment variable or API parameter (implementation dependent).
Set to a default model in the application code.
Refer to the application's code (app/main.py and app/models/) to understand how the model selection is currently implemented.

Training the Models
This repository focuses on the deployment of pre-trained models. The process of training these models (data loading, preprocessing, feature engineering, model training, and saving) is typically done in separate scripts or notebooks (potentially found in the notebooks/ directory).

To use this application with your own data, you will need to:

Train the desired machine learning models (Logistic Regression, XGBoost, Gradient Boosting, LDA) on your MBS dataset.
Save the trained models in a format that can be loaded by the Flask application (e.g., using pickle or model-specific saving methods).
Update the application code (app/models/) to load your trained models and ensure the feature processing aligns with how the models were trained.
Further Development
Potential areas for further development include:

Model Persistence: Implement robust mechanisms for loading and managing different versions of trained models.
Model Selection API: Allow users to specify which model they want to use for prediction via the API request.
Input Data Validation: Add more comprehensive validation of the input JSON data.
Error Handling: Implement more detailed error handling and informative responses.
Authentication and Authorization: Secure the API endpoints.
Integration with Monitoring Tools: Provide example configurations for integrating with other monitoring and alerting tools.
A/B Testing: Implement the ability to A/B test different models.
CI/CD Pipeline: Set up a continuous integration and continuous deployment pipeline for automated builds and deployments.
Contributing
Contributions to this project are welcome. Please feel free to submit pull requests or open issues for bug fixes, feature requests, or improvements.
