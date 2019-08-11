import numpy as np
import pandas as pd

# null 值填充
# testDf中的null值 用trainDf的平均值来填充
def fill_null_median(trainDf:pd.DataFrame,testDf:pd.DataFrame):
   
    for col in trainDf.columns:
        if trainDf[col].isnull().sum() > 0:
            trainDf[col] = trainDf[col].fillna(trainDf[col].median())
        if col != 'Target' and testDf[col].isnull().sum() > 0 :
            trainDf[col] = testDf[col].fillna(trainDf[col].median())

    return trainDf,testDf



