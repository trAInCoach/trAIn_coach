from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.form.get("data")
    
    response = requests.post("http://127.0.0.1:5000/analyze", json={"data": [float(d) for d in data.split(",")]})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
