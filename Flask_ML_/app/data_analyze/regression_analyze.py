# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pickle
from app.ml.regression.linear import LinearRegression
from app.ml.regression.logistic import LogisticRegression
from app.ml.feature_project import label_map, drop_cols, fill_null
from app.utils.redis import Redis


class regBase(object):
    '''
    利用回归进行数据分析类
    created by: Exception
    created date: 2019-08-06
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

    def linearRegPredict(self):
        params = {'n_jobs':1}
        linear_model = Redis.read('LINEAR')
        if linear_model:
            linearReg = pickle.loads(linear_model)
        else:
            linearReg = LinearRegression(params)
            linearReg.train(self._train)
            Redis.write('LINEAR',pickle.dumps(linearReg))
        return linearReg.predict(self._test.values)

    def logisticRegPredict(self):
        params = {}
        logistic_model = Redis.read('LOGISTIC')
        if logistic_model:
            logisticReg = pickle.loads(logistic_model)
        else:
            logisticReg = LogisticRegression(params)
            logisticReg.train(self._train)
            Redis.write('LOGISTIC',pickle.dumps(logisticReg))
        return logisticReg.predict_proba(self._test.values)

        



