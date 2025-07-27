import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="📊 Python Progress Tracker", layout="wide")

st.title("📚 Python Progress Tracker – Live & Auto-Updating!")

# Link to your published Google Sheet CSV
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQi4i8DMkPTAd7vgcTzuDARVBs2FondMVIPpL4NEp5ZTV6iwnREWZEgBptnr87LFLJ5X8rM651d5oCC/pub?output=csv"

# Load data
df = pd.read_csv(csv_url)

# Clean: Drop rows with missing score
df = df.dropna(subset=["🔢 Numeric Score"])

# Plotting
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df["📅 Date"],
    y=df["🔢 Numeric Score"],
    mode='lines+markers',
    line=dict(color='mediumvioletred', width=3),
    marker=dict(size=8),
    name="Python Score"
))

fig.update_layout(
    title="📈 Python Class Score Trend",
    xaxis_title="Class Date",
    yaxis_title="Score out of 10",
    yaxis=dict(range=[0, 10]),
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)
