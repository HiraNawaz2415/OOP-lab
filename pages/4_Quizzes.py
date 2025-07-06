import streamlit as st
import json
import os
import pandas as pd
from datetime import datetime
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



st.title(" C++ OOP Quiz")

# ✅ List of quiz topics
topics = [
    "Classes",
    "Inheritance",
    "Polymorphism",
    "Encapsulation",
    "Abstraction",
    "Constructors",
    "Access Specifiers",
    "Virtual Functions",
    "Templates",
    "Operator Overloading",
    "Exception Handling",
    "Pointers",
    "STL",
    "File I/O"
]

selected_topic = st.selectbox(" Select a topic to practice:", topics)
student_name = st.text_input("👤 Enter your name:")

# ✅ Correct relative path: up from pages/ to oop/questions/
filename = os.path.join(
    os.path.dirname(__file__),  # pages/
    "..",                       # -> oop/
    "questions",
    f"{selected_topic.lower().replace(' ', '_').replace('/', '_')}.json"
)

if not os.path.exists(filename):
    st.warning(f"🚧 Questions not added for **{selected_topic}** yet!\n\nPlease add `{filename}`.")
else:
    with open(filename, "r") as f:
        questions = json.load(f)

    if "score" not in st.session_state:
        st.session_state.score = 0

    st.write(f"### 📝 Topic: {selected_topic}")

    for idx, q in enumerate(questions):
        st.write(f"**Q{idx+1}: {q['question']}**")
        choice = st.radio("Select one:", q["options"], key=f"{selected_topic}_{idx}")
        if st.button(f"Submit Q{idx+1}", key=f"btn_{idx}"):
            if choice == q["answer"]:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Wrong! Correct answer: {q['answer']}")

    if st.button("Show Total Score"):
        st.info(f"**{student_name}**, you scored **{st.session_state.score} / {len(questions)}** for **{selected_topic}**.")

    if st.button("💾 Save Result"):
        if student_name.strip() == "":
            st.warning("⚠️ Please enter your name before saving!")
        else:
            results = {
                "Name": [student_name],
                "Topic": [selected_topic],
                "Score": [st.session_state.score],
                "Total": [len(questions)],
                "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            }
            df = pd.DataFrame(results)

            # ✅ Save inside oop/results/results.csv
            results_dir = os.path.join(os.path.dirname(__file__), "..", "results")
            os.makedirs(results_dir, exist_ok=True)  # Make the folder if missing
            results_file = os.path.join(results_dir, "results.csv")

            if os.path.exists(results_file):
                df.to_csv(results_file, mode="a", header=False, index=False)
            else:
                df.to_csv(results_file, index=False)

            st.success(f"Result saved!\n\n📁 You can find it here:\n`{results_file}`")

            # ✅ Optional: show download button
            with open(results_file, "rb") as file:
                st.download_button(
                    label="⬇️ Download all results",
                    data=file,
                    file_name="results.csv",
                    mime="text/csv"
                )

    if st.button("🔄 Reset"):
        st.session_state.score = 0
        st.rerun()
