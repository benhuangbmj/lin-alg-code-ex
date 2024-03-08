import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

def thirdEx():
  data = pd.read_csv('realEstateAbridged.csv',sep=',', index_col=0)
  headers = data.columns.tolist()
  selectedColumns = headers[0:4]
  
  X1 = np.array(pd.DataFrame(data, columns=selectedColumns))
  Y = np.array(pd.DataFrame(data, columns=[headers[6]]))
  
  X = np.insert(arr=X1, obj=0, values=1, axis=1)
  beta = np.linalg.lstsq(X, Y, rcond=None)[0]
  
  YPred = np.matmul(X, beta)
  r2 = r2_score(Y, YPred)
  print('Selected variables: ', selectedColumns)
  print('R squared: ', r2)
  
  fig, ax = plt.subplots(2,1)
  
  def plotTheLine():
    if X1.shape[1] == 1:
      def f(x):
        return np.matmul(np.array([[1, x]]), beta)[0]
      data.plot(x=selectedColumns[0], xlabel=selectedColumns[0], y=headers[6], ylabel=headers[6], marker='.', linestyle='none', ax=ax[0])
      ax[0].plot([min(X1)[0], max(X1)[0]], [f(min(X1)[0]), f(max(X1)[0])], color='y')
  
  def plotThePoints():
    ax[1].scatter(np.array(range(len(Y))),Y)
    ax[1].scatter(np.array(range(len(Y))),YPred, color='y')
  
  plotTheLine()
  plotThePoints()
  
  plt.show()