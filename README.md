### Boston House Pricing Prediction
A machine learning web application that predicts Boston house prices based on various input features. Built using **Flask**, **scikit-learn**, and deployed via **Docker**.

## Project Overview

This project includes:

- A trained regression model (Linear Regression)
- A Flask-based web interface for interaction
- REST API for predictions
- Automated testing using pytest
- Dockerized for easy deployment

### Software tools and requirements

1. [GithubAccount] (https://github.com)
2. [VSCodeAccount] (https://code.visualstudio.com)
3. [GitCLI] (https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
4. Python 3.9

Create a new environment
```
python -m venv venv
.\venv\Scripts\Activate
```

### Running the App
To start the Flask app locally: 
```
python app.py
```
The app will be available at: http://127.0.0.1:5000

### Running Tests
This project includes unit tests for both the API and the web form, written using the unittest framework but executed with pytest.
```
python test.py
```

### API Endpoint
/predict_api [POST]
Send JSON input like below to receive the predicted price:
```
{
  "data": {
    "CRIM": 0.1,
    "ZN": 18.0,
    "INDUS": 2.31,
    "CHAS": 0,
    "NOX": 0.538,
    "RM": 6.575,
    "Age": 65.2,
    "DIS": 4.09,
    "RAD": 1.0,
    "TAX": 296.0,
    "PTRATIO": 15.3,
    "B": 396.9,
    "LSTAT": 4.98
  }
}
```
### Pull the Docker Image and Run the Container
You can pull and run the Docker image for this project using the following commands:

🔽Pull the Image
```
docker pull arpitamallik23/boston-house-price
```
🚀Run the Container
```
docker run -p 5000:5000 arpitamallik23/boston-house-price
```
The app will be accessible at: http://localhost:5000

### Project Structure
```
├── app.py                  # Main Flask app
├── test.py                 # Unit tests
├── models/
│   ├── regmodel.pkl        # Trained regression model
│   └── scaling.pkl         # Scaler (StandardScaler or similar)
├── templates/
│   └── home.html           # Frontend UI
├── requirements.txt
├── Dockerfile
└── README.md
```