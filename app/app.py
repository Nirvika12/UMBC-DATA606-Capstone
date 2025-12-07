import streamlit as st
import pandas as pd
import joblib

# --- Load model and scaler ---
model = joblib.load("app/logreg_model.pkl")
scaler = joblib.load("app/scaler.pkl")

st.set_page_config(page_title="Startup Success Predictor", layout="centered")


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/8297865/pexels-photo-8297865.jpeg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Startup Success Prediction App")

st.markdown("### Enter your startup details below:")

#  Create two columns for inputs 
col1, col2 = st.columns(2)

with col1:
    institution_type = st.selectbox(
        "Institution Type",
        ["Public", "Private", "Technical", "Non-tech"],
        help="Type of institution supporting the startup (e.g., Public university, Private college, etc.)"
    )
    
    project_domain = st.selectbox(
        "Project Domain",
        ["Agriculture Tech", "Finance Tech", "Green Tech", "Health Tech", "Education Tech"],
        help="Industry or sector the startup belongs to"
    )
    
    team_size = st.number_input(
        "Team Size",
        min_value=1, max_value=50, value=5, step=1,
        help="Number of students or founders in the startup team"
    )
    
    avg_team_experience = st.slider(
        "Avg Team Experience (years)",
        0.0, 10.0, 2.0,
        help="Average entrepreneurial or work experience (in years) among team members"
    )
    
    innovation_score = st.slider(
        "Innovation Score (0–1)",
        0.0, 1.0, 0.5,
        help="Measure of originality and novelty (0 = low innovation, 1 = highly innovative)"
    )
    
    funding_amount_usd = st.number_input(
        "Funding Amount (USD)",
        min_value=0.0,
        max_value=10_000_000.0,
        value=100_000.0,
        step=5000.0,     
        help="Initial funding received by the startup in U.S. dollars"
    )

with col2:
    year = st.number_input(
        "Year Submitted",
        min_value=2019, max_value=2025, step=1,
        help="Year the startup was submitted or evaluated (2019–2025)"
    )
    
    mentorship_support = int(st.checkbox(
        "Mentorship Support",
        help="Check if the startup received formal mentorship support"
    ))
    
    incubation_support = int(st.checkbox(
        "Incubation Support",
        help="Check if the startup received incubation or accelerator support"
    ))
    
    market_readiness_level = st.slider(
        "Market Readiness Level (1–5)",
        1, 5, 3,
        help="Stage of product readiness (1 = idea stage, 5 = market-ready product)"
    )
    
    competition_awards = st.number_input(
        "Competition Awards",
        0, 20, 1,
        help="Number of startup competitions or awards won"
    )
    
    business_model_score = st.slider(
        "Business Model Score (0–1)",
        0.0, 1.0, 0.5,
        help="Clarity and scalability of the business model (0 = unclear, 1 = very strong)"
    )
    
    technology_maturity = st.number_input(
        "Technology Maturity",
        min_value=1, max_value=5, value=5, step=1,
        help="Level of technology maturity (1 = prototype, 5 = production-ready)"
    )

# Prediction
st.markdown("---")
st.subheader("Get Your Prediction")

if st.button("Predict Startup Success"):
    # Create DataFrame for model
    input_data = pd.DataFrame([{
        "institution_type": institution_type,
        "project_domain": project_domain,
        "team_size": team_size,
        "avg_team_experience": avg_team_experience,
        "innovation_score": innovation_score,
        "funding_amount_usd": funding_amount_usd,
        "mentorship_support": mentorship_support,
        "incubation_support": incubation_support,
        "market_readiness_level": market_readiness_level,
        "competition_awards": competition_awards,
        "business_model_score": business_model_score,
        "technology_maturity": technology_maturity,
        "year": year
    }])

    # One-hot encode + align columns
    input_encoded = pd.get_dummies(input_data)
    for col in scaler.feature_names_in_:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[scaler.feature_names_in_]

    # Scale and predict
    input_scaled = scaler.transform(input_encoded)
    pred_prob = model.predict_proba(input_scaled)[0][1]
    pred_label = model.predict(input_scaled)[0]
    
    # Display results
    if pred_label == 1:
        st.success(f"✅ The startup is predicted to **SUCCEED** with probability {pred_prob:.2%}")
    else:
        st.error(f"⚠️ The startup is predicted to **NOT succeed**, with probability {pred_prob:.2%}")
