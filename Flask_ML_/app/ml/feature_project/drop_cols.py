import numpy as np
import pandas as pd


# 1. null值占总数据百分之八十以上
# 2. 单一数据占总数据百分之八十以上
# 3. 所有数据都一样 
def drop_useless_col(trainDf:pd.DataFrame,testDf:pd.DataFrame):        
    # 1. most_null
    most_null_cols_train = [col for col in trainDf.columns if trainDf[col].isnull().sum()/trainDf.shape[0] > 0.8]
    
    # 2. top_value
    top_value_cols_train = [col for col in trainDf.columns if trainDf[col].value_counts(dropna=False,normalize=True).values[0] > 0.9]
   
    # 3. one_value
    one_value_cols_train = [col for col in trainDf.columns if trainDf[col].nunique() <= 1]
    
    # 4. take unique cols from train and test
    drop_cols = list(set(most_null_cols_train + top_value_cols_train + one_value_cols_train))

    # 5. remove target
    if 'target' in drop_cols:
        drop_cols.remove('target')
    
    trainDf = trainDf.drop(drop_cols,axis=1)
    testDf = testDf.drop(drop_cols,axis=1)

    return trainDf, testDf

    


