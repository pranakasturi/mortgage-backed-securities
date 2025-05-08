from flask import Flask, render_template, request
from predict_utils import make_prediction
from prometheus_flask_exporter import PrometheusMetrics

import logging

app = Flask(__name__)
metrics = PrometheusMetrics(app)
logging.basicConfig(level=logging.INFO)

prediction_counter = metrics.counter(
    'model_predictions_total', 'Total predictions by model',
    labels={'model': lambda: request.form.get('model', 'unknown')}
)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        model_key = request.form.get("model")

        try:
            # Retrieve form inputs safely
            CreditScore = request.form.get("CreditScore")
            OCLTV = request.form.get("OCLTV")
            DTI = request.form.get("DTI")
            OrigUPB = request.form.get("OrigUPB")
            OrigInterestRate = request.form.get("OrigInterestRate")

            # Validate presence
            if None in (CreditScore, OCLTV, DTI, OrigUPB, OrigInterestRate) or \
               "" in (CreditScore, OCLTV, DTI, OrigUPB, OrigInterestRate):
                raise ValueError("Please fill in all the input fields.")

            # Convert to float
            features = [
                float(CreditScore),
                float(OCLTV),
                float(DTI),
                float(OrigUPB),
                float(OrigInterestRate)
            ]

            # Make prediction
            result = make_prediction(model_key, features)
            if "prediction" in result:
                prediction = result["prediction"]
            else:
                error = result["error"]

        except Exception as e:
            error = f"Invalid input: {str(e)}"

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)
