#import numpy as np
#import pandas as pd
import fastapi as FastAPI
from joblib import load
from pydantic import BaseModel

class Iris(BaseModel):
    sl: float
    sw: float
    pl: float
    pw: float

feature_names = ['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']


app = FastAPI()

@app.get("/predict")
def predict_model (iobj: Iris):
    #input = np.array([iobj.sl, iobj.sw, iobj.pl, iobj.pw])
    #df = pd.DataFrame(data=input, columns=feature_names)
    model = load('models/iris-sv-model')
    pred = model([[iobj.sl, iobj.sw, iobj.pl, iobj.pw]])
    return {'species': int(pred[0])}
