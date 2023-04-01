from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('C:/Users/Jagvir Dhesi/lighthouselabs/projects/deployment-project/data/loan_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return 'Loan Predictor 9000 ver 1.0'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the loan data from the request
    data = request.get_json()

    # Check if the 'loan_data' key exists in the data dictionary
    if 'loan_data' not in data:
        return jsonify({'error': 'Missing key: loan_data'})

    # Get the dictionary of features from the 'loan_data' key
    loan_data = data['loan_data']

    # Make the prediction
    prediction = model.predict([list(loan_data.values())])

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist(), 'message': 'Loan Predictor 9000 ver 1.0'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

