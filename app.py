import streamlit as st 
import joblib
import pandas as pd
@st.cache_resource
def load_model():
    return joblib.load("nutrient7_model.joblib")

model = load_model()

nutrients = ["Vitamin C", "Vitamin B12", "Calcium", "Protein", "Fiber", "Selenium", "Total Fat"]
st.set_page_config(page_title="Nutrient Deficiency Predictor", layout="wide")
st.title("AI-Based Nutrient Deficiency Predictor")
st.write("Fill in the details below to get predictions.")

st.markdown("---")


st.header("User Input")

col1, col2, col3 = st.columns(3)

with col1:
    RIDAGEYR = st.slider("Age", 1, 120, 25, help="Enter your age in years")
    RIAGENDR = st.selectbox("Gender", ["Male", "Female"])
    BMI = st.slider("BMI", 10.0, 60.0, 22.0, help="Body Mass Index (weight/height)")

with col2:
    fish_seafood = st.slider("Fish & Seafood Intake (per week)", 0, 50, 2)
    meat_poultry = st.slider("Meat & Poultry Intake (per week)", 0,50, 3)
    vegetables = st.slider("Vegetable Servings (per week)", 0, 70, 14)
    fruit = st.slider("Fruit Servings (per week)", 0, 70, 10)
with col3:
    diary = st.slider("Diary Servings (per week)", 0, 70, 7)
    legumes = st.slider("Legume Servings (per week)", 0, 70, 5)
    junk_processed_food = st.slider("Junk/processed Food (per week)", 0, 50, 3)
    activity_level = st.selectbox("Activity Level", ["Low", "Moderate", 'High'])
    ALQ130 = st.selectbox("Alcohol Intake", ["No", "Yes"])
    SMQ020 = st.selectbox("Smoking Status", ["No", "Yes"])
    PFQ059 = st.selectbox("Do you often feel fatigue?", ["No", "Yes"])

gender_map = {"Male": 0, "Female": 1}
activity_map = {"Low": 0, "Moderate": 1, "High": 2}
binary_map = {"No": 0, "Yes":1}

user_df = pd.DataFrame({
    "RIDAGEYR": [RIDAGEYR],
    "RIAGENDR": [gender_map[RIAGENDR]],
    "BMI": [BMI],
    "fish_seafood": [fish_seafood],
    "meat_poultry": [meat_poultry],
    "vegetables": [vegetables],
    "fruit": [fruit],
    "diary": [diary],
    "legumes": [legumes],
    "junk_processed_food": [junk_processed_food],
    "activity_level": [activity_map[activity_level]],
    "ALQ130":[binary_map[ALQ130]],
    "SMQ020": [binary_map[SMQ020]],
    "PFQ059": [binary_map[PFQ059]]
})


if st.button("Predict Deficiencies"):
    try:
        prediction = model.predict(user_df)[0]

        st.success("Prediction Complete!")
        st.subheader("Predicted Nutrient Deficienciencies:")
        deficient_nutrients = [nutrients[i] for i, val in enumerate(prediction) if val == 1]
        if deficient_nutrients:
            for n in deficient_nutrients:
                st.write(f"- {n}")
        else:
            st.write("No deficiencies predicted")

        st.subheader("All Nutrient Status:")
        for i, n in enumerate(nutrients):
            status = "Deficient" if prediction[i] == 1 else "Not Deficient"
            st.write(f"{n}: {status}")


    except Exception as e:
        st.error(f"An error occurred: {e}")