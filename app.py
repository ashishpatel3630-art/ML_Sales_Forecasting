import streamlit as st
import pandas as pd
import joblib

model = joblib.load("sales_model.pkl")

st.title("📊 Sales Forecasting App")

month = st.number_input("Enter Month Number", min_value=0)

if st.button("Predict"):
    input_df = pd.DataFrame({"Month_num": [month]})
    prediction = model.predict(input_df)

    st.success(f"Predicted Sales: {prediction[0]:.2f}")
    
    
    print("model updated")