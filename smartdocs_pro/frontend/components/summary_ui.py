import streamlit as st

def summary_ui(summary, inference_time=None):
    st.subheader("Summary")
    st.write(summary)
    if inference_time:
        st.caption(f"Inference time: {inference_time:.2f} seconds") 