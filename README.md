# 🍃💚 Air Quality Forecasting

This project walks through a complete machine learning pipeline for forecasting nitrogen dioxide (NO₂) levels using time series data. It covers the entire process, from cleaning and preparing the data to training, evaluating, and generating predictions. The core model is an LSTM (Long Short-Term Memory) network that learns from historical NO₂ values to produce accurate short-term forecasts. These predictions can support air quality monitoring and help inform public health decisions.

📌 Originally built for a technical screening and later adapted into a portfolio project.

## 🎯 Goal

The objective of this project is to build a reliable LSTM model that forecasts nitrogen dioxide (NO₂) concentrations based only on historical values. One of the main requirements was that the time series data should be non-seasonal, and no external variables could be used for prediction. The focus throughout the project is on thoughtful data cleaning, careful exploration of patterns, and solid model training. The end result is a forecasting model that helps track air quality trends and can contribute to better decision-making in pollution control and public health.

## 🌍 Real-World Relevance

Reliable NO₂ forecasts help cities manage public health risks, optimize traffic flow, and support environmental planning. This type of model can also benefit factories and industrial areas by helping them monitor emissions, stay within regulatory limits, and adjust operations proactively. Since the model runs only on historical data, it offers a fast and lightweight solution for real-time air quality monitoring across different sectors.

## 🗃️ Repository Structure

```plaintext
Air-quality-forecasting/
│
├── data/                               # Dataset
│   ├── raw/                            # Raw data
│   └── processed/                      # Processed data
│
├── figures/                            # Visualizations
│   ├── correlation-matrix.png        
│   └── lstm-residual-distribution.png  
│
├── models/                             # Trained models
│   └── LSTM-model-air-quality.keras    # Saved LSTM model in Keras format
│
├── notebooks/                          # Jupyter Notebooks
│   ├── setup_path.py                   # Path setup
│   └── air-quality-forecasting.ipynb   # End-to-end project notebook
│
├── results/                            # Model output
│   └── metrics                         # Model metrics
│       └── lstm_evaluation_metrics.txt
│   └── predictions                     # Model predictions
│       └── forecasted-no2-values.txt
│
├── src/                                # Config files
│   └── config.py                       
│
├── requirements.txt                    # Required dependencies
└── README.md                           # Project documentation
```

## 📘 Project Overview

- **Introduction** – This project uses LSTM to forecast NO₂ concentration levels, aiming to provide insights for pollution control and public health.
- **Dataset** – Hourly air quality data with NO₂ and other environmental variables from the UCI Machine Learning Repository.
- **Data Cleaning** – Handled missing values, removed redundant features, and deseasonalized the time series for modeling.
- **Exploratory Data Analysis** – Investigated feature distributions and correlations to understand key patterns in air quality data.
- **Feature Engineering** – Created lag-based features and selected important variables based on correlation analysis.
- **Preprocessing** – Normalized and deseasonalized data to ensure stationarity for LSTM modeling.
- **Modeling** – Built and trained an LSTM model to capture temporal dependencies in the NO₂ time series.
- **LSTM Optimization** – Tuned hyperparameters and applied early stopping to prevent overfitting.
- **Forecasting** – Generated 100-step predictions of NO₂ concentration with the trained LSTM model.
- **Conclusions** – The model demonstrated strong forecasting accuracy, providing actionable insights for air quality management.

## ⚙️ Dependencies

Install all the required libraries to carry out this project using:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/herrerovir/Air-quality-forecasting.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Air-quality-forecasting
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Open the Jupyter Notebook to run the project:

   ```bash
   jupyter notebook
   ```

5. Follow the steps in the notebook to load the dataset, preprocess it, train the model, and make predictions.

## 💾 Dataset

The dataset comes from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/360/air+quality). It contains 9471 hourly observations of 16 air quality variables. For this project, the target variable is NO₂ concentration, and only this variable was used to ensure the forecasts rely solely on historical internal data.

Key details:

- Frequency: Hourly observations
- Total entries: 9471
- Target variable: NO₂ concentration
- Time span: Several months of continuous data

## 🌱 Seasonality Check

The project required the time series data to be non-seasonal, meaning it should not have repeating patterns over time. To check this, seasonal decomposition was performed using the additive method, which breaks the series into three parts: trend, seasonal, and residual.

This analysis showed clear daily (24-hour) and weekly (168-hour) seasonal patterns in the NO₂ levels, meaning air quality changes regularly within these periods.

Although the Augmented Dickey-Fuller (ADF) test suggested the data was stationary, the decomposition confirmed the presence of seasonality. To address this, the seasonal components were removed to focus on the underlying trends.

The ADF test was then applied again to the adjusted data to ensure stationarity. This step helped make sure the LSTM model could effectively learn the trends without being affected by seasonal fluctuations.

## 🤖 Modeling and Evaluation

The model is a univariate LSTM built using Keras. It takes overlapping sliding windows of past NO₂ values as input, with each window used to predict the next NO₂ measurement. The architecture consists of a single LSTM layer followed by a dense output layer. Training included early stopping to prevent overfitting, and evaluation was done on a separate test set.

Below is a summary of the model’s evaluation metrics:

| Metric        | Value  |
| ------------- | ------ |
| R² Score      | 0.77   |
| MAE (µg/m³)   | 14.46  |
| RMSE (µg/m³)  | 377.88 |

The residuals showed no consistent pattern, confirming that the model errors are random and unbiased.

## 🔮 Forecasting

After training, the LSTM model was used to generate a 100-step recursive forecast. The predictions showed a smooth downward trend, starting at 142.7 µg/m³ and gradually decreasing to around 124 µg/m³. This pattern aligns with expected air quality improvements and demonstrates the model’s ability to capture underlying trends without overfitting.

All forecasts were made using only the model’s previous predictions as input, simulating a real-world scenario where future values must be predicted step by step without access to actual future measurements.

## 📈 Results

The model delivered solid performance, explaining 77% of the variance in future NO₂ values. It generalized well, with residuals evenly distributed and no signs of drift or instability during multi-step forecasting.

There are some trade-offs to consider:

**Pros:**

- Does not rely on any external data
- Fast inference with low delay
- Simple and interpretable architecture
- Strong performance for short-term forecasting

**Cons:**

- Accuracy may decline over longer forecast horizons
- Without external inputs, the model is less flexible
- Recursive forecasting can lead to gradual error accumulation

Overall, this approach works well for short-term NO₂ predictions and situations where simplicity and independence from outside data sources are important.

## 🧭 Future Work

There are several ways this project could be improved or expanded:

- **Multivariate Modeling**: Including other air quality variables or external factors like temperature, humidity, and time-of-day could enhance prediction accuracy.
- **Alternative Architectures**: Trying different models such as GRUs, Temporal Convolutional Networks, or attention-based methods might capture patterns more effectively.
- **Hyperparameter Tuning**: Employing tools like Optuna or Keras Tuner could help find the best model settings through more thorough optimization.
- **Uncertainty Estimation**: Adding prediction intervals or Bayesian techniques would provide insights into the confidence of forecasts.
- **Deployment**: Turning the project into a web app or interactive dashboard could enable real-time use and wider accessibility.
