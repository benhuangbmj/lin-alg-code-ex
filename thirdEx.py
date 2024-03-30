import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

def thirdEx():
  #load the data and set the first column as the index 
  data = pd.read_csv('realEstate.csv', sep=',', index_col=0)
  #get all headers
  headers = data.columns.tolist()
  #specify the columns for linear regression
  i = 1
  while i < 7:
    selectedColumns = headers[0:i]
    
    #prepare the data for regression
    X1 = pd.DataFrame(data, columns=selectedColumns).to_numpy()  
    X = np.insert(arr=X1, obj=0, values=1, axis=1)
    Y = pd.DataFrame(data, columns=[headers[6]]).to_numpy()
  
    #run the linear regression
    beta = np.linalg.lstsq(X, Y, rcond=None)[0]    
  
    #calcualte the coefficient of determination (R squared value)
    YPred = np.matmul(X, beta)
    r2 = r2_score(Y, YPred)
  
    #print the indicators
    print('Selected variables: ', selectedColumns)
    print('beta: ', beta)
    print('R squared: ', r2)
    if i == 6:
      D = np.array([[1, 2014.500, 20, 1884.6032,6,24.97398,121.54073]])
      print("Forecast: ", np.matmul(D, beta))
    i = i + 1
    #prepare a canvas with two rows and one column
    '''fig, ax = plt.subplots(2,1)
    plt.subplots_adjust(hspace=.6)
  
    #plot the regression line and the scattor graph of the data if only one variable is selected 
    def plotTheLine():
      if X1.shape[1] == 1:
        def f(x):
          return np.matmul(np.array([[1, x]]), beta)[0]
        data.plot(x=selectedColumns[0], xlabel=selectedColumns[0], y=headers[6], ylabel=headers[6], marker='.', linestyle='none', ax=ax[0])
        ax[0].plot([min(X1)[0], max(X1)[0]], [f(min(X1)[0]), f(max(X1)[0])], color='y')
    #plot the scatter graph of the true dependent values and the predicted dependent values together
    def plotThePoints():
      ax[1].scatter(np.array(range(len(Y))),Y)
      ax[1].scatter(np.array(range(len(Y))),YPred, color='y')
    
    plotTheLine()
    plotThePoints()
  
    #save the figures as a PNG file
    plt.savefig('my-plots.png')
    plt.show()'''