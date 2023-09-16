from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import pandas as pd

app = Flask(__name__)
model_path='/Users/zeelpatel/PycharmProjects/flaskProject1/trained_model.h5'
model = load_model(model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get customer data from the form
            customer_data = {
                'subscription_months': float(request.form['subscription_months']),
                'monthly_bill': float(request.form['monthly_bill']),
                'total_usage_gb': float(request.form['total_usage_gb']),
                # Add more features as needed
            }

            # Convert the customer data to a DataFrame
            input_data = pd.DataFrame([customer_data])

            # Make predictions using the loaded Keras model
            prediction = model.predict(input_data)

            # Format the prediction
            formatted_prediction = "Churn" if prediction[0][0] >= 0.75 else "No Churn"

            # Pass the prediction to the results template
            return render_template('results.html', prediction=formatted_prediction)
        except Exception as e:
            error_message = str(e)
            return render_template('index.html', error=error_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
