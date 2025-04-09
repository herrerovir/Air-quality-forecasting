# Pre-processing

- **Eliminación de Columnas**

Se eliminaron las columnas **NMHC_Sensor_Response** y **NOx_Sensor_Response** debido a:

- **NOx_Sensor_Response**: Fuerte correlación negativa con varias características y redundancia con NOx_Concentration.
  
- **NMHC**: Su alta correlación con C6H<sub>6</sub> sugiere que los niveles de ambos están midiendo compuestos similares y supone redundancia de datos.

Eliminando ambas características evitamos posibles problemas de multicolinealidad en el modelo predictivo.

```python
air_quality = air_quality.drop(["NMHC_Sensor_Response", "C6H6_Concentration"], axis=1)
air_quality.head()
```
