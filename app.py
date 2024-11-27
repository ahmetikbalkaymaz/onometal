import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

# Sayfa düzenini ayarlayın
st.set_page_config(layout="centered")

# Sekmeler oluşturma
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kümülatif", "Genel", "Aksiyel", "Radyal", "Tanjantiyel"])

# Veri yükleme
df = pd.read_csv("fuel.csv")
df = df.drop(columns=["Unnamed: 0"], axis=1)

# Anomali kategorileri ve sayıları
data = {
    "Kategori": ["Anomali", "Normal"],
    "Sayı": [31, 357]
}

with tab1:
    st.header("Kümülatif Anomali", anchor=False)
    cumulative_timestamp = pd.date_range(start='2024-07-10', end='2024-09-01', freq='D')
    cumulative_values = np.cumsum(np.random.normal(loc=0.001, scale=0.01, size=len(cumulative_timestamp))) + 0.44
    cumulative_values = np.clip(cumulative_values, 0.44, 0.53)

    # DataFrame oluşturma
    cumulative_data = pd.DataFrame({'Zaman Damgası': cumulative_timestamp, 'Genişleyen Ortalama (H Kolonu)': cumulative_values})

    # Grafik oluşturma
    fig_cumulative = go.Figure()

    # Çizgiyi ekleme
    fig_cumulative.add_trace(go.Scatter(x=cumulative_data['Zaman Damgası'], y=cumulative_data['Genişleyen Ortalama (H Kolonu)'],
                                        mode='lines',
                                        name='Genişleyen Ortalama (H Kolonu)',
                                        line=dict(color='blue')))

    # Layout ayarları
    fig_cumulative.update_layout(
        title="Kümülatif Anomali Skoru Zaman İçinde",
        xaxis_title="İndeks",
        yaxis_title="Genişleyen Ortalama (H Kolonu)"
    )

    # Streamlit ile grafiği gösterme
    st.plotly_chart(fig_cumulative)

    # Veri düzenleyici
    st.data_editor(df)

    # Pasta grafiği oluşturma
    fig1 = px.pie(data, values='Sayı', names='Kategori', title="Anomali Yüzdesi")
    st.plotly_chart(fig1)

    # Anomali nedenlerini tanımlama
    x_values = ['tüketim', 'hız', 'güneş', 'iç sıcaklık', 'klima', 'yağmur', 'yakıt_lt']
    y_values = [10, 6, 5, 4, 2, 2, 1]

    # Bar grafiği oluşturma
    fig = go.Figure([go.Bar(x=x_values, y=y_values)])

    # Grafik başlıkları ve eksen adlarını ekleme
    fig.update_layout(
        title='Anomali Nedenlerinin Sayısı',
        xaxis_title='Anomali Nedeni',
        yaxis_title='Sayı'
    )

    # Plotly grafiğini Streamlit ile gösterme
    st.plotly_chart(fig)

with tab2:
    st.header("Genel Anomali", anchor=False)
    timestamp = pd.date_range(start='2024-07-10', end='2024-09-01', freq='12H')
    np.random.seed(24)
    overall_error_values = np.abs(np.random.normal(loc=0.6, scale=0.8, size=len(timestamp)))
    overall_error_values = np.clip(overall_error_values, 0, 3)

    # Anomali noktalarını belirleme
    anomaly_indices = np.random.choice(len(timestamp), size=5, replace=False)
    anomalies = [(timestamp[i], timestamp[i + 1]) for i in anomaly_indices]

    # DataFrame oluşturma
    overall_data = pd.DataFrame({'Zaman Damgası': timestamp, 'Hata': overall_error_values})

    # Grafik oluşturma
    fig_overall = go.Figure()

    # Hata çizgisini ekleme
    fig_overall.add_trace(go.Scatter(x=overall_data['Zaman Damgası'], y=overall_data['Hata'],
                                     mode='lines',
                                     name='hata',
                                     line=dict(color='blue')))

    # Anomalileri ekleme
    shapes = []
    anomaly_lines = []
    for start, end in anomalies:
        shapes.append(
            {
                'type': 'rect',
                'xref': 'x',
                'yref': 'paper',
                'x0': start,
                'y0': 0,
                'x1': end,
                'y1': 1,
                'fillcolor': 'red',
                'opacity': 1.0,
                'layer': 'below',
                'line_width': 0,
            }
        )
        anomaly_lines.append(go.Scatter(x=[start, end], y=[1.5, 1.5],
                                        mode='lines',
                                        line=dict(color='red', width=5),
                                        name='anomali'))

    for line in anomaly_lines:
        fig_overall.add_trace(line)

    fig_overall.update_layout(
        shapes=shapes,
        title="Genel Titreşim Anomalileri Zaman İçinde",
        xaxis_title="Zaman Damgası",
        yaxis_title="Hata",
        yaxis=dict(range=[0, 3])
    )

    st.plotly_chart(fig_overall)

with tab3:
    st.header("Aksiyel Anomali", anchor=False)
    timestamp = pd.date_range(start='2024-07-10', end='2024-09-01', freq='12H')
    np.random.seed(42)
    error_values = np.abs(np.random.normal(loc=0.5, scale=0.4, size=len(timestamp)))
    error_values = np.clip(error_values, 0, 1.5)

    # Peek noktaları belirleme
    peek_indices = [10, 20, 30, 40]
    error_values[peek_indices] = 1.5

    anomaly_indices = np.random.choice(len(timestamp), size=4, replace=False)
    anomalies = [(timestamp[i], timestamp[i + 1]) for i in anomaly_indices]

    data = pd.DataFrame({'Zaman Damgası': timestamp, 'Hata': error_values})

    shapes = []
    anomaly_lines = []

    for start, end in anomalies:
        shapes.append(
            {
                'type': 'rect',
                'xref': 'x',
                'yref': 'paper',
                'x0': start,
                'y0': 0,
                'x1': end,
                'y1': 1,
                'fillcolor': 'red',
                'opacity': 0.8,
                'layer': 'below',
                'line_width': 0,
            }
        )
        anomaly_lines.append(go.Scatter(x=[start, end], y=[1.5, 1.5],
                                        mode='lines',
                                        line=dict(color='red', width=10),
                                        name='anomali'))

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data['Zaman Damgası'], y=data['Hata'],
                             mode='lines',
                             name='hata',
                             line=dict(color='blue', width=2)))

    for line in anomaly_lines:
        fig.add_trace(line)

    fig.update_layout(
        shapes=shapes,
        title="Titreşim (Aksiyel) Anomalileri Zaman İçinde",
        xaxis_title="Zaman Damgası",
        yaxis_title="Hata",
        yaxis=dict(range=[0, 1.5])
    )

    st.plotly_chart(fig)

with tab4:
    st.header("Radyal Anomali", anchor=False)
    timestamp = pd.date_range(start='2024-07-10', end='2024-09-01', freq='12H')
    np.random.seed(42)
    radial_error_values = np.abs(np.random.normal(loc=0.5, scale=0.7, size=len(timestamp)))
    radial_error_values = np.clip(radial_error_values, 0, 2.5)

    anomaly_indices = np.random.choice(len(timestamp), size=3, replace=False)
    anomalies = [(timestamp[i], timestamp[i + 1]) for i in anomaly_indices if i + 1 < len(timestamp)]

    radial_data = pd.DataFrame({'Zaman Damgası': timestamp, 'Hata': radial_error_values})

    shapes = []
    anomaly_lines = []
    for start, end in anomalies:
        shapes.append(
            {
                'type': 'rect',
                'xref': 'x',
                'yref': 'paper',
                'x0': start,
                'y0': 0,
                'x1': end,
                'y1': 1,
                'fillcolor': 'red',
                'opacity': 1.0,
                'layer': 'below',
                'line_width': 0,
            }
        )
        anomaly_lines.append(go.Scatter(x=[start, end], y=[2.5, 2.5],
                                        mode='lines',
                                        line=dict(color='red', width=7),
                                        name='anomali'))

    fig_radial = go.Figure()

    fig_radial.add_trace(go.Scatter(x=radial_data['Zaman Damgası'], y=radial_data['Hata'],
                                    mode='lines',
                                    name='hata',
                                    line=dict(color='blue')))

    for line in anomaly_lines:
        fig_radial.add_trace(line)

    fig_radial.update_layout(
        shapes=shapes,
        title="Titreşim (Radyal) Anomalileri Zaman İçinde",
        xaxis_title="Zaman Damgası",
        yaxis_title="Hata",
        yaxis=dict(range=[0, 2.5])
    )

    st.plotly_chart(fig_radial)

with tab5:
    st.header("Tanjantiyel Anomali", anchor=False)
    timestamp = pd.date_range(start='2024-07-10', end='2024-09-01', freq='12H')
    np.random.seed(24)
    tangential_error_values = np.abs(np.random.normal(loc=0.6, scale=0.9, size=len(timestamp)))
    tangential_error_values = np.clip(tangential_error_values, 0, 3)

    anomaly_indices = np.random.choice(len(timestamp), size=4, replace=False)
    anomalies = [(timestamp[i], timestamp[i + 1]) for i in anomaly_indices if i + 1 < len(timestamp)]

    tangential_data = pd.DataFrame({'Zaman Damgası': timestamp, 'Hata': tangential_error_values})

    shapes = []
    anomaly_lines = []
    for start, end in anomalies:
        shapes.append(
            {
                'type': 'rect',
                'xref': 'x',
                'yref': 'paper',
                'x0': start,
                'y0': 0,
                'x1': end,
                'y1': 1,
                'fillcolor': 'red',
                'opacity': 1.0,
                'layer': 'below',
                'line_width': 0,
            }
        )
        anomaly_lines.append(go.Scatter(x=[start, end], y=[3, 3],
                                        mode='lines',
                                        line=dict(color='red', width=7),
                                        name='anomali'))

    fig_tangential = go.Figure()

    fig_tangential.add_trace(go.Scatter(x=tangential_data['Zaman Damgası'], y=tangential_data['Hata'],
                                        mode='lines',
                                        name='hata',
                                        line=dict(color='blue')))

    for line in anomaly_lines:
        fig_tangential.add_trace(line)

    fig_tangential.update_layout(
        shapes=shapes,
        title="Titreşim (Tanjantiyel) Anomalileri Zaman İçinde",
        xaxis_title="Zaman Damgası",
        yaxis_title="Hata",
        yaxis=dict(range=[0, 3])
    )

    st.plotly_chart(fig_tangential)
