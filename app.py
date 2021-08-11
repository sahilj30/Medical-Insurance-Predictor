import numpy as np
import pandas as pd
import pickle
from pickle import load
import streamlit as st
import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


model=pickle.load(open('model.pkl','rb'))

def run():

    #st.title("Medical Insurance")
    html_temp = """
    <div style="background-color:#1ABC9C ;padding:10px">
    <h2 style="color:white;text-align:center;">Medical Insuarance Calculator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    Options = ["Predict Medical Insurance Charges","BMI Calculator"]
    choice = st.sidebar.radio("Select Options",Options)

    if choice == 'BMI Calculator':
        st.subheader("Calculate Your BMI")
 
       
        # TAKE WEIGHT INPUT in kgs
        weight = st.number_input("Enter your weight (in kgs)")
 
        # TAKE HEIGHT INPUT
        # radio button to choose height format
        status = st.radio('Select your height format: ',
                  ('centimeters', 'meters', 'feet'))
 
        # compare status value
        if(status == 'centimeters'):
            ## take height input in centimeters

            #st.text("Enter some value of height")
            
            height = st.number_input('Centimeters')
            #bmi = weight / ((height/100)**2)
            try:
                bmi = weight / ((height/100)**2)
            except:
                st.text("Enter some value of height in Centimeters")
         
        elif(status == 'meters'):
            # take height input in meters
            height = st.number_input('Meters')
     
            try:
                bmi = weight / (height ** 2)
            except:
                st.text("Enter some value of height in Meters")
         
        else:
            # take height input in feet
            height = st.number_input('Feet')
     
            # 1 meter = 3.28
            try:
                bmi = weight / (((height/3.28))**2)
            except:
                st.text("Enter some value of height in Feet")
 
        # check if the button is pressed or not
        if(st.button('Calculate BMI')):
     
            # print the BMI INDEX
            st.text("Your BMI Index is {}.".format(bmi))
     
            # give the interpretation of BMI index
            if(bmi < 16):
                st.error("You are Extremely Underweight")
            elif(bmi >= 16 and bmi < 18.5):
                st.warning("You are Underweight")
            elif(bmi >= 18.5 and bmi < 25):
                st.success("Healthy")       
            elif(bmi >= 25 and bmi < 30):
                st.warning("Overweight")
            elif(bmi >= 30):
                st.error("Extremely Overweight")

    elif choice == 'Predict Medical Insurance Charges':
        st.subheader("Calculate Your Insurance Charges")
    
        # for sex
        sex_display = ('Female','Male')
        sex_options = list(range(len(sex_display)))
        #sex = st.sidebar.selectbox("sex",sex_options, format_func=lambda x: sex_display[x])
        sex = st.selectbox("sex",sex_options, format_func=lambda x: sex_display[x])

        # For smoker
        smoker_display = ('No','Yes')
        smoker_options = list(range(len(smoker_display)))
        #smoker = st.sidebar.selectbox("smoker",smoker_options, format_func=lambda x: smoker_display[x])
        smoker = st.selectbox("smoker",smoker_options, format_func=lambda x: smoker_display[x])

        # For region
        region_display = ('northeast','northwest','southeast','southwest')
        region_options = list(range(len(region_display)))
        #region = st.sidebar.selectbox("region",region_options, format_func=lambda x: region_display[x])
        region = st.selectbox("region",region_options, format_func=lambda x: region_display[x])
    
    
        age = st.text_input("age","enter your age")
        bmi = st.number_input("bmi")
        children = st.text_input("children","enter no. of children you have")

        if st.button("Predit"):
            features = [[sex,smoker,region,age,bmi,children]]
            print(features)
            prediction = model.predict(features)
            prediction = round(float(prediction))
            st.success('Total Medical Insurance Charges : {} Rs.'.format(prediction))

    
run()

