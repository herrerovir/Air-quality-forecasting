# Seasonality

El requerimiento de este ejercicio es que la serie temporal sea **no-estacional**. La estacionalidad se refiere a las fluctuaciones periódicas de un conjunto de datos. Estos intervalos regulares se producen debido a factores estacionales. Para determinar si la serie temporal es no-estacional, primero hay que comprobar si la serie es **estacionaria**. Para ello se emplea la prueba estadística de Dickey-Fuller la cual consiste en detectar la presencia de una raíz unitaria la cual indica no estacionariedad. Si el resultado de la prueba es significativo, sugiere que la serie es estacionaria, y por tanto, no presenta estacionalidad.

```python
def check_seasonality(series):
    """
    Perform the Dickey-Fuller test to check for seasonality and print the results.

    Parameters
    ----------
    series : Pandas Series
        The time series data to test for seasonality.
    
    Returns
    -------
    None
    """
    result = adfuller(series)
    adf_statistic = result[0]
    p_value = result[1]
    critical_values = result[4]
    
    # Print the results
    print("Dickey-Fuller Test Results:\n")
    print(f"ADF Statistic: {adf_statistic}")
    print(f"p-value: {p_value}")

    for key, value in critical_values.items():
        print(f"Critical Value {key}: {value}")
    
    # Interpretation
    interpretation = ("The time series is stationary, indicating the absence of seasonality."
                      if p_value < 0.05 else
                      "The time series is non-stationary, suggesting it may  seasonality.")
    print(f"\nInterpretation: {interpretation}")

```

```python
# Check seasonality on target variable
adf_result = check_seasonality(air_quality["NO2_Concentration"])
```

Los resultados de la prueba de Dickey-Fuller indican que la serie temporal es **no estacional**.

- **Estacionariedad**: La estadística ADF es menor que los valores críticos y el valor p es muy bajo. Esto significa que la serie es estacionaria, lo que sugiere que no tiene tendencias ni fluctuaciones que cambien con el tiempo.

- **No Estacionalidad**: La falta de estacionalidad significa que no hay patrones repetidos en intervalos regulares. Esto implica que la serie no muestra variaciones predecibles según la época del año o del mes.

Por estas razones, podemos afirmar que la serie temporal es no estacional y estacionaria.

```python
# Plot the NO2 concentration over time
plt.figure(figsize = (11, 4))
plt.plot(air_quality["NO2_Concentration"], color = "#e7298a")
plt.xlabel("Fecha")
plt.ylabel("Concentración de NO$_2$")
plt.title("Concentración de NO$_2$ a lo largo del tiempo")
```

```python
# Perform seasonal decomposition of the NO2 concentration data
result = seasonal_decompose(air_quality["NO2_Concentration"], model = "additive", period = 365)

# Plot the decomposition results
plt.figure(figsize = (14, 10))
result.plot()
plt.suptitle("Descomposición Estacional de la Concentración de NO$_2$")

# Change the color of the lines in the plot and set axis labels
for ax in plt.gcf().axes:
    for line in ax.lines:
        line.set_color("#e7298a")
    ax.set_xlabel("Tiempo")

plt.tight_layout()
```

Los resultados de la descomposición estacional muestran los componentes de la serie temporal para comprender mejor la dinámica de la concentración de NO<sub>2</sub> a lo largo del tiempo:

1. **Observado**: datos originales de las concentraciones de NO<sub>2</sub>
2. **Tendencia**: tendencia general a largo plazo de las concentraciones de NO<sub>2</sub>
3. **Estacional**: patrones repetitivos en intervalos regulares de las concentraciones de NO<sub>2</sub>
4. **Residual**: fluctuaciones aleatorias no explicadas por la tendencia o estacionalidad