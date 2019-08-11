from app.ml.cluster.cluster_base import Cluster
from sklearn.cluster import KMeans

class KMEANSCluster(Cluster):
    '''
    K-means 聚类
    created by: Exception
    created date: 2019-08-09
    '''
    def __init__(self,params):
        Cluster.__init__(self)
        self._name = 'K-Means'
        self._model = KMeans(**params)
        
