# Forecasting

Otro de los requisitos de este ejercico es predecir 100 ciclos en el futuro sin utilizar las variables regresoras. Para ello se prepara la última entrada del dataset para que sea compatible con el modelo LSTM. Luego, se itera 100 veces para predecir los siguientes valores, agregando cada nuevo valor pronosticado a una lista que los guarda todos. Finalmente, se imprimen en la consola las predicciones para los próximos 100 pasos de tiempo.

```python
# Number of time steps to forecast
num_forecasts = 100

# Reshape input to fit LSTM
last_input = data[-time_step:].reshape(1, time_step, 1)

# List to store the forecasted values
forecasted_values = []

# Iterate to predict the next value
for _ in range(num_forecasts):
    next_value = model.predict(last_input) 
    forecasted_values.append(next_value[0, 0])
    last_input = np.concatenate((last_input[:, 1:, :], next_value.reshape(1, 1, 1)), axis=1)

# Convert the forecasted values to a numpy array
forecasted_values = np.array(forecasted_values)

# Print the forecasted values
print(f"Forecasted values for the next 100 time steps:\n {forecasted_values}")
```
