import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime


@st.cache_data
def load_data():
    day_data = pd.read_csv("Dashboard/day.csv")
    hour_data = pd.read_csv("Dashboard/hour.csv")
    day_data["dteday"] = pd.to_datetime(day_data["dteday"])
    return day_data, hour_data


day_df, hour_df = load_data()

st.sidebar.header("Pengaturan Data")
data_type = st.sidebar.radio("Pilih Tipe Data", ["Harian", "Jam-jaman"])

st.sidebar.header("Pengaturan Analisis")
variable = st.sidebar.multiselect(
    "Pilih Variabel",
    ["season", "weathersit", "temp", "hum", "windspeed"],
    default=["season"],
)

st.sidebar.header("Filter Data")
if data_type == "Harian":
    min_date = day_df["dteday"].min().to_pydatetime()
    max_date = day_df["dteday"].max().to_pydatetime()
    start_date, end_date = st.sidebar.slider(
        "Rentang Tanggal:",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date),
    )
else:
    start_hour, end_hour = st.sidebar.slider("Rentang Jam:", 0, 23, (0, 23))

st.sidebar.header("Opsi Tambahan")
show_corr = st.sidebar.checkbox("Tampilkan Heatmap Korelasi")
show_stats = st.sidebar.checkbox("Tampilkan Ringkasan Statistik")

data = day_df if data_type == "Harian" else hour_df


def create_plotly_bar_chart(data, x, y, title):
    return px.bar(data, x=x, y=y, title=title)


if data_type == "Harian":
    filtered_data = data[
        (data["dteday"] >= pd.to_datetime(start_date))
        & (data["dteday"] <= pd.to_datetime(end_date))
    ]
else:
    filtered_data = data[(data["hr"] >= start_hour) & (data["hr"] <= end_hour)]


st.title("Dashboard Analisis Penyewaan Sepeda")
st.subheader(f"Data Penyewaan Sepeda - Ringkasan {data_type}")

if show_corr:
    st.subheader("Heatmap Korelasi")
    numeric_data = filtered_data.select_dtypes(include=["float64", "int64"])
    fig, ax = plt.subplots()
    sns.heatmap(numeric_data.corr(), annot=True, ax=ax)
    st.pyplot(fig)


if show_stats:
    st.subheader("Ringkasan Statistik")
    st.write(filtered_data.describe())

for var in variable:
    st.plotly_chart(
        create_plotly_bar_chart(
            filtered_data, var, "cnt", f"Total Penyewaan Sepeda per {var.title()}"
        )
    )
