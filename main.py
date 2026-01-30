# File: main.py
# FastAPI application for predicting medical research classification using a my trained KNN model.
# @author: Soumit Kundu
# Email: soumitkundu@gmail.com
# Date: 2026-01-27

# importing required libraries
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import numpy as np
import pandas as pd
# import pickle
import joblib
from user_input_data import InputData
import os

# initializing the app
app = FastAPI()

# loading the pre-trained model
model = joblib.load(open('models/best_model_pipeline.pkl', 'rb'))

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), 'static')
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def home():
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    index_path = os.path.join(static_dir, 'index.html')
    if os.path.exists(index_path):
        return FileResponse(index_path)
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
