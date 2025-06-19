# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 23:50:10 2025

@author: Dell
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/multiplediseasepredictionsystem/trained_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/multiplediseasepredictionsystem/trained_heart_model.sav','rb'))
breast_cancer_model = pickle.load(open('C:/multiplediseasepredictionsystem/breast_cancer_model.sav','rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction',
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Breast Cancer Prediction'],
                           
                           icons = ['activity','heart fill','lungs'],
                           
                           default_index=0)
    
if (selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction System Using ML ')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose	 = st.text_input('Enter Glucose	Level')
    BloodPressure = st.text_input('Enter BloodPressure')
    SkinThickness = st.text_input('Enter SkinThickness')
    Insulin = st.text_input('Enter Insulin')
    BMI	 = st.text_input('Enter BMI	')
    DiabetesPedigreeFunction = st.text_input('Enter DiabetesPedigreeFunction')
    Age	 = st.text_input('Enter Age	')
    
    #code for prediction 
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is non diabetic'
            
    st.success(diab_diagnosis)
            
    
    
    
    
if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction System Using ML ')
    
    # Adding Columns
    col1 , col2 , col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Number of age')
        
    with col2:
        sex = st.text_input('Number of sex')
    with col3:
        cp = st.text_input('Number of cp')
    with col1:
        trestbps = st.text_input('Number of trestbps')
    with col2:
        chol = st.text_input('Number of chol')
    with col3:
        fbs = st.text_input('Number of fbs')
    with col1:
        restecg = st.text_input('Number of restecg')
    with col2:
        thalach = st.text_input('Number of thalach')
    with col3:
        exang = st.text_input('Number of exang')
    with col1:
        oldpeak = st.text_input('Number of oldpeak')
    with col2:
        slope = st.text_input('Number of slope')
    with col3:
        ca = st.text_input('Number of ca')
    with col1:
        thal = st.text_input('Number of thal')
        
        
    diab_heart = ''
    
    if st.button('Heart Test Result'):
        diab_pred = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (diab_pred[0]==1):
            diab_heart = 'Heart Disease Patient'
            
        else:
            diab_heaet = 'Not a Heart Disease Patient'
            
    st.success(diab_heart)
    
if (selected == 'Breast Cancer Prediction'):
    
    st.title('Breast Cancer Prediction System Using ML ')
    
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        mean_radius = st.text_input('Number of mean_radius')
    with col2:
        mean_texture = st.text_input('Number of mean_texture')
    with col3:
        mean_perimeter = st.text_input('Number of mean_perimeter')
    with col4:
        mean_area = st.text_input('Number of mean area')
    with col5:
        mean_smoothness = st.text_input('Number of mean smoothness')
    with col1:
        mean_compactness = st.text_input('Number of mean compactness')
    with col2:
        mean_concavity = st.text_input('Number of mean concavity')
    with col3:
        mean_concave_points = st.text_input('Number of mean concave points')
    with col4:
        mean_symmetry = st.text_input('Number of mean symmetry')
    with col5:
        mean_fractal_dimension	 = st.text_input('Number of mean fractal dimension')
    with col1:
        radius_error = st.text_input('Number of radius error')
    with col2:
        texture_error = st.text_input('Number of texture error')
    with col3:
        perimeter_error = st.text_input('Number of perimeter error')
    with col4:
        area_error = st.text_input('Number of area error')
    with col5:
        smoothness_error = st.text_input('Number of smoothness error')
    with col1:
        compactness_error = st.text_input('Number of compactness error')
    with col2:
        concavity_error = st.text_input('Number of concavity error')
    with col3:
        concave_points_error = st.text_input('Number of concave points error')
    with col4:
        symmetry_error = st.text_input('Number of symmetry error')
    with col5:
        fractal_dimension_error = st.text_input('Number of  fractal dimension error')
    with col1:
        worst_radius = st.text_input('Number of  worst radius')
    with col2:
        worst_texture = st.text_input('Number of worst texture ')
    with col3:
        worst_perimeter = st.text_input('Number of worst perimeter')
    with col4:
        worst_area = st.text_input('Number of worst area')
    with col5:
        worst_smoothness = st.text_input('Number of worst smoothness')
    with col1:
        worst_compactness = st.text_input('Number of worst compactness')
    with col2:
        worst_concavity = st.text_input('Number of worst concavity')
    with col3:
        worst_concave_points = st.text_input('Number of worst concave points')
    with col4:
        worst_symmetry = st.text_input('Number of worst symmetry')
    with col5:
        worst_fractal_dimension = st.text_input('Number of worst fractal dimension')
        
        
    diab_breast =''
    
    if st.button('Breast Cancer Prediction'):
        diab_breast_pred = breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
        
        if (diab_breast_pred[0]==1):
            diab_breast = 'Patient of Breast Cancer'
            
        else:
            diab_breast = 'Patient Not Have Breast Cancer'
            
        st.success(diab_breast)
    
    