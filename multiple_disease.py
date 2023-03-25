# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:23:53 2023

@author: 91981
"""

import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path 
here = Path(__file__).parent

diabetes_model = pickle.load(open(here / 'diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open(here / 'trained_model.sav','rb'))

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('trained_model.sav','rb'))

#breat_cancer_model = pickle.load(open('C:/Users/91981/Downloads/Disease ML model/breast_cancer_model.sav','rb'))


#sidebar

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons= ['activity','heart'],
                           default_index = 0)
    
#Diabetes prediction page

if(selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction')
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.number_input('Glucose Level')
        
    with col3:
        BloodPressure = st.number_input('BloodPressure level')
        
    with col1:
        SkinThickness = st.number_input('SkinThickness')
    
    with col2:
        Insulin = st.number_input('Insulin Level')
        
    with col3:
        BMI = st.number_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.number_input('Age')
        
#code for prediction

    diab_diagnosis = ''
    
    if st.button("Diabetes test"):
        diab_prediction= diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        #input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        diab_prediction_input=np.asarray(diab_prediction)
        prediction=diab_prediction_input.reshape(1,-1)
        if (prediction[0]== 0):
            diab_diagnosis='The Person does not have diabetes'
        else:
            diab_diagnosis='The Person has diabetes'

     
    st.success(diab_diagnosis)
    
    
    
if(selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction')
    
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain Type')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
    
    with col2:
        chol = st.number_input('Serum Cholestrol in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic')
    
    with col2:
        thalach = st.number_input('Max Heart Rate Achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced')
        
    with col1:
        oldpeak = st.number_input('ST Depression induced by Exercise Relative To Rest')
        
    with col2:
        slope = st.number_input('Slope of Peak Exercise')
        
    with col3:
        ca = st.number_input('No of major vessels')
        
    with col1:
         thal = st.number_input('0= normal; 1= fixed defect; 2= reversable defect')
        
#code for prediction

    heart_dignosis = ''

    if st.button("Heart Disease test"):
        heart_prediction= heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
     
        if (heart_prediction[0]== 0):
            heart_dignosis='The Person does not Heart Disease'
        else:
            heart_dignosis='The Person has Heart Disease'

     
    st.success(heart_dignosis)
    
#if(selected == 'Breast Cancer Prediction'):
    
    #st.title('Breast Cancer Prediction')
    
    
    
