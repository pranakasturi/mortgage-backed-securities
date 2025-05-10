# Machine Learning Flask Docker App for Mortgage Backed Securities with Prometheus Metrics

This repository contains a Dockerized Flask application that leverages various machine learning models (Logistic Regression, XGBoost, Gradient Boosting, and Linear Discriminant Analysis - LDA) to predict the probability of default for Mortgage Backed Securities (MBS). The application exposes an API endpoint for making predictions and integrates Prometheus for monitoring key performance indicators.

## Overview

The goal of this project is to provide a scalable and easily deployable solution for MBS default prediction. It incorporates:

* **Multiple Machine Learning Models:** Implements and allows for comparison of Logistic Regression, XGBoost, Gradient Boosting, and LDA models.
* **Flask API:** Provides a simple and intuitive RESTful API for submitting MBS data and receiving default probability predictions.
* **Dockerization:** Packages the application and its dependencies into a Docker container for easy deployment across different environments.
* **Prometheus Metrics:** Exposes key application metrics in the Prometheus format, enabling monitoring and alerting.

## Repository Structure
├── app/
│   ├── predict_utils.py
│   ├── models/
│   │   ├── gradient_boosting.pkl
│   │   ├── lda.pkl
│   │   ├── logistic_regression.pkl
│   │   └── xgboost.pkl
│   ├── static/
│   │   └── (optional static files)
│   ├── templates/
│   │   └── # HTML templates
│   └── main.py         # Flask application entry point
├── data/
│   ├── (optional sample data files)
├── docker/
│   └── Dockerfile      # Docker configuration
├── metrics/
│   └── metrics.py      # Prometheus metrics implementation
├── notebooks/
│   └── (optional Jupyter notebooks for model development and analysis)
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── docker-compose.yml  # Docker Compose for multi-container setup

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
