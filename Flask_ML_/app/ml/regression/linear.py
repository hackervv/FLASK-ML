from sklearn import linear_model
from app.ml.regression.regression_base import Regression

class LinearRegression(Regression):
    '''
    线性回归模型类
    created by:Exception
    created date:2019-08-04
    '''
    def __init__(self,params):
        Regression.__init__(self)
        self._name = 'linear'
        self._model = linear_model.LinearRegression(**params)
        
