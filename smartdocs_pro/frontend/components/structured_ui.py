import streamlit as st

def structured_ui(structured_data, inference_time=None):
    st.subheader("Structured Data")
    st.json(structured_data)
    if inference_time:
        st.caption(f"Inference time: {inference_time:.2f} seconds") 