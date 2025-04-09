# Test 2: Time Series Regression

## Air Quality Forecasting

**Author:** Virginia Herrero [Email](mailto:v.herrero@outlook.com) | [LinkedIn](https://www.linkedin.com/in/virginia-herrero-casero/) | [GitHub](https://github.com/herrerovir)

### Introducción

En este proyecto, se lleva a cabo un proceso de machine learning de principio a fin, con el objetivo de predecir la calidad del aire usando datos de series temporales. Este cuaderno detalla paso a paso todas las decisiones tomadas desde la limpieza de los datos hasta el desarrollo y evaluación del modelo.

Elegí este conjunto de datos porque es relevante para mi formación como ingeniero químico especializada en control de calidad. Predecir la calidad del aire es una gran oportunidad para mostrar mis habilidades en ingeniería aplicada a la ciencia de datos, especialmente en el ámbito del control de calidad para diferentes industrias.

### Dataset

El conjunto de datos utilizado en este proyecto se obtuvo del UCI Machine Learning Repository [here](https://archive.ics.uci.edu/dataset/360/air+quality).

La información proporcionada del conjunto de datos es la siguiente:

- The dataset contains 9358 instances of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality Chemical Multisensor Device. The device was located on the field in a significantly polluted area, at road level, within an Italian city. 

- Data were recorded from March 2004 to February 2005 (one year) representing the longest freely available recordings of on field deployed air quality chemical sensor devices responses. 

- Ground Truth hourly averaged concentrations for CO, Non Metanic Hydrocarbons, Benzene, Total Nitrogen Oxides (NOx) and Nitrogen Dioxide (NO2) and were provided by a co-located reference certified analyzer.

- Missing values are tagged with -200 value.

Las variables de este conjunto de datos son las siguientes:

- `Date`: (DD/MM/YYYY)

- `Time`: (HH.MM.SS)

- `CO(GT)`: True hourly averaged concentration CO in mg/m^3 (reference analyzer)

- `PT08.S1(CO)`: (tin oxide) hourly averaged sensor response (nominally CO targeted)

- `NMHC(GT)`: True hourly averaged overall Non Metanic HydroCarbons concentration in microg/m^3 (reference analyzer)

- `C6H6(GT)`: True hourly averaged Benzene concentration  in microg/m^3 (reference analyzer)

- `PT08.S2(NMHC)`: (titania) hourly averaged sensor response (nominally NMHC targeted)

- `NOx(GT)`: True hourly averaged NOx concentration  in ppb (reference analyzer)

- `PT08.S3(NOx)`: (tungsten oxide) hourly averaged sensor response (nominally NOx targeted)

- `NO2(GT)`: True hourly averaged NO2 concentration in microg/m^3 (reference analyzer)

- `PT08.S4(NO2)`: (tungsten oxide) hourly averaged sensor response (nominally NO2 targeted)

- `PT08.S5(O3)`: (indium oxide) hourly averaged sensor response (nominally O3 targeted)

- `T`: Temperature in °C

- `RH`: Relative Humidity (%)

- `AH`: Absolute Humidity

### Data loading

Carga el archivo CSV **AirQualityUCI** como un DataFrame de pandas.

```python
# Import all required libraries
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# Seasonal analysis
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose

# Modeling and evaluation
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

```python
# Load the dataset
df = pd.read_csv("../data/raw/AirQualityUCI.csv", delimiter = ";", decimal = ",")
df.head()
```