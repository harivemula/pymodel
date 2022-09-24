#import numpy as np
#import pandas as pd
from fastapi import FastAPI
from joblib import load
import os

app = FastAPI()

@app.get("/predict")
def predict_model (sl: float, sw: float, pl: float, pw: float):
    #input = np.array([iobj.sl, iobj.sw, iobj.pl, iobj.pw])
    #df = pd.DataFrame(data=input, columns=feature_names)
    model = load(os.path.join('./models', 'iris-sv-model'))
    print(model)
    pred = model([[sl, sw, pl, pw]])
    return {'species': int(pred[0])}
