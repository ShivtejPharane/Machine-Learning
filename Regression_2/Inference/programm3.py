import streamlit as st
import numpy as np
import pickle
#load the model
with open('./model.pkl','rb') as file:
    model = pickle.load(file)

#set the title of the app
st.title("GPA Prediction App")
#get the user input for SAT score
sat_score = st.number_input("Enter the SAT score:", min_value=0, max_value=1600, step=1)
#add a button to make the prediction
if st.button("Predict GPA"):
    gpa = model.predict([[sat_score]])
    st.success(f"Predicted GPA: {gpa[0]:.2f}")