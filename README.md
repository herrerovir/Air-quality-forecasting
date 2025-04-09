# Test 2: Time Series Regression - Air Quality Forecasting

En este proyecto, se lleva a cabo un proceso de machine learning de principio a fin, con el objetivo de predecir la calidad del aire usando datos de series temporales. En el cuaderno Jupyter se detalla paso a paso todas las decisiones tomadas desde la limpieza de los datos hasta el desarrollo y evaluación del modelo.

**Motivación**

Elegí este conjunto de datos porque es relevante para mi formación como ingeniero químico especializada en control de calidad. Predecir la calidad del aire es una gran oportunidad para mostrar mis habilidades en ingeniería aplicada a la ciencia de datos, especialmente en el ámbito del control de calidad para diferentes industrias.

## Tabla de contenidos

- [Contenido del repositorio](#contenido-del-repositorio)
- [Estructura del notebook](#estructura-del-notebook)
- [Dependencias](#dependencias)
- [Instalar dependencias](#instalar)
- [Como ejecutar el projecto](#como-ejecutar-el-proyecto)
- [Dataset](#dataset)
- [Modelado](#modelado)
- [Resultados](#resultados)

## Contenido del repositorio

```plaintext
VHC-TestDataScience-2/
│
├── data/                               # Conjunto de datos
│   ├── raw/                            # Datos originales
│   ├── processed/                      # Datos limpios
│
├── models/                             # Modelos entrenados
│   ├── LSTM-model-air-quality.keras    # Modelo guardado en formato keras
│
├── notebooks/                          # Jupyter notebooks
│   ├── VHC-TestDataScience-2.ipynb     # Proyecto completo de inicio a fin
│   └── VHC-TestDataScience-2.html      # Proyecto completo en formato HTML
│
├── results/                            # Resultados del proyecto
│   ├── figures/                        # Gráficas generadas
│   └── model_results.txt               # Resultados del modelo
│
├── requirements.txt                    # Dependencias del proyecto
└── README.md                           # Documentación del proyecto
```

## Estructura del notebook

1. **Introducción**: descripción del problema, motivación y objetivo del proyecto.
2. **Dataset**: descripción del conjunto de datos.
2. **Carga de Datos**: importación y exploración inicial del conjunto de datos.
3. **Limpieza de los datos**: limpieza y preprocesado inicial de los datos.
4. **Estacionalidad**: comprobación de la no-estacionalidad de la serie temporal.
5. **Análisis exploratorio**: exploración de la variable objetivo y las características.
6. **Preprocesado**: procesamiento de los datos antes del modelado.
7. **Modelado**: construcción de la red neuronal recurrente.
8. **Predicciones**: obtener las predicciones para los siguientes 100 ciclos.

9. **Conclusiones**: Resumen del proyecto y los resultados obtenidos.

## Dependencias

Todas las dependencias necesarias para este proyecto están listadas en el fichero **requirements.txt**, entre las que se encuentran: 

- Python
- Jupyter Notebooks
- Pandas
- NumPy
- Tensorflow
- Matplotlib
- Seaborn

## Instalar dependencias

Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes librerías de Python:

```{shell}
pip install -r requirements.txt
```

## Como ejecutar el proyecto

1. Clona este repositorio:
   ```{shell}
   git clone https://github.com/herrerovir/VHC-TestDataScience-2.git
   ```
2. Navega al directorio del proyecto:
   ```{shell}
   cd VHC-TestDataScience-2
   ```
3. Abre el notebook:
   ```{shell}
   jupyter notebook

## Dataset

El conjunto de datos utilizado en este proyecto se obtuvo del UCI Machine Learning Repository [here](https://archive.ics.uci.edu/dataset/360/air+quality). Este dataset consiste en 9471 entradas y 16 columnas. 

## Modelado

El modelo elegido para este proyecto fue una red neuronal recurrente, en concreto LSTM (Long Short-Term Memory). Lo interesante de la LSTM es que está hecha para aprender de datos en secuencia, lo que la hace perfecta para predecir la calidad del aire. Por tanto, en este proyecto se logró construir un modelo sólido que mostró métricas de evaluación muy buenas y una alta puntuación R², lo que indica un rendimiento efectivo. Por último, se realizaron predicciones para los próximos 100 ciclos sin utilizar variables de regresión, tal como se había solicitado en el ejercicio.

## Resultados

A continuación se muestran las gráficas que recogen y muestran las metricas y resultados del modelo xgboost:

**Pérdida del modelo a través de las épocas**

![LSTM-training-validation-loss-graph](https://github.com/user-attachments/assets/2d04ad70-60b4-487a-893b-163726c69513)

**Predicciones vs valores reales**

![LSTM-prediction-vs-real-values-plot](https://github.com/user-attachments/assets/5b226064-1ea5-45f5-bada-bf119e318161)

**Residuos**

![LSTM-residues-graph](https://github.com/user-attachments/assets/fd18386f-fc2f-4399-b4b6-1a16448a902c)

**Histograma de residuos**

![LSTM-residues-histogram](https://github.com/user-attachments/assets/34c8f10f-9705-402f-8baf-82426553ad2c)

