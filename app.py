# app.py
import streamlit as st
import pandas as pd
import joblib

# Basic Streamlit setup
st.set_page_config(page_title="Flat Price Predictor", layout="centered")

st.title("🏠 Mumbai Flat Price Prediction App")
st.write("""
Use the sidebar to:
- Predict Flat Prices 📈
- View Market Insights 📊
""")

# Load both saved models
stage1_model = joblib.load("catboost_stage1_location_model.pkl")
stage2_model = joblib.load("catboost_stage2_correction_model.pkl")

# Load Locations
locations = pd.read_csv("locations.csv")['location'].tolist()

# Sidebar: Input
st.sidebar.header("Enter Flat Details")

flat_types = ["1BHK", "2BHK", "3BHK", "4BHK", "5BHK", "6BHK"]
furnishing_options = ["Furnished", "Semi-Furnished", "Unfurnished"]
parking_options = ["yes", "no"]

flat_type = st.sidebar.selectbox("Flat Type", flat_types)
location1 = st.sidebar.selectbox("Location", locations)
buildupArea_sqft = st.sidebar.number_input("Built-up Area (sqft)", min_value=300, max_value=5000, step=100)
furnishing = st.sidebar.selectbox("Furnishing", furnishing_options)
parking = st.sidebar.selectbox("Parking", parking_options)

# Create Stage 1 input (for base location model)
stage1_input = pd.DataFrame({
    "location1": [location1]
})

# Create Stage 2 input (for correction model)
stage2_input = pd.DataFrame({
    "buildupArea_sqft": [buildupArea_sqft],
    "furnishing": [furnishing],
    "parking": [parking]
})

# Predict Button
if st.button("Predict Flat Price"):
    with st.spinner('Predicting... Please wait'):
        # Step 1: Predict Base Price using Location
        base_price = stage1_model.predict(stage1_input)[0]

        # Step 2: Predict Adjustment using Features
        correction = stage2_model.predict(stage2_input)[0]

        # Step 3: Final Prediction
        final_price = base_price + correction
        
        # Ensure the final price is not negative
        final_price = abs(final_price)

        st.subheader("🎯 Prediction Result")
        st.success(f"Estimated Flat Price: ₹{final_price:.2f} Crores")
        
        # Optional Confidence Interval
        rmse_estimate = 0.2  # around ±20 lakhs
        st.info(f"Expected Range: ₹{final_price - rmse_estimate:.2f} Cr - ₹{final_price + rmse_estimate:.2f} Cr")

# Footer
st.markdown("---")
st.caption("Thank you for using the app!  ❤️")

