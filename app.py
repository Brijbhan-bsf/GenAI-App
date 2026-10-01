import streamlit as st

st.set_page_config(
    page_title="GenAI Deployment Demo",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 GenAI App Deployment")
st.write("Assignment 39 — Streamlit Cloud & Hugging Face Spaces")

st.info(
    "This is a deployment-ready Streamlit application. "
    "It can be deployed on Streamlit Cloud and Hugging Face Spaces."
)

st.header("Text Analyzer")

text = st.text_area(
    "Enter some text",
    placeholder="Type your text here..."
)

if st.button("Analyze Text"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        words = text.split()
        characters = len(text)
        lines = len(text.splitlines())

        st.subheader("Analysis")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Words", len(words))
        with col2:
            st.metric("Characters", characters)
        with col3:
            st.metric("Lines", lines)

        st.success("Application is working successfully!")

st.divider()
st.caption("GenAI Assignment 39 | Brijbhan Kumar")
