import pickle
import os
from flask import Flask
from flask import request
from flask import jsonify


model_file = "rf.bin"


app = Flask('diabetesrisk')

def load_model():
    with open(model_file,'rb') as f_in:
      dv, model = pickle.load(f_in)  


    return dv,model
    
def predict_diabetes(client):
    dv, model = load_model()
    
    X= dv.transform([client])
    y_pred = model.predict_proba(X)[:,1]
    print(y_pred)
    return y_pred

@app.route('/diabetesrisk',methods=['POST'])
def predict():
    client = request.get_json()
    y_pred = predict_diabetes(client)
 
    risk = y_pred > 0.5

    result = {
       'Diabetest_Risk_probablity': float(y_pred),
       'Diabetes Risk': bool(risk)

    }
    return jsonify(result)

@app.route('/test',methods=['GET'])
def tets():
    return "Hello"

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0',port=9696)