import streamlit as st
from utils.uml_parser import parse_cpp_file
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


st.title("📈 UML Visualizer")

uploaded_file = st.file_uploader("Upload a C++ file", type=["cpp", "h"])

if uploaded_file:
    with open("temp.cpp", "wb") as f:
        f.write(uploaded_file.read())

    result = parse_cpp_file("temp.cpp")

    st.write("Classes found:", result["classes"])
    st.write("Relations found:", result["relations"])

    diagram = "digraph G {\n  node [shape=record];\n"

    for cls in result["classes"]:
        diagram += f'  {cls} [label="{{{cls}}}"];\n'

    for parent, child in result["relations"]:
        diagram += f'  {parent} -> {child};\n'

    diagram += "}"

    st.graphviz_chart(diagram)
