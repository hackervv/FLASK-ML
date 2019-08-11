from app.ml.classify.classify_base import Classify
from sklearn import linear_model

class SGDClassifier(Classify):
    '''
    随机梯度下降分类器
    created by: Exception
    created date: 2019-08-09
    '''

    def __init__(self,params):
        Classify.__init__(self)
        self._name = 'SGDClassifier'
        self._model = linear_model.SGDClassifier(**params)

