import requests

url = "http://127.0.0.1:9696/diabetesrisk"

patient = {
    "gender":"male",
    "age":50,
    "hypertension": 0,
    "heart_disease": 0,
    "smoking_history": "current",
    "bmi": 25.31,
    "hba1c_level":7.0,
    "blood_glucose_level":220
}
res= requests.post(url, json=patient).json()


print(res)