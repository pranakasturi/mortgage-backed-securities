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
