import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def secondEx(xVar='X2'):
# define a one-row-two-column plot to display two figures side by side. The subplots are stored in axs
  fig, axs = plt.subplots(1,2)
# load the data and take the first column as the index
  data = pd.read_csv('realEstateAbridged.csv',index_col=0, sep=',')
# capture the headers of the table
  col = data.columns.tolist()
# get the full headers from realEstate.csv
  headers = pd.read_csv('realEstate.csv', index_col=0, nrows=0).columns.tolist();
# plot a scatter plot and store it in the first figure. Use the full header for as labels
  data.plot(x=xVar, xlabel=headers[col.index(xVar)], y='Y', ylabel=headers[col.index('Y')], marker='.', linestyle='none', ax=axs[0])
# create a dataFrame with the selected columuns
  dataFrame = pd.DataFrame(data, columns=col)
# find the correlation matrix
  corrMat = dataFrame.corr()
  print(corrMat)
# visualize the correlation matrix with a heat map in the second figure
  axs[1].imshow(corrMat)
# show the plot on the scree
  plt.show()