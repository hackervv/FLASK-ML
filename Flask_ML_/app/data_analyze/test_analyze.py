import numpy as np
import pandas as pd
from app.ml.regression.linear import LinearRegression
from app.ml.regression import linear

def test_linear(x):
    feature = [1,4,8]
    target = [2,6,4]
    df = pd.DataFrame({'train':feature,'target':target})
    linearModel = linear.LinearRegression()
    linearModel.train(df)                        
    result = linearModel.preidct(x)
    return result
