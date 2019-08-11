import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 将非数字的列映射成数字
def lable_map(trainDf:pd.DataFrame,testDf:pd.DataFrame):
    for col in trainDf.columns:
        if trainDf[col].dtype not in ['int64','int32','float64','float32']:
            le = LabelEncoder()
            le.fit(list(trainDf[col].astype(str).values) + list(testDf[col].astype(str).values))

            trainDf[col] = le.transform(list(trainDf[col].astype(str).values))
            testDf[col] = le.transform(list(testDf[col].astype(str).values))

    return trainDf,testDf
            

