from app.ml.base import BaseModel

class Cluster(object):
    '''
    聚类模型基类
    created by: Exception
    created date: 2019-08-08
    '''

    def __init__(self):
        BaseModel.__init__()
        self._features = None

    def train(self, data):
        self._features = data
        self._model.fit(self._features)

    def getParameterDef(self):
        pass

    def setParameter(self,parameter):
        pass

    def predict(self, data):
        return self._model.predict(data)

