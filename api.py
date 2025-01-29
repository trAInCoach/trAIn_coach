from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

try:
    model = tf.keras.models.load_model("models/trAIn_model.h5")
    print("✅ AI model loaded successfully!")
except Exception as e:
    print(f"⚠️ Failed to load AI model: {e}")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json.get("data")

    if not data:
        return jsonify({"error": "No data provided"}), 400

  
    input_data = np.array(data).reshape(1, -1)
    prediction = model.predict(input_data)[0][0]

    response = {
        "status": "success",
        "analysis": "Good form" if prediction > 0.5 else "Needs improvement",
        "confidence": float(prediction)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
