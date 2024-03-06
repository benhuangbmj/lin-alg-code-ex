import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def secondEx(xVar='X4'):
# define a one-row-two-column subplot to display two figures side by side
  fig, axs = plt.subplots(1,2)
# load the data
  data = pd.read_csv('realEstateAbridged.csv',sep=',')
# capture the headers of the table
  col = list(data.columns)
# remove the "No" header 
  col.remove('No')
# plot a scatter plot and store it in the first figure
  data.plot(x=xVar,y='Y', marker='.', linestyle='none', ax=axs[0])
# create a dataFrame with the selected columuns
  dataFrame = pd.DataFrame(data, columns=col)
# find the correlation matrix
  corrMat = dataFrame.corr()
  print(corrMat)
# visualize the correlation matrix with a heat map in the second figure
  axs[1].imshow(corrMat)
# show the plot on the scree
  plt.show()