import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig, axs = plt.subplots(1,2)
data = pd.read_csv('realEstateAbridged.csv',sep=',')
col = list(data.columns)
col.remove('No')
data.plot(x='X4',y='Y', marker='.', linestyle='none', ax=axs[0])
dataFrame = pd.DataFrame(data, columns=col)
corrMat = dataFrame.corr()
print(corrMat)
axs[1].imshow(corrMat)
plt.show()