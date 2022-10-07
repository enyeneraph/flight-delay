import pickle
import xgboost as xgb
import pandas as pd
import json

filename = 'finalized_model.sav'

def predict(data, file=filename):
    loaded_model = pickle.load(open(file, 'rb'))
    prediction = loaded_model.predict(data)
    return_value = ['No Flight Delay', 'Flight Delay']
    if prediction[0] == 0:
        return return_value[0]
    else:
        return return_value[1]
    