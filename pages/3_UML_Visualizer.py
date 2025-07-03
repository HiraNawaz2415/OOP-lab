import streamlit as st
from utils.uml_parser import parse_cpp_file

# Inject custom CSS for sidebar + layout + text styling
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

    /* Headings and text elements in main content should be black by default */
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

    /* Custom white text for class output */
    .white-text {
        color: white !important;
    }

    /* Button styling */
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

    # Display Classes and Relations in WHITE text using custom div
    st.markdown(
        f"""
        <div class='white-text'>
            <h3>Classes found:</h3>
            <pre>{result["classes"]}</pre>
            <h3>Relations found:</h3>
            <pre>{result["relations"]}</pre>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Build Graphviz diagram with white boxes for classes
    diagram = "digraph G {\n  node [shape=record, style=filled, fillcolor=white];\n"

    for cls in result["classes"]:
        diagram += f'  {cls} [label="{{{cls}}}"];\n'

    for parent, child in result["relations"]:
        diagram += f'  {parent} -> {child};\n'

    diagram += "}"

    st.graphviz_chart(diagram)
