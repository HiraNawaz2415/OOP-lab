import streamlit as st


st.set_page_config(page_title="C++ OOP Course", layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
      background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Main content area background */
    [data-testid="stAppViewContainer"] {
        background-color: white;
    }

    /* Headings and text elements in main content should be black */
    [data-testid="stAppViewContainer"] h1,
    [data-testid="stAppViewContainer"] h2,
    [data-testid="stAppViewContainer"] h3,
    [data-testid="stAppViewContainer"] h4,
    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] span,
    [data-testid="stAppViewContainer"] li,
    [data-testid="stAppViewContainer"] div {
        color: black;
    }

    /* Button text white, background green */
    [data-testid="stAppViewContainer"] button {
        color: white !important;
        background-color: #56ab2f !important;
    }

    /* Inputs and selectbox background white */
    [data-testid="stAppViewContainer"] input,
    [data-testid="stAppViewContainer"] select {
        background-color: white !important;
        color: black !important;
    }

    /* Code blocks background white, text black */
    [data-testid="stAppViewContainer"] pre,
    [data-testid="stAppViewContainer"] code {
        background-color: white !important;
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("🏫 Welcome to the C++ OOP Course!")

st.markdown("""
This interactive app helps you **learn, practice, and master** Object-Oriented Programming in C++.

**What you can do:**
- 🧩 Write & run C++ code
- 📈 Visualize UML class diagrams
- ✅ Take quizzes & challenges
- 🎓 Track your progress
- 🗂️ Download slides & notes

👉 Use the sidebar to navigate through the pages!
""")

st.image("CS/assets/logo.png", width=200)
