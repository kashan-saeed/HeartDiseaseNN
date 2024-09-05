# -*- coding: utf-8 -*-
"""184A_final_Understanding_Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ysTEs-7zKFKrWx-Lc-tq4J5aEvLQWHPy

# This is to understand the data better

### Setup
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

"""### Check GPU Avaliability"""

# Device configuration
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)

"""### Data"""

dataset1 = pd.read_csv('/content/drive/My Drive/184A/finalProj/data/processed.cleveland.txt', header = None)
dataset1.columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
dataset1 = dataset1.replace('?', np.nan)
dataset1 = dataset1.astype({'age': 'float64','sex': 'category','cp': 'category','trestbps': 'float64','chol': 'float64', 'fbs': 'category', 'restecg': 'category', 'thalach': 'float64', 'exang': 'category', 'oldpeak': 'float64', 'slope': 'category', 'ca': 'category', 'thal': 'category', 'num': 'category'})

dataset2 = pd.read_csv('/content/drive/My Drive/184A/finalProj/data/reprocessed.hungarian.txt', sep=" ", header = None)
dataset2.columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
dataset2 = dataset2.replace(-9, np.nan)
dataset2['ca'] = dataset2['ca'].replace(9, np.nan)
dataset2 = dataset2.astype({'age': 'float64','sex': 'category','cp': 'category','trestbps': 'float64','chol': 'float64', 'fbs': 'category', 'restecg': 'category', 'thalach': 'float64', 'exang': 'category', 'oldpeak': 'float64', 'slope': 'category', 'ca': 'category', 'thal': 'category', 'num': 'category'})

dataset3 = pd.read_csv('/content/drive/My Drive/184A/finalProj/data/processed.switzerland.txt', header = None)
dataset3.columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
dataset3 = dataset3.replace('?', np.nan)
dataset3['chol'] = dataset3['chol'].replace(0,np.nan)
dataset3 = dataset3.astype({'age': 'float64','sex': 'category','cp': 'category','trestbps': 'float64','chol': 'float64', 'fbs': 'category', 'restecg': 'category', 'thalach': 'float64', 'exang': 'category', 'oldpeak': 'float64', 'slope': 'category', 'ca': 'category', 'thal': 'category', 'num': 'category'})

dataset4 = pd.read_csv('/content/drive/My Drive/184A/finalProj/data/processed.va.txt', header = None)
dataset4.columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num']
dataset4 = dataset4.replace('?', np.nan)
dataset4['chol'] = dataset4['chol'].replace('0',np.nan)
dataset4['trestbps'] = dataset4['trestbps'].replace('0',np.nan)
dataset4 = dataset4.astype({'age': 'float64','sex': 'category','cp': 'category','trestbps': 'float64','chol': 'float64', 'fbs': 'category', 'restecg': 'category', 'thalach': 'float64', 'exang': 'category', 'oldpeak': 'float64', 'slope': 'category', 'ca': 'category', 'thal': 'category', 'num': 'category'})

'''
dataset1 = dataset1.dropna()
dataset1 = dataset1.reset_index(drop=True)

dataset2 = dataset2.drop(['ca', 'thal'], axis = 1)
dataset2 = dataset2.dropna()
dataset2 = dataset2.reset_index(drop=True)

dataset3 = dataset3.drop(['chol', 'fbs', 'ca', 'thal'], axis = 1)
#chol is all 0
dataset3 = dataset3.dropna()
dataset3 = dataset3.reset_index(drop=True)

dataset4 = dataset4.drop(['chol', 'slope', 'ca', 'thal'], axis = 1)
#has a lot of 0 on chol
dataset4 = dataset4.dropna()
dataset4 = dataset4.reset_index(drop=True)
'''
pass

datasetAll = pd.concat([dataset1, dataset2, dataset3, dataset4], ignore_index=True, sort=False)
datasetAll = datasetAll.dropna()
datasetAll = datasetAll.reset_index(drop=True)
print(datasetAll.shape)
print(datasetAll['num'].value_counts())

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
datasetAll.iloc[:,0:-1] = scaler.fit_transform(datasetAll.iloc[:,0:-1])

"""### Over/Undersampling"""

from collections import Counter
from imblearn.under_sampling import NeighbourhoodCleaningRule, TomekLinks, ClusterCentroids, NearMiss, EditedNearestNeighbours, CondensedNearestNeighbour, OneSidedSelection, RandomUnderSampler
from imblearn.over_sampling import SMOTE

X = datasetAll.iloc[:,0:-1]
y = datasetAll.iloc[:,-1]

print('Original dataset shape %s' % Counter(y))

#print('\nOversampling')
#smote = SMOTE()
#X, y = smote.fit_resample(X, y)
#print('SMOTE shape %s' % Counter(y))

print('\nRandom')
rus = RandomUnderSampler(sampling_strategy='auto')
X_res, y_res = rus.fit_resample(X, y)
print('RandomUnderSampler shape %s' % Counter(y_res))

print('\nKeep')
cnn = CondensedNearestNeighbour(sampling_strategy='auto')
X_res, y_res = cnn.fit_resample(X, y)
print('CondensedNearestNeighbour shape %s' % Counter(y_res))

nm = NearMiss(sampling_strategy='auto')
X_res, y_res = nm.fit_resample(X, y)
print('NearMiss shape %s' % Counter(y_res))

print('\nDelete')
tl = TomekLinks(sampling_strategy='auto')
X_res, y_res = tl.fit_resample(X, y)
print('TomekLinks shape %s' % Counter(y_res))

enn = EditedNearestNeighbours(sampling_strategy='majority')
X_res, y_res = enn.fit_resample(X, y)
print('EditedNearestNeighbours shape %s' % Counter(y_res))

print('\nBoth')
ncr = NeighbourhoodCleaningRule(sampling_strategy='auto')
X_res, y_res = ncr.fit_resample(X, y)
print('NeighbourhoodCleaningRule shape %s' % Counter(y_res))

oss = OneSidedSelection(sampling_strategy='auto')
X_res, y_res = oss.fit_resample(X, y)
print('OneSidedSelection shape %s' % Counter(y_res))

print()

cc = ClusterCentroids(sampling_strategy='auto')
X_res, y_res = cc.fit_resample(X, y)
print('ClusterCentroids shape %s' % Counter(y_res))
XSam = X_res
YSam = y_res

X = pd.DataFrame(XSam)
X.columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
X = X.astype({'age': 'float64','sex': 'category','cp': 'category','trestbps': 'float64','chol': 'float64', 'fbs': 'category', 'restecg': 'category', 'thalach': 'float64', 'exang': 'category', 'oldpeak': 'float64', 'slope': 'category', 'ca': 'category', 'thal': 'category'})
y = pd.DataFrame(YSam)
y.columns = ['num']
y = y.astype({'num': 'float64'})
#print(X)

"""### Feature Selection"""

#Univariate Selection
#apply SelectKBest class to extract top 13 best features
howMany = 13
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
bestfeatures = SelectKBest(score_func=chi2, k=howMany)
fit = bestfeatures.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)
#concat two dataframes for better visualization
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']  #naming the dataframe columns
print(featureScores.nlargest(howMany,'Score'))  #print 10 best features

#Feature Importance
#plot graph of feature importances for better visualization
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X,y)
importances = list(model.feature_importances_)
importances.sort(reverse=True)
print(np.array(importances)) #use inbuilt class feature_importances of tree based classifiers
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(13).plot(kind='barh')
plt.show()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#print(dataset1)
#print(dataset2)
#print(dataset3)
#print(dataset4)
#print(dataset)

"""### Datasets to Test"""

dataset = pd.concat([dataset1, dataset2, dataset3, dataset4], ignore_index=True, sort=False)

#top 6 features - oldpeak, chol, thalach, age, trestbps, ca
#middle - slope
#bottom - restecg, cp, thal, fbs, exang, sex (lowest)

#drop ca, slope, thal
#(558, 11)
datasetV1 = dataset.drop(['slope', 'ca', 'thal'], axis = 1)
datasetV1 = datasetV1.dropna()
datasetV1 = datasetV1.reset_index(drop=True)

#drop ca, thal (will lose 1/3 of data since slope is 1/3 nan)
#(392, 12)
datasetV2 = dataset.drop(['ca', 'thal'], axis = 1)
datasetV2 = datasetV2.dropna()
datasetV2 = datasetV2.reset_index(drop=True)

#drop thal (will still lose majority of data since ca had 2/3 nan)
#(297, 13)
datasetV3 = dataset.drop(['thal'], axis = 1)
datasetV3 = datasetV3.dropna()
datasetV3 = datasetV3.reset_index(drop=True)

print(datasetV1.shape)
print(datasetV1['num'].value_counts())
print(datasetV2.shape)
print(datasetV2['num'].value_counts())
print(datasetV3.shape)
print(datasetV3['num'].value_counts())

pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

import pandas_profiling as pp
import warnings
warnings.filterwarnings('ignore')

pp.ProfileReport(dataset1, title = 'Dataset1', html = {'style':{'full_width': True}})