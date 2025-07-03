import streamlit as st
import requests
import time
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #a8e063 0%, #56ab2f 100%);
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




st.title(" C++ Code Playground")

code = st.text_area("Write your C++ code below:", """
#include<iostream>
using namespace std;

int main() {
    cout << "Hello, OOP!";
    return 0;
}
""", height=300)

if st.button("Run Code"):
    api_url = "https://judge0-ce.p.rapidapi.com/submissions"

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "4ed139f3e2msheba04539d9d3fc9p19f912jsn3c85daa29e31",
        "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
    }

    # Make submission
    submission = {
        "language_id": 54,  # 54 = C++ (GCC 9.2.0)
        "source_code": code,
        "stdin": ""
    }

    res = requests.post(api_url, json=submission, headers=headers)

    if res.status_code == 201:
        token = res.json()["token"]
        st.info(f"Submitted! Token: {token}")

        # Poll for result
        result = {}
        while True:
            check = requests.get(f"{api_url}/{token}", headers=headers)
            result = check.json()
            if result["status"]["id"] in [1, 2]:  # In queue or processing
                time.sleep(1)
            else:
                break

        if result["status"]["id"] == 3:
            st.success("Output:")
            st.code(result["stdout"])
        else:
            st.error(f"Error:\n{result.get('stderr', '')}")
    else:
        st.error(f"Submission failed:\n{res.text}")
