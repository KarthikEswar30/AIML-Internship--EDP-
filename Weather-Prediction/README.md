# Weather Prediction Tool

Week 4 of my AI/ML internship project.

The goal of this project is to build a weather prediction tool for Hyderabad.

## Week 4

This week focused on collecting historical weather data and creating useful time-series features.

## Work Done

- Used the Open-Meteo Historical Weather API
- Collected historical weather data for Hyderabad
- Retrieved hourly and daily weather data
- Stored raw weather data in CSV files
- Checked data types and missing values
- Aggregated hourly data into daily features
- Created lag features for temperature
- Created rolling average features
- Added day of week and month features
- Created the next-day maximum temperature target
- Saved the final feature dataset for future model training

## Features

- Temperature
- Humidity
- Pressure
- Wind speed
- Precipitation
- Weather code
- Temperature lag features
- Rolling averages
- Calendar features

## Tools Used

- Python
- Pandas
- NumPy
- Requests
- Jupyter Notebook
- Open-Meteo API

## Dataset

The weather data was collected directly from the Open-Meteo Historical Weather API.

## Next Step

The processed dataset will be used in Week 5 for Regression and ARIMA model training.