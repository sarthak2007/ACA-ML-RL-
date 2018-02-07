import numpy as np
from numpy import genfromtxt
my_data = genfromtxt("/home/shashank/Downloads/train_1.csv", delimiter = ',')
theta = np.array(list(np.random.normal() for i in range(101)))
m = len(my_data[ : , 0])
n = 100
alpha = 1.0e-14
precision = 0.0001
zero = np.array(list(list(0 for i in range(m)) for j in range(102)))
zero = zero.reshape(m , n + 2)
zero[: , 0] = np.array(list(1 for i in range(len(zero[:,0]))))
zero[: , 1:] = my_data
my_data = zero
X = zero[: , :101]
Y = zero[: , 101]

def cost(p, data):
    s = 0
    for j in range(m):
        H = float(X[j, :].dot(np.transpose(p))) 
        s += (H - Y[j]) ** 2
    return float((1 / (2 * m)) * s)

def grad_desc(p, data):
    c = cost(p, data)
    prev_cost = 0.0
    while(abs((prev_cost - c) / c) > precision ):
        for i in range(m):
            H = float(X[i, :].dot(np.transpose(p)))
            for j in range(n + 1): 
                p[j] -= (alpha * (H - Y[i]) * X[i, j])
        prev_cost = c
        c = cost(p, data)
    return p
    
weights = grad_desc(theta, my_data)
print(weights)


    
            
                
                
