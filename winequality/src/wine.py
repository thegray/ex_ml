# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:18:22 2018

@author: Bangun

ML practice : wine quality (tutorial from elitedatascience.com)

Random Forest Regression
"""

import numpy as np
import pandas as pd

#sampling helper
from sklearn.model_selection import train_test_split

#preprocessing module
from sklearn import preprocessing

#random forest mode
from sklearn.ensemble import RandomForestRegressor

#cross-validation pipeline
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

#evaluation metrics
from sklearn.metrics import mean_squared_error, r2_score

#module for saving scikit-learn models
from sklearn.externals import joblib

######

datapath = r'..\data\winequality-red.csv'

data = pd.read_csv(datapath, sep=';')
#print(data.head())
#print(data.shape)
#print(data.describe())

######
#split data into training and test sets
y = data.quality
X = data.drop('quality', axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=123,
                                                    stratify=y)

######
#feature scaling
#standarization data, (feature - mean) / std deviation

#using transformer, save the means and std deviation for later use
scaler = preprocessing.StandardScaler().fit(X_train)

X_train_scaled = scaler.transform(X_train)

#print(X_train_scaled.mean(axis=0))
#print(X_train_scaled.std(axis=0))

X_test_scaled = scaler.transform(X_test)

#print(X_test_scaled.mean(axis=0))
#print(X_test_scaled.std(axis=0))

# OR

#using cross-validation pipeline
#pipeline with preprocessing and model
pipeline = make_pipeline(preprocessing.StandardScaler(),
                         RandomForestRegressor(n_estimators=100))

####
#hyperparameters

#get List of tunable hyperparameters
#print(pipeline.get_params())

#declare hyperparameters to tune
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}

#####
#Sklearn cross-validation with pipeline
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
#GridSearchCV essentially performs cross-validation 
#across the entire "grid" (all possible permutations) of hyperparameters

#fit and tune model
clf.fit(X_train, y_train)

#see the best parameters
#print(clf.best_params_)

#confirm model will be retrained
#print(clf.refit)

#####

#Predict time!
#Predict a new set of data
y_pred = clf.predict(X_test)

#evaluate the pefromance of the model, using the metrics ealier
print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))

#Save model to a .pkl file
modelpath = r'..\models\randomforest_regressor.pkl'
joblib.dump(clf, modelpath)

#use the model saved
loaded_clf = joblib.load(modelpath)

#predict data using loaded model
y_pred2 = loaded_clf.predict(X_test)
print(r2_score(y_test, y_pred2))
print(mean_squared_error(y_test, y_pred2))


