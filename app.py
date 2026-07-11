import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("career_model.pkl")

st.set_page_config(page_title="Career Recommendation", page_icon="🎯")

st.title("🎯 AI Career Recommendation System")

st.write("Rate your skills from 0 to 10.")

python = st.slider("Python", 0, 10, 5)
sql = st.slider("SQL", 0, 10, 5)
java = st.slider("Java", 0, 10, 5)
ml = st.slider("Machine Learning", 0, 10, 5)
communication = st.slider("Communication", 0, 10, 5)
leadership = st.slider("Leadership", 0, 10, 5)
creativity = st.slider("Creativity", 0, 10, 5)

if st.button("Recommend Career"):

    user_data = pd.DataFrame([[
        python,
        sql,
        java,
        ml,
        communication,
        leadership,
        creativity
    ]], columns=[
        "Python",
        "SQL",
        "Java",
        "MachineLearning",
        "Communication",
        "Leadership",
        "Creativity"
    ])

    prediction = model.predict(user_data)[0]
    probabilities = model.predict_proba(user_data)[0]

    confidence = max(probabilities) * 100

    st.success(f"Recommended Career: **{prediction}**")
    st.info(f"Confidence: {confidence:.2f}%")

    career_info = {
        "Data Scientist": {
            "Skills": "Python, SQL, Statistics, Machine Learning",
            "Salary": "₹8–20 LPA"
        },
        "Software Engineer": {
            "Skills": "Java, C++, Data Structures",
            "Salary": "₹5–15 LPA"
        },
        "Data Analyst": {
            "Skills": "Excel, SQL, Power BI",
            "Salary": "₹4–10 LPA"
        },
        "AI Engineer": {
            "Skills": "Python, Deep Learning, TensorFlow",
            "Salary": "₹10–25 LPA"
        },
        "UI/UX Designer": {
            "Skills": "Figma, Adobe XD, Creativity",
            "Salary": "₹4–12 LPA"
        },
        "Digital Marketer": {
            "Skills": "SEO, Google Ads, Social Media",
            "Salary": "₹3–8 LPA"
        },
        "Project Manager": {
            "Skills": "Leadership, Agile, Communication",
            "Salary": "₹8–18 LPA"
        }
    }

    if prediction in career_info:
        st.subheader("Career Details")
        st.write("**Required Skills:**", career_info[prediction]["Skills"])
        st.write("**Average Salary:**", career_info[prediction]["Salary"])
