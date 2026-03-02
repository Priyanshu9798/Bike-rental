import joblib
import pandas as pd
import streamlit as st
import pathlib

# "#444253ff"
# "#9f9f9fff"
# "#2c255cff"
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")


css_path = pathlib.Path("assests/style.css")
load_css(css_path)
st.title("Bike Price Prediction app")

col1, col2 = st.columns(2)
model = joblib.load("used_bike_price_model.joblib.gz")


with col1:
    st.subheader("Using historic Dataset")
    st.image("bike.jpg")
with col2:

    bike_model =  st.text_input("Enter bike Model Name")
    if bike_model:
        st.success(f"Successfully Selected {bike_model}")

    model_year = st.slider("Select Model Year", min_value=2000, max_value=2025, value=2018, step=1 )

    kms_driven = st.number_input("Enter Kms Driven")
    if kms_driven:
        st.success(f"Successfully Select {kms_driven}")

    owner = st.selectbox("Owner type", ["first owner", "second owner", "third owner"])

    location = st.text_input("City / location (e.g., delhi)") 
    if location:
        st.success(f"Successfully Selected {location}")   

    mileage = st.number_input("Mileage (kmpl)", min_value=0.0, max_value=150.0, value=45.0, step=1.0)


    cc = st.slider("Engine capacity (cc)", min_value=50, max_value=500, value=100, step=5)

    def cc_to_bhp(cc_value):
        return cc_value * 0.08

    if st.button("Predict Price",key="button"):
        power_bhp = cc_to_bhp(cc)

        data = pd.DataFrame({
            "model_name": [bike_model],
            "owner": [owner],
            "location": [location.lower()],
            "model_year": [int(model_year)],
            "kms_driven": [int(kms_driven)],
            "mileage":[float(mileage)],
            "power":[float(power_bhp)]

        }) 

        price_pred = model.predict(data)[0]
        st.subheader("Estimated Price")
        st.success(f"Your bike estimated price: ₹{price_pred:,.0f}")
        
st.subheader("Connect Me")
st.link_button("GitHub", "https://github.com/Priyanshu9798")
st.link_button("LinkedIn", "https://www.linkedin.com/in/priyanshu-kumar-73995b306/")