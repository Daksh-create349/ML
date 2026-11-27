import os
import streamlit as st
import pandas as pd
from pickle import load

st.title("Classification Model")
st.write("Will they hire an attorney?")

def create_page():

    age = st.sidebar.slider("Enter Age:", min_value=10, max_value=15)
    seat = st.sidebar.radio("Seatbelt:", [0, 1])
    amt = st.sidebar.number_input("Enter Amount:")
    gender = st.sidebar.radio("Gender:", [0, 1])
    insur = st.sidebar.selectbox("Life Insurance:", [0, 1])

    data = {
        "CLMSEX": gender,
        "CLMINSUR": insur,
        "SEATBELT": seat,
        "CLMAGE": age,
        "LOSS": amt
    }

    df = pd.DataFrame(data, index=[0])
    return df

features = create_page()

if st.sidebar.button('Submit'):
    st.write(features)

model_path = os.path.join(os.path.dirname(__file__), 'logistic_model.pkl')
loaded_model = load(open(model_path, 'rb'))
res = loaded_model.predict(features)

if res == 0:
    st.write('No, they will not hire an attorney')
else :
    st.write('Yes, they will hire an attorney')