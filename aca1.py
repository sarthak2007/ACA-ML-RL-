import numpy as np
def coef(A):
    m=A.shape[0]     #rows
    n=A.shape[1]     #columns
    B=np.zeros((n,1),dtype=A.dtype)
    Y=A[:,n-1]
    X=np.delete(A,n-1,1)
    X=np.hstack((np.ones((m,1),dtype=A.dtype),X))
    for i in range(10000):
       B=B-0.000000000001/m*np.dot(X.transpose(),np.dot(X,B)-Y)
    return B
points=np.matrix(np.genfromtxt('aca.csv',delimiter=","))
print np.matrix(coef(points))
