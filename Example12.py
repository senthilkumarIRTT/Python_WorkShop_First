import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
X = np.array([[0,0],[1,1]])
Y = [0,1]
clf.fit(X,Y)
clf =svm.SVC()
svc(kernel='precomputed')
clf.predict(gram)
plt.scatter(X[:,0],X[:,1],c=Y,s=50,cmap='spring')
plt.show()

