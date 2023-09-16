import requests

api_url = 'https://34.125.116.35:5000/predict'

customer_data = {
    'Subscription_Length_Months': 10,
    'Monthly_Bill': 100,
    'Total_Usage_GB': 5,
    # Add other customer data as needed
}

response = requests.post(api_url, json=customer_data)
if response.status_code == 200:
    prediction = response.json()['prediction']
    print(f'Churn Prediction: {prediction}')
else:
    print(f'Error: {response.status_code}')
