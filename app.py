from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model  # Import the Keras load_model function
import pandas as pd  # For data preprocessing

app = Flask(__name__)
model_path='/Users/zeelpatel/PycharmProjects/flaskProject/trained_model.h5'
model = load_model(model_path)  # Replace with the path to your saved model

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get customer data from the request
        customer_data = request.json

        # Perform input validation and preprocessing here
        # For example, you can convert the incoming JSON to a DataFrame
        input_data = pd.DataFrame([customer_data])

        # Make predictions using the loaded Keras model
        prediction = model.predict(input_data)

        # Format the prediction
        formatted_prediction = "Churn" if prediction[0][0] >= 0.5 else "No Churn"

        # Return the prediction as a JSON response
        response = {'prediction': formatted_prediction}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
