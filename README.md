# 🍃💚 Air Quality Forecasting

This project walks through a full machine learning workflow to forecast NO₂ levels in air quality using time series data. It covers everything from data cleaning and preprocessing to model selection, evaluation, and predictions. The final model, an LSTM (Long Short-Term Memory), accurately forecasts future NO₂ concentrations, providing valuable insights for pollution control and public health planning.

📌 Originally built for a technical screening and later adapted into a portfolio project..

## 🎯 Goal

Build a robust LSTM model to forecast NO₂ concentrations, helping to predict air quality trends. The two requirements for this project were: series must be non-seasonal, and the predictions must rely solely on historical data, with no external variables. The project emphasizes data cleaning, feature exploration, and model training to deliver reliable predictions that support informed decisions on pollution control and public health.

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
├── scr/                                # Config files
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

This project requires the following Python libraries:

```bash
pip install -r requirements.txt
```
- **Python**
- **Jupyter Notebooks**
- **Pandas**
- **NumPy**
- **TensorFlow**
- **Matplotlib**
- **Seaborn**

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

The dataset used for this project comes from the UCI Machine Learning Repository [here](https://archive.ics.uci.edu/dataset/360/air+quality). It contains 9471 entries and 16 columns, with hourly measurements of various air quality parameters, including NO₂, CO, benzene (C₆H₆), and others. The focus of this project is on forecasting the NO₂ concentration over time.

## 🌱 Seasonality Check

As part of the project requirements, the time series data needed to be non-seasonal, meaning it should not contain any repeating patterns over time. To ensure this, we first performed a **Seasonal Decomposition** using the `additive decomposition` method to separate the time series into three components: **trend**, **seasonal**, and **residual**.

The decomposition revealed strong daily (24-hour) and weekly (168-hour) seasonal patterns in the NO₂ concentrations, indicating that air quality fluctuates regularly within these time frames.

Despite the **Augmented Dickey-Fuller (ADF) test** indicating that the series was stationary, the decomposition highlighted the presence of seasonality. To resolve this, we deseasonalized the data by removing these seasonal components, leaving only the underlying trends for modeling.

After deseasonalizing, the ADF test was re-applied to confirm that the data was stationary, ensuring that the LSTM model could effectively capture the trends without being influenced by seasonal fluctuations.

## 🤖 LSTM Model Evaluation & Results

* The LSTM model achieved a strong R² score of 0.77, showing it explains 77% of the variance in NO₂ concentration. This demonstrates the model's effectiveness in capturing the underlying trends.
* The residuals showed no clear bias or patterns, confirming that the model is well-calibrated and the errors are random.

## 🔮 Forecasting

To forecast future NO₂ concentrations, the trained LSTM model predicted the next 100 time steps based only on the historical data. Although no external features were used, the model generated smooth, realistic predictions. The forecast followed a clear downward trend, with NO₂ concentrations declining from 142.7 µg/m³ to around 124 µg/m³ over the forecast horizon. This aligns with expectations of gradual improvement in air quality.

## 📈 Results

The final LSTM model showed excellent performance in predicting NO₂ concentrations. With an R² score of 0.77 and well-calibrated residuals, the model accurately captured the underlying trends in the data. Forecasts for future air quality demonstrated consistent, realistic behavior, proving the model’s reliability for short-term predictions. Overall, this model provides actionable insights for pollution control and public health planning.
