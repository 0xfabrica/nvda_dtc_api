# 🚀 Predictor de Tendencias Bursátiles con FastAPI y la acción de Nvidia ($NVDA)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)

## 📊 Descripción

Esta es una API REST desarrollada con FastAPI que utiliza un modelo de Machine Learning (DecisionTreeClassifier) para predecir la tendencia del mercado bursátil. El modelo analiza datos históricos de precios y volumen para predecir si el precio de una acción específica subirá o bajará en el futuro cercano. Esta herramienta puede ser útil para la toma de decisiones informadas en el ámbito del trading.

### 🎯 Características del Modelo

- **Tipo**: `DecisionTreeClassifier`
- **Objetivo**: Predicción binaria (SUBE/BAJA), donde:
    - `0`: Indica que se espera que el precio **BAJE**.
    - `1`: Indica que se espera que el precio **SUBA**.
- **Variables de entrada**:
    - `Adj_Close`: Precio de cierre ajustado.
    - `Close`: Precio de cierre.
    - `High`: Precio más alto alcanzado durante el período.
    - `Low`: Precio más bajo alcanzado durante el período.
    - `Open`: Precio de apertura.
    - `Volume`: Volumen de transacciones durante el período.

### 📈 Métricas de Rendimiento

El modelo fue evaluado utilizando un conjunto de datos de prueba independiente, obteniendo las siguientes métricas de rendimiento:

| Métrica    | Valor | Descripción                                                |
|------------|-------|------------------------------------------------------------|
| Accuracy   | 0.94  | Precisión general del modelo, porcentaje de predicciones correctas. |
| Precision  | 0.93  | Proporción de predicciones positivas correctas sobre todas las predicciones positivas. |
| Recall     | 0.94  | Proporción de instancias positivas reales identificadas correctamente. |
| F1-score   | 0.94  | Media armónica entre precisión y recall, proporcionando un equilibrio. |

#### Matriz de Confusión

La matriz de confusión muestra el rendimiento del modelo en términos de verdaderos positivos (VP), verdaderos negativos (VN), falsos positivos (FP) y falsos negativos (FN):

|                | Predicho 0 | Predicho 1 |
|----------------|------------|------------|
| **Real 0** | 2989 (VN)  | 185 (FP)   |
| **Real 1** | 211 (FN)   | 3173 (VP)  |

**Interpretación de la Matriz de Confusión:**

* **Verdaderos Negativos (VN):** 2989 instancias donde el modelo predijo correctamente que el precio bajaría.
* **Falsos Positivos (FP):** 185 instancias donde el modelo predijo incorrectamente que el precio subiría.
* **Falsos Negativos (FN):** 211 instancias donde el modelo predijo incorrectamente que el precio bajaría.
* **Verdaderos Positivos (VP):** 3173 instancias donde el modelo predijo correctamente que el precio subiría.

## 🛠️ Instalación

Sigue estos pasos para configurar el entorno y ejecutar la API:

```bash
# Clonar el repositorio
git clone https://github.com/0xfabrica/predictor-tendencias-bursatiles.git
# Navegar al directorio del proyecto
cd app

# Instalar las dependencias
pip install -r requirements.txt

# Arrancar proyecto
uvicorn main:app --reload

# Navegar al link de despliegue
http://127.0.0.1:(puerto)/docs/
```
Abrirás algo como esto:
![image](https://github.com/user-attachments/assets/1d883ccd-c45d-4e16-9ab1-97c67ec0e14c)

