import pickle
import streamlit as st



loaded_model = pickle.load(open('classifier.pkl', 'rb'))



    
    # page title
st.title('Breast Cancer Prediction using ML')
    
    
    # getting the input data from the user
col1, col2, col3 = st.columns(3)
    
    
with col1:
    radius_mean = st.number_input('Radius Mean', value=0.0)

with col2:
    texture_mean = st.number_input('Texture Mean', value=0.0)

with col3:
    smoothness_mean = st.number_input('Smoothness Mean', value=0.0)

with col1:
    compactness_mean = st.number_input('Compactness Mean', value=0.0)

with col2:
    symmetry_mean = st.number_input('Symmetry Mean', value=0.0)

with col3:
    fractal_dimension_mean = st.number_input('Fractal Dimension Mean', value=0.0)

with col1:
    radius_se = st.number_input('Radius Standard Error', value=0.0)

with col2:
    texture_se = st.number_input('Texture Standard Error', value=0.0)

with col3:
    smoothness_se = st.number_input('Smoothness Standard Error', value=0.0)

with col1:
    compactness_se = st.number_input('Compactness Standard Error', value=0.0)

with col2:
    symmetry_se = st.number_input('Symmetry Standard Error', value=0.0)

with col3:
    fractal_dimension_se = st.number_input('Fractal Dimension Standard Error', value=0.0)

         
diagnosis=''
      
      
if st.button('Breast Cancer Prediction'):
        
        diagnosis_pred= loaded_model.predict([[radius_mean,  texture_mean, smoothness_mean,
       compactness_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, smoothness_se, compactness_se,
       symmetry_se, fractal_dimension_se]])
        
        if (diagnosis_pred[0]==1):
             diagnosis= "Our analysis indicates the presence of malignant breast cancer."
        else:
             diagnosis= "Our assessment reveals no evidence of malignant breast cancer(Benign)."
        
st.success(diagnosis)
    
       
         
        
    
    

