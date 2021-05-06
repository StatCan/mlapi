#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Iris Classifier
#
# (C) 2021 Statistics Canada
# Author: Andres Solis Montero
# -----------------------------------------------------------
import numpy as np 
from os.path import exists
from joblib import dump
from joblib import load
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from pydantic import BaseModel, conlist
from typing import List, Any
from dataclasses import dataclass


MODEL_PATH = './ml/model.joblib'
"""Global variable containg the model path"""

@dataclass
class IrisClassifier:
    """
    A Iris classification model using sckit-learn iris dataset. 
    Iris data comes with 4 features (speal length, sepal width, petal length, petal width)
    and classifies each observation bewteen one of the three classes: 
    Iris Setosa, Iris Versicolour, and Iris Virginica.

    The classifier could be trained using a DecisionTreeClassifier or 
    GradientBoostringClassifier.  

    Examples:
        ```
        clf = IrisClassifier.load()

        clf = IrisClassifier()
        X = np.ndarray([...])
        y = np.ndarray([...])
        clf.train(X, y, gradient_boosting=True)
        clf.predict([[0,0,1,2]])
        ```

    """
    classifier : Pipeline   = None 

    def train(self, X: np.ndarray, y:np.ndarray, gradient_boosting:bool = False) -> bool:
        """
        Trains the Iris Classifier
       
        Args:
            X: np.ndarray
                A list of 4 feature input data
            y: np.ndarray
                Input labels

        Kwargs:
            gradient_boosting: bool=False
                flag to train with a GradientBoostringClassifier. If false
                a DecisionTree with random_state=42 will be use. 
        """
        clf = GradientBoostingClassifier() if gradient_boosting \
                                           else DecisionTreeClassifier(random_state=42) 
        self.classifier = Pipeline([
            ('scaling', MinMaxScaler()),
            ('clf', clf)
        ])
        self.classifier.fit(X,y)
        return True
    
    def predict(self, data: List[conlist(float, min_items=4, max_items=4)]) -> dict:
        """
        Predicts the classes and classes probabilities of a list of features. 
        Kwargs:
            data: List[conlist=4, max_items=4)]
                List of list containing only 4 features. 

        Returns:
            dict:
                Prediction classes and probabilities. 
        """
        prediction      = self.classifier.predict(data).tolist()
        probability     = self.classifier.predict_proba(data).tolist()
        print({"prediction": prediction,
                "probability": probability})
        return {"prediction": prediction,
                "probability": probability}

    def save(self, filename:str) -> None:
        """
        Saves the classifier to the specified filename path
        Args:
            filename: str
                output filename path.
        """
        dump(self.classifier, filename)
    
    @staticmethod
    def load(filename:str = MODEL_PATH) -> 'IrisClassifier':
        """
        Static factory method to return an instance of a IrisClassifier.
        If the filename doesn't exist a new classifier is created and trained
        with the default iris dataset. 
        Returns:
            IrisClassifier:
                [description]. Valid Values are [values]
        """
        if not exists(filename):
            data = IrisClassifier.dataset()
            clf  = IrisClassifier()
            clf.train(data['X'], data['y'])
            clf.save(filename)
            return clf 
        else:
            return IrisClassifier(load(filename))
    
    @staticmethod
    def dataset() -> dict:
        """
        Default dataset 
        Returns:
            dict:
                Training data and labels. 
        """
        dataset = datasets.load_iris()
        return {"X":dataset.data, 
                "y":dataset.target}


