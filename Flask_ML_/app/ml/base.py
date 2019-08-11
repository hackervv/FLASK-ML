import uuid

class BaseModel(object):
    '''
    sklearn 模型基类
    created by:Exception
    created date：2019-08-04
    '''
    def __init__(self):
        self._uuid = str(uuid.uuid4())
        self._name = None

    def train(self,data):
        pass

    def getParameterDef(self):
        pass

    def setParameter(self, parameter):
        pass

    def predict(self, data):
        pass

    def getId(self):
        return self._uuid

    def getName(self):
        return self._name


