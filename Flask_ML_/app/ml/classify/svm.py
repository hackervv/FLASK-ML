from app.ml.classify.classify_base import Classify
from sklearn import svm


class SVC(Classify):
    '''
    支持向量机分类
    created by: Exception
    created date: 2019-08-08
    '''
    def __init__(self,params):
        Classify.__init__(self)
        self._name = 'SVC'
        self._model = svm.SVC(**params)


