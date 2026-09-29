import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# File paths
MODEL_PATH = PROJECT_ROOT / "Week5" / "models" / "regression_model.pkl"
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "weather_features.csv"
BACKTEST_PATH = PROJECT_ROOT / "Week6" / "results" / "backtest_results.csv"


# Load model and dataset
model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

df["date"] = pd.to_datetime(df["date"])


# Features used by the trained model
features = [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
    "temperature_mean",
    "humidity_mean",
    "pressure_mean",
    "wind_speed_mean",
    "precipitation_hourly_sum",
    "temperature_lag_1",
    "temperature_lag_3",
    "temperature_lag_7",
    "temperature_rolling_3",
    "temperature_rolling_7",
    "humidity_rolling_3",
    "pressure_rolling_3",
    "day_of_week",
    "month"
]


# Page configuration
st.set_page_config(
    page_title="Weather Prediction Tool",
    page_icon="🌤️",
    layout="centered"
)


# Title
st.title("Weather Prediction Tool")
st.write("Predict next-day maximum temperature for Hyderabad.")


# Date selection
selected_date = st.date_input(
    "Select a date",
    value=df["date"].max().date(),
    min_value=df["date"].min().date(),
    max_value=df["date"].max().date()
)

selected_date = pd.Timestamp(selected_date)


# Find selected date
selected_row = df[df["date"] == selected_date]


if selected_row.empty:
    st.warning("No weather data is available for the selected date.")

else:
    input_data = selected_row[features]

    prediction = model.predict(input_data)[0]

    # Prediction
    st.subheader("Prediction")

    st.metric(
        "Next-Day Maximum Temperature",
        f"{prediction:.2f} °C"
    )

    # Prediction comparison
    actual_value = selected_row["target_next_day_max_temp"].iloc[0]

    error = abs(prediction - actual_value)

    st.subheader("Prediction Comparison")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Predicted",
        f"{prediction:.2f} °C"
    )

    col2.metric(
        "Actual",
        f"{actual_value:.2f} °C"
    )

    col3.metric(
        "Absolute Error",
        f"{error:.2f} °C"
    )

    # Weather information used
    st.subheader("Weather Information Used")

    display_columns = [
        "temperature_2m_max",
        "temperature_2m_min",
        "temperature_mean",
        "humidity_mean",
        "pressure_mean",
        "wind_speed_mean",
        "precipitation_sum"
    ]

    st.dataframe(
        selected_row[display_columns].T.rename(
            columns={selected_row.index[0]: "Value"}
        )
    )

    # Model information
    st.subheader("Model Information")

    st.write("Model: Linear Regression")
    st.write("Target: Next-day maximum temperature")
    st.write("Location: Hyderabad")


# Load Week 6 backtest results
backtest_df = pd.read_csv(BACKTEST_PATH)

# Historical model performance
st.subheader("Historical Model Performance")

st.write("Linear Regression Backtest")
st.write("MAE: 0.889 °C")
st.write("RMSE: 1.228 °C")


# Historical backtest chart
st.subheader("Historical Backtest")

chart_data = backtest_df[
    [
        "date",
        "actual",
        "predicted_regression"
    ]
].copy()

chart_data["date"] = pd.to_datetime(chart_data["date"])

chart_data = chart_data.set_index("date")

st.line_chart(chart_data)