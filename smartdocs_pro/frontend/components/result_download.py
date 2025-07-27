import streamlit as st
import json
import pandas as pd

def result_download(data, filename_prefix="result"):
    json_str = json.dumps(data, indent=2)
    st.download_button("Download JSON", json_str, file_name=f"{filename_prefix}.json", mime="application/json")
    # If data is tabular, offer CSV
    if isinstance(data, list) and data and isinstance(data[0], dict):
        df = pd.DataFrame(data)
        csv = df.to_csv(index=False)
        st.download_button("Download CSV", csv, file_name=f"{filename_prefix}.csv", mime="text/csv") 