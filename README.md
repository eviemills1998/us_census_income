# US Census Income Prediction
This repository contains a model to determine the factors influencing earnings above and below $50,000 in the United States based on the U.S. Census Income Dataset.

## Overview
The goal of this project is to predict whether an individual's income exceeds $50,000 based on various demographic and personal features. 

The project involves exploratory data analysis (EDA), building machine learning models, and extracting insights from the trained models.

## Scripts
### 1. eda.ipynb - Exploratory Data Analysis (EDA)
This Jupyter notebook performs an initial analysis of the dataset, including:

The goal of EDA is to better understand the dataset

## 2. modelling.ipynb - Model Building & Evaluation
This notebook builds and evaluates machine learning models to predict income classification:

XGBoost Classifier: A gradient boosting algorithm known for its effectiveness in handling structured/tabular data.
Random Forest Classifier: An ensemble learning method using multiple decision trees to make predictions.
The notebook includes:

Model training and tuning
Performance evaluation using metrics like accuracy, precision and recall.
Feature importance charts to visualise the most influential variables in the model's predictions.

### 3. insights.ipynb - Post-Modeling Insights
This notebook focuses on further exploring the features that were found to be most influential after modeling:
* Occupation
* Education
* Weeks worked per year

It’s more of an exploratory phase to dive deeper into the model's results to better understand the "why" behind the predictions.

### 4. project.py
A script to store file paths used throughout this project.
