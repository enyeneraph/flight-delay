import pickle
import xgboost as xgb
import pandas as pd
import json
# pickled_model = pickle.load(open('model.pkl', 'rb'))
# pickled_model.predict(X_test)

booster = xgb.Booster()
booster.load_model('test_model.bin')


def predict(data):
    
    pickled_model = pickle.load(open('LR_model.bin', 'rb'))
    prediction = pickled_model.predict(data)
    return_value = ['No Flight Delay', 'Flight Delay']
    if prediction[0] == 0:
        return return_value[0]
    else:
        return return_value[1]
    # booster = xgb.Booster()
    # booster.load_model('test_model.bin')
    # data = xgb.DMatrix(data.values)

    # print('final', data.shape)
    # clf = joblib.load(“rf_model.sav”)
    # return booster.predict(data.reshape((1,-1)))
    # with open('xgboost_native_model_from_test_model.pkl-0.bin','rb') as f:
    #     clf = pickle.load(f)
    # pd.DataFrame(data, columns=["MONTH_NAME", "DAY_NAME", "CARRIER_NAME", "DEPARTING_AIRPORT", "PREVIOUS_AIRPORT"])
    # return booster.predict(data)
    # return return_value[[prediction][0]]

# pickled_model = pickle.load(open('model.pkl', 'rb'))
# pickled_model.predict(X_test)