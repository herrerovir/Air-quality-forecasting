# Data cleaning

Limpia y preprocesa el conjunto de datos antes de seguir con el análisis.

```python
df.info()
```

* **Elimina columnas innecesarias**

Las columnas Unnamed: 15 y Unnamed: 16 están vacías, por lo tanto, se eliminan del conjunto de datos.

```python
df = df.drop(["Unnamed: 15", "Unnamed: 16"], axis = 1)
```

* **Renombra columnas**

Algunas columnas se renombraron para proporcionar un contexto más claro y mejorar la comprensión para una audiencia no técnica del conjunto de datos.

```python
df.columns
df = df.rename(columns = {"CO(GT)" : "CO_Concentration",
                          "PT08.S1(CO)" : "CO_Sensor_Response",
                          "NMHC(GT)" : "NMHC_Concentration",
                          "C6H6(GT)" : "C6H6_Concentration",
                          "PT08.S2(NMHC)" : "NMHC_Sensor_Response",
                          "NOx(GT)" : "NOx_Concentration",
                          "PT08.S3(NOx)" : "NOx_Sensor_Response",
                          "NO2(GT)" : "NO2_Concentration",
                          "PT08.S4(NO2)" : "NO2_Sensor_Response",
                          "PT08.S5(O3)" : "O3_Sensor_Response",
                          "T" : "Temperature",
                          "RH" : "Relative_Humidity",
                          "AH" : "Absolute_Humidity"})
# Show the dataset with the renamed variables
df.head()
```

* **Valores nulos**

Identifica y elimina cualquier valor nulo en el conjunto de datos cuando sea necesario.

```python
# Check the total of null values in each column
df.isna().sum()
```

Hay 114 valores nules en todas las columnas del dataset.

```python
# Show all the rows with missing values
missing_rows = df[df.isna().any(axis = 1)]
missing_rows
```

El conjunto de datos tiene un total de 114 valores faltantes, lo cual es un porcentaje relativamente bajo, aproximadamente el 1.2% de todo el conjunto de datos. Dado este pequeño porcentaje, eliminaré todas las filas con valores nulos. Dado que se trata de una serie temporal, utilizar un método de imputación como el fill forward podría crear valores duplicados, ya que simplemente llevaría hacia adelante la última entrada no NaN disponible. Por lo tanto, eliminar estas filas es el mejor método para mantener la integridad de los datos.
```python
# Drop missing values
df = df.dropna()
````

La descripción del conjunto de datos indica que los valores faltantes están etiquetados con el valor -200. Por lo tanto, se buscarán todos los valores -200 y se reemplazarán por valores NaN.

```python
# Count -200 values in each column
df.apply(lambda x : x == -200).sum()
```

El análisis del conteo de valores -200 muestra claramente que la característica **"NMHC_Concentration"** tiene una cantidad significativa de valores nulos. Por esta razón, esta columna se eliminará directamente del conjunto de datos. Posteriormente, todas las instancias de -200 se reemplazarán por valores NaN y se imputarán siguiendo el método de relleno hacia adelante, el cual es adecuado para las series temporales.

```python
# Drop the colum with too many missing values
df.drop(columns = ["NMHC_Concentration"], inplace = True)
# Replace values with NaN
df.replace(to_replace = -200, value = np.nan, inplace = True)
# Forward fill missing values
df.ffill(inplace = True)
# Check remaining missing values
df.isna().sum()

```

* **Valores duplicados**

Verifica si hay entradas duplicadas en el conjunto de datos.

```python
df.duplicated().sum()
```

El dataset no tiene valores duplicados.

* **Tipos de datos**

Verifica que todas las columnas tengan los tipos de datos apropiados.

```python
df.dtypes
```

Las columnas **"Date"** y **"Time"** están configuradas como tipos objeto, por lo que necesitan ser convertidas al tipo datetime.

```python
# Create new feature with date and time
df["Datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], format = "%d/%m/%Y %H.%M.%S")

# Set the new feature as the index
df = df.set_index("Datetime")

# Drop the unnecesary columns
df = df.drop(["Date", "Time"], axis = 1)
df
# Check again for missing values after transformation
df.isna().sum()
```

* **Outliers**

Examina el resumen estadístico del conjunto de datos para identificar posibles valores atípicos. Esta visión general inicial ayudará a resaltar cualquier valor inusual que pueda requerir una exploración adicional.

```python
df.describe().T`
```

A partir de las estadísticas resumidas del conjunto de datos, es evidente que las siguientes variables muestran discrepancias importantes entre sus valores máximos y el cuartil superior, lo que indica la existencia de posibles valores atípicos.

- CO_Concentration
- C6H6_Concentration
- NOx_Concentration

Primero, se trazarán graficas de estas variables para identificar posibles valores atípicos. Luego, los valores atípicos se identificarán utilizando el método del rango intercuartílico (IQR). El análisis de la distribución de los datos revelará los valores que están fuera del rango típico, lo que permitirá seleccionar un enfoque adecuado para manejarlos.

```python
# Plot the CO concentration distribution using a histogram and boxplot
CO_concentration_distribution = plt.figure()
fig, ax = plt.subplots(1, 2, figsize = (11, 3))
sns.histplot(df["CO_Concentration"], ax = ax[0], color = "#e7298a")
sns.boxplot(x = df["CO_Concentration"], ax = ax[1], color = "#e7298a")
ax[0].set_xlabel("Concentración de CO")
ax[1].set_xlabel("Concentración de CO")
plt.suptitle("Distribución de la concentración de CO", size = 12)
# Plot the C6H6 concentration distribution using a histogram and boxplot
C6H6_concentration_distribution = plt.figure()
fig, ax = plt.subplots(1, 2, figsize = (11, 3))
sns.histplot(df["C6H6_Concentration"], ax = ax[0], color = "#e7298a")
sns.boxplot(x = df["C6H6_Concentration"], ax = ax[1], color = "#e7298a")
ax[0].set_xlabel("Concentración de C$_6$H$_6$")
ax[1].set_xlabel("Concentración de C$_6$H$_6$")
plt.suptitle("Distribución de la concentración de C$_6$H$_6$", size = 12)
# Plot the NOx concentration distribution using a histogram and boxplot
NOx_concentration_distribution = plt.figure()
fig, ax = plt.subplots(1, 2, figsize = (11, 3))
sns.histplot(df["NOx_Concentration"], ax = ax[0], color = "#e7298a")
sns.boxplot(x = df["NOx_Concentration"], ax = ax[1], color = "#e7298a")
ax[0].set_xlabel("Concentración de NO$_x$")
ax[1].set_xlabel("Concentración de NO$_x$")
plt.suptitle("Distribución de la concentración de NO$_x$", size = 12)
```

Encuentra los valores atípicos utilizando el método del rango intercuartílico (IQR).

```python
# Create a function to find outliers using the IQR method

def find_outliers_iqr(dataframe, column):
    """
    Finds outliers in the specified column of a DataFrame using the IQR method

    Parameters
    ----------
    dataframe : Pandas DataFrame
        The DataFrame containing the data
    
    column : str
        The name of the column (as a string) in which to find the outliers

    Returns
    -------
    Pandas DataFrame
        A DataFrame containing the outliers identified in the specified column
   """
    # Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    
    # Calculate IQR
    IQR = Q3 - Q1
    
    # Determine the bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Identify outliers
    outliers = dataframe[(dataframe[column] < lower_bound) | (dataframe[column] > upper_bound)]
    print(f"The number of outliers in the column {column} is {outliers.shape[0]}")
    
    return outliers`

```

```python
# Find outliers in the dataset
for i in df.columns:
    find_outliers_iqr(df, i)

```

A partir del análisis estadístico de los valores atípicos, se puede concluir que hay una gran cantidad de valores fuera de rango. Teniendo en cuenta la naturaleza de las características, los valores atípicos podrían estar presentes debido a picos de contaminación en el aire. Por lo tanto, estos datos podrían ser relevantes. Sin embargo, la presencia de valores atípicos puede afectar el rendimiento del modelo que se utilizarán posteriormente para predecir los 100 ciclos. Por estas razones, he decidido limitar los valores atípicos para conservar todos los datos, pero reducir el posible impacto negativo que puedan tener en el modelo predictivo.

```python
def cap_outliers(dataframe, column):
    """
    Cap outliers in a specified column of the DataFrame using the IQR method

    Parameters
    ----------
    dataframe : Pandas DataFrame
        The DataFrame containing the data
    
    column : str
        The name of the column to cap outliers


    Returns
    -------
    Pandas DataFrame
        A DataFrame with outliers capped
    """
    if column not in dataframe.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    
    # Calculate Q1 and Q3
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)

    # Calculate IQR

    IQR = Q3 - Q1

    # Define bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Cap the outliers
    dataframe[column] = dataframe[column].clip(lower = lower_bound, upper = upper_bound)

    return dataframe
```

```python
# Cap outliers
for i in df.columns:
    cap_outliers(df, i)
```

La distribución de las características después de limitar los outliers es la siguiente: 

```python
df.hist(figsize = (20, 10), color = "#e7298a")
plt.suptitle("Distribución de las características")

```

* **El conjunto de datos limpio:**

```python
air_quality = df.copy()
air_quality.head()
# Save the cleaned dataset
air_quality.to_csv("../data/processed/Air-quality-cleaned-dataset.csv")
```