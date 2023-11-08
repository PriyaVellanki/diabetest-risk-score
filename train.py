import numpy as np
import pandas as pd
import pickle
from sklearn import preprocessing

from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.ensemble import RandomForestClassifier



from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction import DictVectorizer



from sklearn.metrics import roc_auc_score
from sklearn.metrics import auc


# parameters
ESTIMATORS = 100 
MAX_DEPTH = 15
MIN_SAMPLES_LEAF=5
OUTPUT_FILE = 'rf.bin'




"""  Load the csv file using pandas read_csv. """





###Cleanup the data
def data_cleanse(df):
    ### There is 
    df = df[df.gender != "other"]
    df.columns = df.columns.str.lower().str.replace(' ', '_')   
    string_columns = list(df.dtypes[df.dtypes == 'object'].index)

    for col in string_columns:
        df[col] = df[col].str.lower().str.replace(' ', '_')

    df['smoking_history'] = df['smoking_history'].replace(["no_info"], "never")  



def split_data(df):
    df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=24)
    df_full_train = df_full_train.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)
    y_full_train = df_full_train.diabetes.values
    y_test = df_test.diabetes.values
 
    del df_full_train['diabetes']
    del df_test['diabetes']

    return df_full_train,df_test,y_full_train,y_test

print("Loading Data......\n")
df = pd.read_csv('./data/diabetes_prediction_dataset.csv')

print("Cleansing Data......\n")
data_cleanse(df)
print("Split Data for train and test data tests.....\n")
df_full_train,df_test,y_full_train,y_test = split_data(df)


dict_train_full = df_full_train.fillna(0).to_dict(orient='records')
dict_test = df_test.fillna(0).to_dict(orient='records')

print("Fit and Transform Data......\n")
dv = DictVectorizer(sparse=False)
X_train_full = dv.fit_transform(dict_train_full)
X_test = dv.transform(dict_test)
features = list(dv.get_feature_names_out())


print("Training the model .....\n")
rf = RandomForestClassifier(n_estimators=ESTIMATORS,
                            max_depth=MAX_DEPTH, 
                            min_samples_leaf=MIN_SAMPLES_LEAF,
                            random_state=1,
                            class_weight="balanced")

rf_final = rf.fit(X_train_full,y_full_train)



y_pred_rf = rf_final.predict(X_test)

print(y_test[:10])
auc = roc_auc_score(y_test,y_pred_rf)
print("Auc is {}".format(auc))




with open(OUTPUT_FILE, 'wb') as f_out:
    pickle.dump((dv, rf_final), f_out)

print(f'The model is saved to {OUTPUT_FILE}')












