# File: main.py
# FastAPI application for predicting medical research classification using a my trained KNN model.
# @author: Soumit Kundu
# Email: soumitkundu@gmail.com
# Date: 2026-01-27

# importing required libraries
from fastapi import FastAPI
import uvicorn
import numpy as np
import pandas as pd
# import pickle
import joblib
from user_input_data import InputData

# initializing the app
app = FastAPI()

# loading the pre-trained model
model = joblib.load(open('models/best_model_pipeline.pkl', 'rb'))



@app.get("/")
def home():
    return {"message": "Hello, this is a FastAPI application for medical research classification prediction."}

@app.get('/{name}')
def get_name(name: str):
    return f"Welcome: {name}"

# defining the prediction endpoint
@app.post('/predict')
def predict_class(data: InputData):
    # converting input data to a DataFrame
    input_data = pd.DataFrame([data.dict()])

    # return {"input_data": input_data}
    
    # making the prediction
    prediction = model.predict(input_data)
    
    # returning the prediction
    return {"prediction": prediction[0]}

# running the app
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
