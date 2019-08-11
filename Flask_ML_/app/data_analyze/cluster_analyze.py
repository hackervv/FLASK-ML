# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from app.ml.cluster.kmeans import KMEANSCluster
from app.ml.feature_project import label_map, drop_cols, fill_null

class cluBase(object):
    '''
    利用聚类进行数据分析
    created by: Exception
    created date: 2019-08-09
    '''
    def __init__(self,test:pd.DataFrame):
        #数据清洗和特征工程
        train = pd.read_csv("app/data_analyze/data/train.csv")
        train.rename(columns={'Survived':'Target'}, inplace=True)

        # 删除乘客id，以及乘客的名字
        train.drop(['PassengerId'], axis=1)
        test.drop(['PassengerId'], axis=1)

        train.drop(['Name'], axis=1)
        test.drop(['Name'], axis=1)
        
        # 1. 删除无用列
        train, test = drop_cols.drop_useless_col(train,test)
        # 2. label值映射
        train, test = label_map.lable_map(train,test) 
        # 3. 填充null值
        train, test = fill_null.fill_null_median(train,test)

        self._train = train
        self._test = test

    def kmeansPredict(self):
        params = {}
        clu = KMEANSCluster(params)
        clu.train(self._train)
        return clu.predict(self._test.values)


