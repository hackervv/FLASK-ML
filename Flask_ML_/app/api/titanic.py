from flask_restplus import Api, Resource,fields
from flask import Flask
from app import app
import numpy as np
import pandas as pd
from flask import jsonify
from werkzeug.contrib.fixers import ProxyFix

from app.data_analyze.regression_analyze import regBase
from app.data_analyze.classify_analyze import clfBase
from app.data_analyze.cluster_analyze import cluBase
from app.model.dto import passergerInfo

from app.utils.redis import Redis


# 公共api对象

# 回归接口
api = Api(app,version='1.0',title='Titanic survive predict API',description='API for titanic passenger survive predict with machine learning',default='Regression',default_label='')
app.wsgi_app = ProxyFix(app.wsgi_app)

# 分类接口
clf_ns = api.namespace('Classifier')

# 聚类接口
clu_ns = api.namespace('Cluster')

passengerInfo = api.model('passengerInfo',passergerInfo)

# ----- Regression -------
@api.route('/Regression/LinearRegression/')
class LinearRegression(Resource):
    @api.doc('Linear Regression')
    @api.expect(passengerInfo)
    #@api.marshal_with(passengerInfo)
    def post(self):
        test = pd.DataFrame(api.payload,index=[0])
        reg = regBase(test)
        return reg.linearRegPredict()

@api.route('/Regression/LogisticRegression/')
class LogisticRegresion(Resource):
    @api.doc('Logistic Regression')
    @api.expect(passengerInfo)
    def post(self):
        test = pd.DataFrame(api.payload,index=[0])
        reg = regBase(test)
        res = reg.logisticRegPredict().tolist()[0]
        return jsonify({'Survived': res[1]})
    
# ------ Classifier -------

@clf_ns.route('/BayesClassifier/')
class BayesClassifier(Resource):
   @clf_ns.doc('Bayes Classifier')
   @clf_ns.expect(passengerInfo)
   def post(self):
       test = pd.DataFrame(clf_ns.payload,index=[0])
       clf = clfBase(test)
       res = clf.bayesClssiferPreidct().tolist()
       return jsonify({'Survived':res})

@clf_ns.route('/SVClassifier/')
class SVC(Resource):
    @clf_ns.doc('SVC Classifier')
    @clf_ns.expect(passengerInfo)
    def post(self):
        test = pd.DataFrame(clf_ns.payload,index=[0])
        clf = clfBase(test)
        res = clf.SVCPredict().tolist()
        return jsonify({'Survived':res})

@clf_ns.route('/SGDClassifier/')
class SGDClassifier(Resource):
    @clf_ns.doc('SGDClassifier')
    @clf_ns.expect(passengerInfo)
    def post(self):
        test = pd.DataFrame(clf_ns.payload,index=[0])
        clf = clfBase(test)
        res = clf.SGDClassifierPredict().tolist()
        return jsonify({'Survived':res})

#------ Cluster ----------

@clu_ns.route('/K-Means/')
class KMeams(Resource):
    @clu_ns.doc('K-Means Cluster')
    @clf_ns.expect([passengerInfo])
    def post(self):
        test = pd.DataFrame(np.array(clu_ns.payload),index=[0])
        clu = cluBase(test)
        res = clu.kmeansPredict().tolist()
        return jsonify({'data':res})









        




