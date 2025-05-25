import streamlit as st
from predict import predict_toxicity

st.title("🛡️ Toxic Comment Classifier")
text = st.text_area("Enter a comment:")

if st.button("Classify"):
    if text.strip():
        results = predict_toxicity(text)
        st.subheader("Results:")
        for label, value in results.items():
            st.write(f"**{label}**: {value}")
    else:
        st.warning("Please enter some text.")
