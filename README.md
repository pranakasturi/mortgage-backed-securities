# Machine Learning Flask Docker App for Mortgage Backed Securities with Prometheus Metrics

This repository contains a Dockerized Flask application that leverages various machine learning models (Logistic Regression, XGBoost, Gradient Boosting, and Linear Discriminant Analysis - LDA) to predict the probability of default for Mortgage Backed Securities (MBS). The application exposes an API endpoint for making predictions and integrates Prometheus for monitoring key performance indicators.

## Overview

The goal of this project is to provide a scalable and easily deployable solution for MBS default prediction. It incorporates:

* **Multiple Machine Learning Models:** Implements and allows for comparison of Logistic Regression, XGBoost, Gradient Boosting, and LDA models.
* **Flask API:** Provides a simple and intuitive RESTful API for submitting MBS data and receiving default probability predictions.
* **Dockerization:** Packages the application and its dependencies into a Docker container for easy deployment across different environments.
* **Prometheus Metrics:** Exposes key application metrics in the Prometheus format, enabling monitoring and alerting.

## Repository Structure
<pre>
text
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

#### Accessing the Application
Once the Docker container is running, you can access the Flask API at http://localhost:5000.

## API Endpoints
The application exposes the following API endpoint:
The application exposes the following API endpoint:
•	/predict (POST): 
o	Description: Accepts JSON data representing the features of an MBS and returns the predicted probability of default.
o	Request Body (JSON): The JSON payload should contain the features required by the trained machine learning models. The specific features will depend on the data used for training. Example: 

```
JSON
{
  "credit_score": 700,
  "ocltv": 83.3,
  "dti": 36.5,
  "originali_upb" : 250000,
  "original_interest_rate": 3.75
}
```
Note: Ensure the feature names and data types in your request match the expectations of the trained models.
o	Response (JSON): 
```
JSON
{
  "logistic_regression": 1,
  "xgboost": 1,
  "gradient_boosting": 1,
  "lda": 0
}
```
The model field indicates which model was used for the prediction (this might be configurable or a default). The probability_of_default field contains the predicted probability.

