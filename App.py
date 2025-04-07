import streamlit as st
import pandas as pd
import pickle
import json

# Page config
st.set_page_config(page_title="Cardio Predict", page_icon="🫀", layout="centered")

# Title
st.markdown("<h1 class='header'>🫀 Cardio Predict</h1>", unsafe_allow_html=True)
st.write("Provide patient information below to assess heart disease risk.")

# Load model
model = pickle.load(open("./model/Model.pickle", "rb"))

# Load input fields
with open("./model/user_input.json", "r") as f:
    input_fields = json.load(f)

# Input form
with st.form("user_input_form"):
    st.markdown("### 📝 Patient Information Form")
    user_input = {}

    for field, values in input_fields.items():
        # If binary values only
        unique_vals = sorted(set(values))
        field_label = field.replace("_", " ").title()

        if set(unique_vals) == {0.0, 1.0}:
            if field == 'Gender':
                bool_map = {"👩 Female": 0.0, "👨 Male": 1.0}
            else:
                bool_map = {"❌ False": 0.0, "✅ True": 1.0}
            selected = st.selectbox(f"{field_label}", list(bool_map.keys()))
            user_input[field] = bool_map[selected]
        else:
            user_input[field] = st.selectbox(f"{field_label}", sorted(unique_vals))

    submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        input_df = pd.DataFrame([user_input])
        prediction = model.predict(input_df)[0]

        st.markdown("---")
        st.markdown("### 🧠 Prediction Result:")

        if prediction == 1:
            st.error("⚠️ **High Risk of Heart Disease**\n\nPlease consult a cardiologist.")
        else:
            st.success("✅ **Low Risk of Heart Disease**\n\nKeep up the healthy lifestyle!")
