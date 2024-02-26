import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3])
y = np.array([3.25,4,4.5])
plt.plot(x,y, 'o')
A = np.array([
  [1,1],
  [1,2],
  [1,3]
])
ATran = np.transpose(A)
ATA = np.dot(ATran, A)
ATAInv = np.linalg.inv(ATA)
ALeftInv = np.dot(ATAInv, ATran)
beta = np.dot(ALeftInv, np.transpose(y))
def line(x):
  return beta[0] + beta[1]*x

plt.plot([1, 3], [line(1), line(3)])
plt.show()