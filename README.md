# Multiple-Disease-Prediction-System
  A machine learning-based web application that predicts three different diseases: Diabetes, Heart Disease, and Breast Cancer.

Features
  Three Disease Prediction Models:
  
    Diabetes Prediction
    
    Heart Disease Prediction
    
    Breast Cancer Prediction
    
    User-friendly Interface:
    
    Interactive sidebar navigation
    
    Organized input fields
    
    Clear result display
    
Built with:

  Python
  Streamlit (for web interface)
  Scikit-learn (for machine learning models)

Installation
  Clone the repository:
    bash
    git clone https://github.com/yourusername/multiplediseasepredictionsystem.git
    cd multiplediseasepredictionsystem
    
  Install the required packages:
    bash
    pip install -r requirements.txt
    
  Run the application:
  
    bash
    streamlit run mutiplediseaseprediction1.py
Usage
  Select the disease you want to predict from the sidebar menu
  Fill in the required health parameters
  Click the prediction button
  View your results

Models Included
  Diabetes Prediction Model:
  
    Uses parameters like Glucose level, BMI, Age, etc.
  
  Heart Disease Prediction Model:
  
    Uses parameters like age, cholesterol levels, blood pressure, etc.
  
  Breast Cancer Prediction Model:
  
    Uses tumor characteristics like radius, texture, perimeter, etc.

File Structure
text
multiplediseasepredictionsystem/
├── mutiplediseaseprediction1.py       # Main application file
├── trained_model.sav                  # Diabetes prediction model
├── trained_heart_model.sav            # Heart disease prediction model
├── breast_cancer_model.sav            # Breast cancer prediction model
└── README.md                          # This file
Requirements
  Python 3.7+
  
  Streamlit
  
  Scikit-learn

  Pickle

Contributing
  Contributions are welcome! Please fork the repository and create a pull request with your changes.



