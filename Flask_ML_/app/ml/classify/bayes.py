from sklearn.naive_bayes import GaussianNB
from app.ml.classify.classify_base import Classify

class NBayesClassifier(Classify):
    '''
    朴素贝叶斯分类器类
    created by: Exception
    created date: 2019-08-07
    '''
    def __init__(self,params):
        Classify.__init__(self)
        self._name = 'Bayes'
        self._model = GaussianNB(**params)