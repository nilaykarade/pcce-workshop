import streamlit as st
import pickle
import numpy as np

st.image("car.png",width=100)
st.title("Nilay's AI based car price predcition")

st.header("Please enter car details")

kms=st.number_input("Enter kms",0,1000000)
age=st.number_input("Enter age",0,100)
op=st.number_input("Enter original price",0,10000000)
fuel=st.radio("Select fuel type",("Petrol","Diesel","CNG"))
transmission=st.radio("Select transmission type",("Manual","Automatic"))

button_clicked=st.button("Predict car price")

if button_clicked:
    #st.header(str(kms)+str(age)+str(op)+fuel+transmission)
    if fuel=="Petrol":
        fuel=list([0,0,1])
    elif fuel=="Diesel":
        fuel=list([0,1,0])
    else:
        fuel=list([1,0,0])

    if transmission=="Manual":
        transmission=list([0,1])
    else :
        transmission=list([1,0])
        #[[100000,10000000,10,0,0,1,1,0]]
    data=[np.array([kms,op,age,fuel[0],fuel[1],fuel[2],transmission[0],transmission[1]])]
    model=pickle.load(open("lr_model.pkl","rb"))
    prediction=model.predict(data)
    st.header("Predicted car price is "+prediction[0])
    
    