# Electricity-Anomaly-Detection
An unsupervised machine learning project using Python and Isolation Forest to detect unusual electricity consumption patterns. The project explores data cleaning, feature engineering, anomaly detection and experimental analysis using real household electricity usage data.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Git/GitHub

- ## Dataset

The project uses the UCI Individual Household Electric Power Consumption dataset.

The dataset contains measurements of household electricity consumption recorded at one-minute intervals over several years.

The original dataset is not included in this repository because of its large file size. It can be downloaded from the UCI Machine Learning Repository.

## Methodology

The project follows these main steps:

1. Load and inspect the raw electricity consumption data.
2. Clean missing and invalid values.
3. Convert the measurements into hourly averages.
4. Create features describing time and recent consumption behaviour.
5. Train an Isolation Forest anomaly detection model.
6. Identify unusual electricity consumption periods.
7. Analyse detected anomalies by time and day of the week.
8. Investigate how the model's contamination parameter affects anomaly detection.


## Features

The model uses:

- Global active power
- Hour of day
- Day of week
- 24-hour rolling mean
- 24-hour rolling standard deviation

  ## Results

Using an Isolation Forest model with a contamination value of 0.02, the model identified 683 anomalous observations from 34,145 hourly observations.

The detected anomalies included both unusually high and unusually low electricity consumption.

The analysis also showed variation in detected anomaly rates across the week, with Sunday having the highest detected anomaly rate and Thursday the lowest.
