# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import pickle
from app.ml.classify.bayes import NBayesClassifier
from app.ml.classify.svm import SVC
from app.ml.classify.sgd import SGDClassifier
from app.ml.feature_project import label_map, drop_cols, fill_null
from app.utils.redis import Redis

class clfBase(object):
    '''
    利用分类器对数据进行分析
    created by: Exception
    created date: 2019-08-07
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

    def bayesClssiferPreidct(self):
        # 朴素贝叶斯分类方法
        params = {}
        # 训练之前先读取redis是否存在已经训练好的模型，如果有，直接反序列化读取对象，如果没有训练新的模型并写入redis
        bayes_model = Redis.read('BAYES')
        if bayes_model:
            bayesClf = pickle.loads(bayes_model)
        else:
            bayesClf = NBayesClassifier(params)
            bayesClf.train(self._train)
            Redis.write('BAYES',pickle.dumps(bayesClf))
        return bayesClf.predict(self._test.values)[0]

    def SVCPredict(self):
        # 支持向量机分类方法
        params = {}
        svc_model = Redis.read('SVC')
        if svc_model:
             SVClf = pickle.loads(svc_model)
        else:
            SVClf = SVC(params)
            SVClf.train(self._train)
            Redis.write('SVC',pickle.dumps(SVClf))
        return SVClf.predict(self._test.values)[0]

    def SGDClassifierPredict(self):
        # 随机梯度下降分类方法
        params = {}
        sgd_model = Redis.read('SGD')
        if sgd_model:
            SGDClf = pickle.loads(sgd_model)
        else:
            SGDClf = SGDClassifier(params)
            SGDClf.train(self._train)
            Redis.write('SGD',pickle.dumps(SGDClf))
        return SGDClf.predict(self._test.values)[0]



