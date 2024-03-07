import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('realEstateAbridged.csv',sep=',', index_col=0)
headers = data.columns.tolist()
xVar = headers[2]

X1 = np.array(pd.DataFrame(data, columns=headers[2:3]))
Y = np.array(pd.DataFrame(data, columns=[headers[6]]))

X = np.insert(arr=X1, obj=0, values=1, axis=1)
beta = np.linalg.lstsq(X, Y, rcond=None)[0]
def f(x):
  return beta[0] + beta[1]*x
fig, ax = plt.subplots()
data.plot(x=xVar, xlabel=xVar, y=headers[6], ylabel=headers[6], marker='.', linestyle='none', ax=ax, color='y')
ax.plot([min(X1), max(X1)], [f(min(X1)), f(max(X1))])
plt.show()