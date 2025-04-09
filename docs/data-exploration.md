# Exploratory Data Analysis
## **Target Variable**
La variable objetivo de este proyecto es la concentración de NO<sub>2</sub>. He elegido esta variable por las siguientes razones:

- De entre todos los contaminantes del dataset, NO<sub>2</sub> es uno de los más perjudiciales para la salud.
- Los efectos de NO<sub>2</sub> sobre la salud están bien documentados.
- La regulación establece valores máximos y claros para este gas.
air_quality.columns

- **Concentraciones mensuales de NO<sub>2</sub>**

```python
# Resample and plot the monthly mean of NO2 concentration levels
monthly_no2 = air_quality["NO2_Concentration"].resample("ME").mean()

ax = monthly_no2.plot(kind = "bar", figsize = (11, 4), color = "#e7298a")
plt.xlabel("Mes")
plt.ylabel("Concentración promedio de NO$_2$")
ax.set_xticks(range(len(monthly_no2)))
ax.set_xticklabels(monthly_no2.index.strftime("%B, %Y"))
plt.title("Concentraciones promedio mensuales de NO$_2$");  
```

Las concentraciones de NO<sub>2</sub> entre marzo de 2004 y abril de 2005 muestran que las concentraciones de este gas aumentan durante los meses de invierno y durante el verano decrecen hasta llegar al mínimo en agosto. Esto probablemente es debido al uso de calefacciónes en las casas y comercios, el transporte y mayor uso de electricidad. variaron. También se observa que existe una tendencia general al alza en los niveles de NO<sub>2</sub>.

- **Concentraciones de NO<sub>2</sub> por hora**

```python
# Resample the data to get hourly mean values
hourly_no2 = air_quality["NO2_Concentration"].resample("h").mean()

# Create a bar plot
plt.figure(figsize=(14, 6))
sns.barplot(x=hourly_no2.index.hour, y=hourly_no2.values, errorbar = None, color = "#e7298a")
plt.xlabel("Hora del día")
plt.ylabel("Concentración promedio de NO$_2$")
plt.title("Concentración promedio por hora de NO$_2$")
plt.xticks(range(24), [f"{h}:00" for h in range(24)]);
```

Los niveles de NO<sub>2</sub> fluctúan durante el día de manera significativa, oscilando entre 92.0 y 190.0 ppb. Las concentraciones comienzan en 113.0 ppb a medianoche y aumentan a lo largo de la tarde, alcanzando un pico de 122.0 ppb alrededor de las 21:00. Los niveles son más bajos durante la noche, probablemente debido a un menor uso del transporte, electricidad, etc.

## **Features**

```python
# Drop unnecessary columns and resample the data by month, calculating the mean
monthly_mean = air_quality.drop(["Temperature", "Relative_Humidity", "Absolute_Humidity"], axis=1).resample("ME").mean()
# Plot monthy average values of all the gases
colors = ["black", "blue", "deepskyblue", "lightseagreen", "limegreen", "gold", "darkorange", "chocolate", "deeppink"]

monthly_mean.plot(figsize=(15, 8), color=colors)
plt.xlabel("Mes")
plt.ylabel("Concentración promedio de gases tóxicos")
plt.title("Concentración mensual promedio de gases tóxicos")
plt.legend(loc="upper right")
plt.tight_layout()
```

Los gráfica que representa las concentraciones mensuales promedios de los gases en el aire, muestra que éstas fluctuan significativamente a lo largo del tiempo. La única que se mantiene bastante estable es la concentración de CO se mantiene bastante estable. Por otro lado, el benceno muestra más variabilidad. Las concentraciones de NO<sub>x</sub> y NO<sub>2</sub> son mucho más altas durante el otoño e invierno, lo que probablemente sea debido al aumento en el uso de calefacción y tráfico.

## **Matriz de Correlación**

```python
correlations = air_quality.corr(numeric_only = True)
correlations
correlation_heatmap_graph = plt.figure(figsize = (11, 4))
sns.heatmap(correlations, linewidths = 0.5, annot = True, cmap = "PuRd")
plt.title("Correlation Heatmap", size = 12)
```

La matriz de correlación muestra las relaciones entre las diferentes variables, cuánto más fuerte es el color, más relación hay entre las variables. Las relaciones más importantes entre los parámetros de calidad del aire son los siguientes:

1. **Correlaciones Fuertes**:
   - La concentración de CO se relaciona estrechamente con su sensor y con la concentración de C6H<sub>6</sub>.
   - Las respuestas de los sensores de C6H<sub>6</sub> y NMHC perfectamente correlacionadas.

2. **Compuestos de Nitrógeno**:
   - NOx y NO<sub>2</sub> tienen una fuerte correlación positiva, lo que significa que cuando uno aumenta, el otro también aumenta.
   - La respuesta del sensor de NOx se correlaciona negativamente con su concentración. Esto puede indicar que el sensor no funciona correctamente.

3. **Temperatura y Humedad**:
   - La temperatura tiene una leve correlación positiva con el sensor de NO<sub>2</sub> y negativa con CO.
   - La humedad absoluta se correlaciona más fuerte con la temperatura y el sensor de NO<sub>2</sub>.