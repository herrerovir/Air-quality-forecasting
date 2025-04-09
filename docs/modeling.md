# LSTM Modeling

El objetivo de este ejercicio es desarrollar un modelo que sea capaz de predecir en el futuro la calidad del aire mediante una serie temporal. Por ello, el algoritmo elegido para construir dicho modelo es una red neuronal recurrente (RNN) ya que éstas son ideales para resolver este tipo de problemas. En concreto se construirá un modelo Long-Short-Term-Memory.

```python
# Create function to prepare the data for LSTM model
def create_dataset(data, time_step = 1):
    X, Y = [], []
    for i in range(len(data) - time_step):
        X.append(data[i:(i + time_step)])
        Y.append(data[i + time_step])
    return np.array(X), np.array(Y)

# Normalize the data
data = air_quality["NO2_Concentration"].values
data = (data - np.min(data)) / (np.max(data) - np.min(data))

# Set the time steps to create sequences for the model
time_step = 24

# Create the dataset to feed to the LSTM model
X, y = create_dataset(data, time_step)

# Reshape the data to be compatible with the LSTM model
X = X.reshape(X.shape[0], X.shape[1], 1)

# Split the data into training and testing sets
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
model.add(LSTM(50))
model.add(Dense(1))

model.compile(optimizer = "adam", loss = "mean_squared_error")

# Train the model
early_stopping = EarlyStopping(monitor = "val_loss", patience = 5)
history = model.fit(X_train, y_train, epochs = 50, batch_size = 64, validation_split = 0.2, callbacks = [early_stopping])

# Make predictions
y_pred = model.predict(X_test)

# Inverse transform predictions and actual values
y_test = y_test.reshape(-1, 1)
y_pred = y_pred.reshape(-1, 1)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Print results
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R²): {r2}")
```

Este modelo, con dos capas de LSTM y una completamente conectada es una excelente opción para resolver este problema por las siguientes razones:

- **Generalización**: la pérdida de validación se mantiene cercana a la pérdida de entrenamiento, lo que indica una buena capacidad de generalización a datos no vistos.
- **Métricas de Error**: las métricas de evaluación del modelo reflejan predicciones confiables.
- **Poder Predictivo**: el alto valor de R² demuestra que el modelo captura eficazmente las tendencias en los datos.

```python
# Save the model
model.save("../model/LSTM-model-air-quality.keras")
```

**Pérdida de entrenamieto y validación**

```python
# Plot training and validation loss curves
plt.figure(figsize = (11, 4))
plt.plot(history.history["loss"], label = "Pérdida de entrenamiento", color = "#e7298a")
plt.plot(history.history["val_loss"], label = "Pérdida de validación", color = "deepskyblue")
plt.title("Pérdida del modelo LSTM a lo largo de las épocas")
plt.ylabel("Pérdida")
plt.xlabel("Época")
plt.legend()
```

**Predicciones vs Valores Reales y valor R2**

```python
# Calcular r2 score
r2 = r2_score(y_test, y_pred)

# Plot predictions vs actual values
plt.figure(figsize =  (11, 4))
plt.plot(y_test, label="Concentración de NO$_2$ Real", color = "#e7298a")
plt.plot(y_pred, label="Concentración de NO$_2$ Predicha", color = "deepskyblue")
plt.title(f"Predicciones vs Valores Reales (R² = {r2:.2f})")
plt.ylabel("Concentración de NO$_2$")
plt.xlabel("Pasos de Tiempo")
plt.legend()
```

**Gráfica de residuos**

```python
# Calculate residual
residuals = y_test - y_pred

# Plot residuals
plt.figure(figsize=(11, 4))
plt.scatter(range(len(residuals)), residuals, color = "#e7298a")
plt.axhline(y = 0, color = "deepskyblue", linestyle = "--")
plt.title("Residuos")
plt.ylabel("Residuos")
plt.xlabel("Índice")
```

**Histograma de residuos**

```python
# Plot residuals histogram
plt.figure(figsize = (11, 4))
plt.hist(residuals, bins = 30, alpha = 0.7, color = "#e7298a")
plt.title("Histograma de residuos")
plt.xlabel("Residuos")
plt.ylabel("Frequencia")
```