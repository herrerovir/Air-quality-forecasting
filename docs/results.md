# Conclusiones

El objetivo de este ejercicio fue crear un modelo de machine learning para predecir la calidad del aire en el futuro. El primer paso y uno de los más importantes es la limpieza de los datos. Este es una etapa esencial en el análisis de datos para asegurar que la información sea íntegra y confiable. Además, Se verificó que no hubiera estacionalidad en los datos, tal como se mencionaba en el planteamiento del problema. Antes del modelado se llevó a cabo una exploración de las variables para descubrir información relevante, tendencias y relaciones entre las variables. 

El modelo elegido para este proyecto fue una red neuronal recurrente, en concreto LSTM (Long Short-Term Memory). Lo interesante de la LSTM es que está hecha para aprender de datos en secuencia, lo que la hace perfecta para predecir la calidad del aire

Al final, se logró construir un modelo sólido que mostró métricas de evaluación muy buenas y una alta puntuación R², lo que indica un rendimiento efectivo. Por último, se realizaron predicciones para los próximos 100 ciclos sin utilizar variables de regresión, tal como se había solicitado en el ejercicio.