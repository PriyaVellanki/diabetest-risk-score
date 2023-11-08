import pickle
import pandas as pd  


model_file = "rf.bin"

patient = {
    "gender":"male",
    "age":80.0,
    "hypertension": 0,
    "heart_disease": 0,
    "smoking_history": "ever",
    "bmi": 25.31,
    "HbA1c_level":8.0,
    "blood_glucose_level":220.0
}




with open(model_file,'rb') as f_in:
      dv, model  = pickle.load(f_in)  


X_test = dv.transform([patient])

print(X_test)
predict = model.predict(X_test)
print((predict).round(4))



