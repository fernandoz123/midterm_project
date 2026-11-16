import requests
import json

patient = {
    "gender": "Male",
    "age": 68,
    "hypertension": 1,
    "heart_disease": 0,
    "smoking_history": "never",
    "bmi": 31.5,
    "HbA1c_level": 6.0,
    "blood_glucose_level": 201
}

host = "myfirstapp-env.eba-gm82p3zh.us-east-1.elasticbeanstalk.com"
url = f'http://{host}/predict'

response = requests.post(url, json=patient) 
result = response.json() 
print(result)