from app.ml.base import BaseModel


class Classify(BaseModel):
    '''
    分类模型基类
    created by: Exception
    created date: 2019-08-07
    '''
    def __init__(self):
        BaseModel.__init__(self)
        self._target = None
        self._features = None

    def train(self, data):
        self._features = data.drop('Target',axis=1)
        self._target = data['Target']
        self._model.fit(self._features, self._target)


    def getParameterDef(self):
        pass

    def setParameter(self, parameter):
        pass

    def predict(self, data):
        return self._model.predict(data)
