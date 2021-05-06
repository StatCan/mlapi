#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# RestAPI mlapi entry point 
# based on: https://github.com/rodrigo-arenas/fast-ml-deploy/blob/master/app.py
#
# (C) 2021 Statistics Canada
# Author: Andres Solis Montero
# -----------------------------------------------------------
from fastapi import FastAPI
from ml.classifier import IrisClassifier
from pydantic import BaseModel, conlist
from typing import List, Any
from fastapi import UploadFile

app = FastAPI(title="MLAPI Template", description="API for ml model", version="1.0")
"""FastAPI global app instance"""

class IrisPredictionInput(BaseModel):
    """
    Request data descrition containing a list of lists containing four 
    features (sepal length, sepal width, petal length, petal width) all 
    expressed in centimeters. 


    Examples:
        ```
        instance = IrisPredictionInput([[0,1,2,3]])
        ```
    """
    data: List[conlist(float, min_items=4, max_items=4)]

class IrisPredictionResponse(BaseModel):
    """
    Prediction response list and classes probabilities. 

    Examples:
        ```
        IrisPredictionResponse(prediction=[0], probability=[1.0, 0, 0])
        ```
    """
    prediction: List[int]
    probability: List[Any]

clf = IrisClassifier.load()
"""Global classifier instance"""

@app.get("/")
def read_root():
    """
    FastAPI GET route '/'

    Returns:
        dict:
            A dummy Hello World! dictionary
    """
    return {"Hello":"World!"}

@app.post("/predict",response_model=IrisPredictionResponse)
async def predict(iris: IrisPredictionInput) :
    """
    FastAPI POST route '/predict' endpoint for a prediction request
 
    Args:
        iris: IrisPredictionInput
            A list of list containing 4 features e.g., [[1,0,1,1]]

    Returns:
        IrisPredictionResponse:
            A prediction response object
    """
    return clf.predict(iris.data)

@app.post("/train")
async def train(gradient_boosting: bool = False) -> bool:
    """
    FastAPI POST route '/train' endpoint to train our model
 
    Args:
        gradient_boosting: bool
            A boolean flag to switch between a DTreeClassifier or GradientBoostClassifier

    Returns:
        bool:
            A boolean value identifying if trainning was successful.
    """
    data = clf.dataset()
    return clf.train(data['X'], data['y'], gradient_boosting)

