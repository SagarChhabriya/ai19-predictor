import streamlit as st 
import pickle

st.header("AI19 Salary Predictor")
st.set_page_config(page_title="AI19-Predictor", page_icon="💵")


with open("model.pkl", 'rb') as f:
    model = pickle.load(f)


yoe = st.number_input("Experience Years", min_value=0.0, max_value=10.0, step=0.5, value=2.0)

if st.button("Predict"):

    predictions = model.predict([[yoe]])

    st.success(predictions[0])

      