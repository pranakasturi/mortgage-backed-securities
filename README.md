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

