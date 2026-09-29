# Weather Prediction Tool

This project is part of my AI/ML internship.

The goal is to build a weather prediction tool for Hyderabad using historical weather data.

## Week 4

- Used the Open-Meteo Historical Weather API
- Collected historical weather data for Hyderabad
- Retrieved hourly and daily weather data
- Stored raw weather data as CSV files
- Created daily weather features
- Created temperature lag features
- Created rolling average features
- Added date-based features
- Created the next-day maximum temperature target

## Week 5

This week focused on training weather prediction models.

### Work Done

- Used the processed dataset created in Week 4
- Prepared features and target for prediction
- Used a chronological train-test split
- Trained a Linear Regression model
- Trained an ARIMA model
- Generated predictions from both models
- Evaluated the models using MAE, MSE, RMSE and R2
- Compared the initial results of both models
- Saved the trained models for future use

### Models Used

- Linear Regression
- ARIMA(1,1,1)

### Dataset

The models use the engineered weather dataset created from Open-Meteo historical weather data.

### Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Statsmodels
- Matplotlib
- Joblib
- Jupyter Notebook
- Open-Meteo API

## Next Step

The next stage will focus on time-series evaluation, backtesting and comparing model predictions with actual weather data.

## Week 6

This week focused on evaluating the weather prediction models using time-series backtesting.

### Work Done
- Loaded the processed weather dataset
- Used the Linear Regression model from Week 5
- Used ARIMA for time-series forecasting
- Performed walk-forward backtesting
- Generated predictions for historical dates
- Compared predictions with actual weather values
- Calculated MAE, MSE and RMSE
- Analyzed prediction errors
- Saved backtesting results as CSV

### Evaluation
The models were evaluated using historical data while maintaining chronological order to avoid future data leakage.

### Output
Backtesting results are stored in:

`Week6/results/backtest_results.csv`

## Week 7

This week focused on evaluating historical weather forecasts against actual historical weather data.

### Work Done
- Retrieved archived forecast data using the Open-Meteo Previous Model Runs API
- Evaluated 1-day, 3-day and 7-day forecast lead times
- Used historical weather data as the reference dataset
- Converted hourly forecast values into daily maximum temperature forecasts
- Compared forecasts with actual maximum temperatures
- Calculated MAE, MSE and RMSE
- Analyzed forecast errors
- Visualized forecast performance
- Saved forecast evaluation results

### Output
Forecast evaluation results are stored in:

`Week7/results/forecast_evaluation.csv`

## Week 8

This week focused on deploying the trained weather prediction model as a Streamlit application.

### Work Done
- Loaded the trained Linear Regression model
- Connected the model with the processed weather dataset
- Created a Streamlit application
- Added date-based prediction
- Displayed next-day maximum temperature
- Displayed weather information used for prediction
- Added model performance information
- Added historical backtest visualization

### Application
The Streamlit application is located at:

`Week8/app/app.py`

### Model
The application uses the trained Linear Regression model from Week 5.

### Next Step
The project can be extended into a full web-based weather prediction system with live weather inputs, prediction reliability, forecast comparison and a more advanced user interface.