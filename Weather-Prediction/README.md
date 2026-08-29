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