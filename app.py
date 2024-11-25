import streamlit as st

st.set_page_config(layout="centered")

tab1,tab2,tab3,tab4,tab5 = st.tabs(["Cumulative","Overal","Axial","Radial","Tangential"])

with tab1:
    st.header("Cumulative Anomaly",anchor=False)
    st.image("cumulative.png")

with tab2:
    st.header("Overall Anomaly",anchor=False)
    st.image("overall.png")

with tab3:
    st.header("Axial Anomaly",anchor=False)
    st.image("axial.png")

with tab4:
    st.header("Radial Anomaly",anchor=False)
    st.image("radial.png")

with tab5:
    st.header("Tangential Anomaly",anchor=False)
    st.image("tangential.png")