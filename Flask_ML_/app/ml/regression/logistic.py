from sklearn import linear_model
from app.ml.regression.regression_base import Regression

class LogisticRegression(Regression):
    '''
    逻辑回归模型类
    created by: Exception
    created date: 2019-08-07
    '''
    def __init__(self,params):
        Regression.__init__(self)
        self._name = 'Logistic'
        self._model = linear_model.LogisticRegression(**params)

    def predict_proba(self,data):
        return self._model.predict_proba(data)


