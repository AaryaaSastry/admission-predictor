from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model/admission_model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Parse incoming JSON data
    data = request.get_json()

    # Extract features in the expected order
    features = [
        data.get("gpa", 0),
        data.get("tenthMarks", 0),
        data.get("twelfthMarks", 0),
        data.get("collegeName", "College_1"),
        data.get("location", "CityA"),
        data.get("metroProximity", 1),
        data.get("worldRanking", 1000),
        data.get("subjects", "Engineering"),
        data.get("scholarshipAvailability", 0),
        data.get("scholarshipAmount", 0)
    ]

    # Preprocess the input features if needed, e.g., scaling
    features_scaled = scaler.transform([features])

    # Make the prediction
    prediction = model.predict(features_scaled)

    # Return the prediction result
    return jsonify({"prediction": bool(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
