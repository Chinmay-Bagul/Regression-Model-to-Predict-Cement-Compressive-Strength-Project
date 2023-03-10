# -*- coding: utf-8 -*-
"""Regression Model to Predict Cement Compressive Strength Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15m69ch9nWaxq_eBP82mTJxP-VzgXecZm

## Regression Model to Predict Cement Compressive Strength Project
"""

# import library
import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

# import data
cement = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Concrete%20Compressive%20Strength.csv')

# view data
cement.head()

# info of data
cement.info('info')

# summary statistics
cement.describe()

# check for missing value
cement.isna().sum()

# check for categories
cement.nunique()

# visualize pairplot
import seaborn
seaborn.pairplot(cement)

# correlation
cement.corr()

# column names
cement.columns

# define y
y = cement['Cement (kg in a m^3 mixture)']

# define x
x = cement.drop('Cement (kg in a m^3 mixture)', axis=1)

# train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.7, random_state=2529)

# verify shape
x_train.shape, x_test.shape, y_train.shape, y_test.shape

# select model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# train model
model.fit(x_train,y_train)

# predict with model
y_pred=model.predict(x_test)

"""## model evaluation"""

# model accuracy
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

# model MAE
mean_absolute_error(y_test,y_pred)

# model MAPE
mean_absolute_percentage_error(y_test,y_pred)

# model MSE
mean_squared_error(y_test,y_pred)

# future prediction
sample=cement.sample()
sample

# define X_new
x_new=sample.loc[:,x.columns]
x_new

# predict for X_new
model.predict(x_new)