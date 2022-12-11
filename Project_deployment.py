
import streamlit as st
import pandas as pd



st.title("Welcome to Telecom Project")


st.sidebar.header('User Input Parameters')
    



def user_input_features():
    
    al = st.sidebar.number_input("Insert the account_length")
    vmm = st.sidebar.number_input("Insert the voice_mail_messages")
    csc = st.sidebar.number_input("Insert the customer_service_calls")
    ip = st.sidebar.selectbox("Insert the international_plan",(0,1))
    dcall = st.sidebar.number_input("Insert the day_calls")
    dc = st.sidebar.number_input("Insert the day_charge")
    ecall = st.sidebar.number_input("Insert the evening_calls")
    ec = st.sidebar.number_input("Insert the evening_charge")
    ncall = st.sidebar.number_input("Insert the night_calls")
    nc = st.sidebar.number_input("Insert the night_charge")
    icall = st.sidebar.number_input("Insert the international_calls")
    ic = st.sidebar.number_input("Insert the international_charge")
    tc = st.sidebar.number_input("Insert the total_charge")
    
    
    new = {
         'account_length': al,
         'voice_mail_messages':vmm,
         'customer_service_calls':csc,
         'international_plan': ip,
         "day_calls": dcall,
         "day_charge": dc,
         "evening_calls": ecall,
         "evening_charge": ec,
         "night_calls": ncall,
         "night_charge": nc,
         "international_calls": icall,
         "international_charge": ic,
         "total_charge": tc,
                         
            }
    features = pd.DataFrame(new,index = [0])
    return features 

telecom = user_input_features()
st.write(telecom)


import pickle

with open(file="Churn_Final_Model.pkl",mode="rb") as f:
    model = pickle.load(f)
    

st.write("Model loaded")



prediction = model.predict(telecom)

prediction_proba = model.predict_proba(telecom)

st.subheader('Prediction_Result')

st.write('*** CUSTOMER CHURN ***' if prediction_proba [0][1] > 0.5
         else '*** CUSTOMER WILL NOT CHURN ***')








