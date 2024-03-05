import matplotlib.pyplot as plt
import numpy as np

def firstExample():
  x = np.array([1,2,3])
  y = np.array([3.25,4,4.5])
  W = [];
  for i in range(len(x)):
    W.append([1, x[i]])

  X = np.array(W)

  XT = np.transpose(X)
  XTX = np.matmul(XT, X)
  XTXinv = np.linalg.inv(XTX)
  beta = np.matmul((np.matmul(XTXinv, XT)), np.transpose(y));

  def f(x):
    return beta[0] + beta[1] * x

  [a,b] = [min(x) - 1, max(x) + 1]
  plt.plot([a,b], [f(a), f(b)])
  plt.plot(x,y, 'o')
  plt.show()