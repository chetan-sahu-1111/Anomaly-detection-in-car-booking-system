from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Load the trained model and feature scaler
model = IsolationForest(contamination=0.1, random_state=42)
# Load the model and scaler here (you need to train and save the model first)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        data = request.form.to_dict()
        # Perform preprocessing and feature engineering on input data
        # ...
        # Predict using the loaded model
        prediction = model.predict(pd.DataFrame([data]))[0]
        if prediction == -1:
            result = "Anomaly Detected!"
        else:
            result = "No Anomaly Detected."
        return render_template('result.html', result=result)
    except Exception as e:
        print(str(e))
        return 'Error occurred.'

if __name__ == '__main__':
    app.run(debug=True)
