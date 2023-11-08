# Diabetes Prediction

## Problem Description

The outline of the project is to predict whether a patient is prone to risk of a heart attack or not, using different health parameters.

## About the Dataset
 
The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes.

This dataset provides a comprehensive array of features relevant to heart health and lifestyle choices, encompassing patient-specific details such as age, gender, cholesterol levels, blood pressure, heart rate, and indicators like diabetes, family history, smoking habits, obesity, and alcohol consumption. Additionally, lifestyle factors like exercise hours, dietary habits, stress levels, and sedentary hours are included. Medical aspects comprising previous heart problems, medication usage, and triglyceride levels are considered. Socioeconomic aspects such as income and geographical attributes like country, continent, and hemisphere are incorporated. The dataset, consisting of around 7000 records from patients around the globe, culminates in a crucial binary classification feature denoting the presence or absence of a heart attack risk, providing a comprehensive resource for predictive analysis and research in cardiovascular health.

## How to Use 

### Prerequisites

```
python 3.10
docker
```

### Cloning the repo

First and foremost, the repo needs to cloned to local for usage. This can be achieved using:

```python
git clone https://github.com/PriyaVellanki/diabetest-risk-score.git
```

### Acquiring Data

The data used for training this model is stored in `/data/diabetes_prediction_dataset.csv` in the repo.

### Using Docker Image

Build Docker Image

```
docker build -t {build-tag} .
```
Run the docker image

```
docker run -it --rm -p 9696:9696 {build-tag}
```


`{build-tag}`: Specifies any user-defined tag for docker image. eg. `diabetes-risk-score:latest `

### Making predictions

By default, the patient parameters are set at the following for test service:

```
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
```

To test the model with specific input and check the prediction probablity value.

```python
python predict_test_using_model.py
```
To test the model using API endpoint either after starting gunicorn loclaly or after docker deployment.

```python
python test_predict_api.py
```

## Sample Output

Locally, user shoudl be able to get a similar output to the one shown below upon running all steps successfully.



## Acknowledgement

The project has been created as part of ML ZOOMCAMP with the help of a colaborative slack community of DataTalks and specially Alexey.

## Feedback

