from collections import OrderedDict
from joblib import load


def encode_user_values(params):
    """
    Take in dictionary of values for the parameters and converts to format to be used by ML models
    - Hour 
    - Temp
    - Hum
    - Wind
    - Visb
    - Rainfall 
    - Snow
    - DWeek: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
    - Holiday 0 or 1
    - Fday: 0 or 1
    - Season: Autumn, Spring, Summer, Winter
    """
    # Initial checks
    if params["Holiday"] not in ["Yes", "No"]:
        raise ValueError("Holiday value must be Yes or No")

    if params["Fday"] not in ["Yes", "No"]:
        raise ValueError("Fday value must be Yes or No")
    
    if params["DWeek"] not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
        raise ValueError("Invalid day of week value")
    
    if params["Season"] not in ["Autumn", "Spring", "Summer", "Winter"]:
        raise ValueError("Season must be either Autumn, Spring, Summer, or Winter")
    
    """Order to follow internally
    ['Hour', 'Temp', 'Hum', 'Wind', 'Visb', 'Rainfall', 'Snow', 'Weekend',
       'Holiday', 'Fday', 'DWeek_Friday', 'DWeek_Monday', 'DWeek_Saturday',
       'DWeek_Sunday', 'DWeek_Thursday', 'DWeek_Tuesday', 'DWeek_Wednesday',
       'Seasons_Autumn', 'Seasons_Spring', 'Seasons_Summer', 'Seasons_Winter',
       'Count']"""
    
    ret_dict = OrderedDict()
    ret_dict["Hour"] = params["Hour"]
    ret_dict["Temp"] = params["Temp"]
    ret_dict["Hum"] = params["Hum"]
    ret_dict["Wind"] = params["Wind"]
    ret_dict["Visb"] = params["Visb"]
    ret_dict["Rainfall"] = params["Rainfall"]
    ret_dict["Snow"] = params["Snow"]
    ret_dict["Weekend"] = 1 * (params["DWeek"] in ["Saturday", "Sunday"])
    ret_dict["Holiday"] = 1 if params["Holiday"] == 'Yes' else 0
    ret_dict["Fday"] = 1 if params["Fday"] == 'Yes' else 0
    days = ["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday","Wedesday"]
    
    # Encode days
    for day in days: 
        if params["DWeek"] == day: 
            ret_dict["DWeek_" + day] = 1
        else:
            ret_dict["DWeek_" + day] = 0
    
    seasons = ["Autumn", "Spring", "Summer", "Winter"]
    for season in seasons: 
        if params["Season"] == season:
            ret_dict["Seasons_" + season] = 1
        else: 
            ret_dict["Seasons_" + season] = 0
            
    return list(ret_dict.values())


# CALL THIS FUNCTION WITH APPROPRIATE MODEL PATHS AND INPUT DATA TO GET PREDICTION
# also requires the function above (encode user values)
# defaults to SVM 
def predict_bike_count(raw_input, model_type='linear_regression'):
    """
    raw_input is a dictionary format with the following values
    - Hour 
    - Temp
    - Hum
    - Wind
    - Visb
    - Rainfall 
    - Snow
    - DWeek: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
    - Holiday 0 or 1
    - Fday: 0 or 1
    - Season: Autumn, Spring, Summer, Winter
    
    MMS_PATH: is the relative path to the min max scaler file
    MODEL_PATH: the relative path to the appropriate model file
    """
    path_base = "machine_learning/models"
    path_mms = f"{path_base}/min_max_scaler.joblib"
    path_model = f"{path_base}/{model_type}.joblib"

    encoded_values = encode_user_values(raw_input)
    scaler = load(path_mms) 
    scaled_values = scaler.transform([encoded_values])
    model = load(path_model)
    pred = model.predict(scaled_values)
    ret_val = round(pred[0])

    return ret_val
