import numpy as np
import pandas as pd
from fastapi import FastAPI
from joblib import load

app = FastAPI()
feature_names = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
target_names = ['setosa', 'versicolor', 'virginica']
@app.get("/predict")
def predict_model (sl: float, sw: float, pl: float, pw: float):
    input = np.array([[sl, sw, pl, pw]])
    df = pd.DataFrame(data=input, columns=feature_names)
    model = load('./models/iris-sv-model')
    print(model)
    pred = model.predict([[sl, sw, pl, pw]])
    return {'species': target_names[int(pred[0])]}
