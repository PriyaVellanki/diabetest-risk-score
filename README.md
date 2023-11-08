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
git clone

### Acquiring Data

The data used for training this model is stored in `/data/diabetes_prediction_dataset.csv` in the repo.

### Using Docker Image

```
docker build -t {build-tag} .
```

```
docker run -it --rm -p 9696:9696 {build-tag}
```

`{build-tag}`: Specifies any user-defined tag for docker image. eg. `diabetes-risk-score:latest `

### Making predictions

By default, the patient parameters are set at:

```
    "gender": "male", 
    "diabetes": "yes", 
    "family_history": "yes", 
    "smoking": "yes", 
    "obesity": "yes", 
    "alcohol_consumption": "yes", 
    "diet": "unhealthy", 
    "previous_heart_problems": "yes", 
    "medication_use": "yes", 
    "country": "united_states", 
    "age": 75, 
    "cholesterol": 360, 
    "heart_rate": 85, 
    "exercise_hours_per_week": 8, 
    "stress_level": 10, 
    "sedentary_hours_per_day": 4.987731820348275, 
    "income": 181290, 
    "bmi": 38, 
    "triglycerides": 369, 
    "physical_activity_days_per_week": 2, 
    "sleep_hours_per_day": 3, 
    "systolic_bp": 200, 
    "diastolic_bp": 130
```
User may change the parameters to test out different scenarios by changing values or parameters in `predict-test.py`

#### Allowed parameters for features (with restrictions):

- gender: male/female
- diabetes - yes/no
- family_history - yes/no
- smoking - yes/no
- obesity - yes/no
- alcohol_consumption - none/light/moderate/heavy
- diet - healthy/average/unhealthy
- previous_heart_problems - yes/no
- medication_use - yes/no
- stress_level - 1-10
- sedentary_hours_per_day - 0-24
- physical_activity_days_per_week - 0-7
- sleep_hours_per_day - 0-24
- country - One of ['Argentina', 'Nigeria', 'Thailand', 'Spain', 'Germany', 'France',
       'South Africa', 'Colombia', 'Italy', 'China', 'Vietnam',
       'United States', 'Japan', 'Canada', 'India', 'United Kingdom',
       'New Zealand', 'Brazil', 'South Korea', 'Australia']

Once, user is happy with patient input, predictions can be made in a new console window inside the project folder.

```python
python predict-test.py
```

## Sample Output

Locally, user shoudl be able to get a similar output to the one shown below upon running all steps successfully.

![sample_output](output.JPG)

## Acknowledgement

The project has been created as part of ML ZOOMCAMP with the help of a colaborative slack community of DataTalks and specially Alexey.

## Feedback

