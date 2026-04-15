from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and feature names
model = joblib.load("nids_model.pkl")
feature_names = joblib.load("feature_names.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Prepare input for ML model
    input_data = [data.get(feature, 0) for feature in feature_names]
    input_array = np.array(input_data).reshape(1, -1)

    # Extract key features for rule-based detection
    src_bytes = data.get("src_bytes", 0)
    dst_bytes = data.get("dst_bytes", 0)
    flag = data.get("flag", 0)
    protocol = data.get("protocol_type", 0)

    # 🚨 HYBRID DETECTION LOGIC (FINAL)

    # Strong attack: high traffic but no response
    if src_bytes > 10000 and dst_bytes == 0:
        prediction = 1
        confidence = 99.0

    # Suspicious flags (connection failed/rejected)
    elif flag in [1, 2]:  # S0 or REJ
        prediction = 1
        confidence = 95.0

    # ICMP abnormal behavior (common in ping attacks)
    elif protocol == 2 and src_bytes > 5000:
        prediction = 1
        confidence = 93.0

    else:
        # Use ML model
        prediction = model.predict(input_array)[0]
        confidence = max(model.predict_proba(input_array)[0]) * 100

    # Final result text
    result = "🚨 Attack Detected" if prediction == 1 else "✅ Normal Traffic"

    return jsonify({
        "result": result,
        "confidence": round(confidence, 2)
    })


if __name__ == "__main__":
    # Disable reloader to avoid Windows error
    app.run(debug=True, use_reloader=False)