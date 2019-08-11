from app.ml.base  import BaseModel
import numpy as np
import pandas as pd

class Regression(BaseModel):
    '''
    回归模型基类
    created by:Exception
    created date:2019-08-04
    '''

    def __init__(self):
        BaseModel.__init__(self)
        self._features = None
        self._target = None

    def train(self,data):
        self._features = data.drop('Target',axis=1)
        self._target = data['Target']
        self._model.fit(self._features,self._target)

    def getParameterDef(self):
        pass

    def setParameter(self, parameter):
        pass

    def preidct(self, data):
        print(data,'======data=====')
        return self._model.predict(data)





