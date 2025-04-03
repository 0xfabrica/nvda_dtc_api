import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

with open('model_dtc_without_target.joblib', 'rb') as file:
    modelo = joblib.load(file)


app = FastAPI()

# Definir el esquema de datos de entrada
class DatosEntrada(BaseModel):
    Adj_Close: float
    Close: float
    High: float
    Low: float
    Open: float
    Volume: int

@app.post("/predict")
def predict(datos: DatosEntrada):
    # Convertir los datos de entrada a un DataFrame (manteniendo el mismo preprocesamiento que en entrenamiento)
    data = pd.DataFrame([datos.dict()])
    data = data.rename(columns={"Adj_Close": "Adj Close"})

    data['Tomorrow'] = 0  # Este valor es irrelevante para la predicción


    #features = ['Adj Close', 'Volume', 'Tomorrow']
    features = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume', 'Tomorrow']
    prediccion = modelo.predict(data[features])
    resultado = int(prediccion[0])
    # Devolver preddiccion con mensaje:
    mensaje = "SUBE" if resultado == 1 else "BAJA"

    return {"prediccion": resultado, "mensaje": mensaje}

# Para ejecutar localmente: 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)