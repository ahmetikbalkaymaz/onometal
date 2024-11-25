import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


st.set_page_config(layout="centered")

tab1,tab2,tab3,tab4,tab5 = st.tabs(["Cumulative","Overal","Axial","Radial","Tangential"])

df = pd.read_csv("fuel.csv")
df= df.drop(columns=["Unnamed: 0"],axis=1)


data = {
    "Category":["Anomaly","Normal"],
    "Count":[31,357]
}
with tab1:
    st.header("Cumulative Anomaly",anchor=False)
    st.image("cumulative.png")
    st.data_editor(df)
    fig1 = px.pie(data, values='Count', names='Category', title="Anomaly Percentage")
    st.plotly_chart(fig1)
    x_values = ['consume', 'speed', 'sun', 'temp_inside', 'AC', 'rain', 'fuel_lt']
    y_values = [10, 6, 5, 4, 2, 2, 1]

    # Plotly ile bar grafiği oluşturma
    fig = go.Figure([go.Bar(x=x_values, y=y_values)])

    # Grafik başlıkları ve eksen adlarını ekleme
    fig.update_layout(
        title='Anomaly Reasons Count',
        xaxis_title='Anomaly_Reason',
        yaxis_title='Count'
    )

    # Plotly grafiğini Streamlit ile gösterme
    st.plotly_chart(fig)
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