from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("nids_model.pkl")
feature_names = joblib.load("feature_names.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    input_data = [data.get(feature, 0) for feature in feature_names]
    input_array = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_array)[0]
    confidence = max(model.predict_proba(input_array)[0]) * 100

    result = "🚨 Attack Detected" if prediction == 1 else "✅ Normal Traffic"

    return jsonify({
        "result": result,
        "confidence": round(confidence, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)