import numpy as np
from numpy import genfromtxt
my_data = genfromtxt("/home/shashank/Downloads/train_1.csv", delimiter = ',')
theta = np.array(list(np.random.normal() for i in range(101)))
m = len(my_data[ : , 0])
n = 100
alpha = 3.5e-12
precision = 0.01
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
        H = float(np.matmul(X[j, :], np.transpose(p))) 
        s += (H - Y[j]) ** 2
    return float((1 / (2 * m)) * s)

def grad_desc(p, data):
    der = np.array(list(0 for i in range(n + 1)))
    c = cost(p, data)
    prev_cost = 0.1
    while(abs((prev_cost - c) / prev_cost) > precision ):
        for i in range(n + 1):
            der[i] = calc_der(p, data, i)
        p = p - (alpha * der)
        w = p
        prev_cost = c
        c = cost(p, data)
    return p
    
def calc_der(p, data, k):
    s = 0
    for j in range(m):
        H = float(np.matmul(X[j, :], np.transpose(p)))
        s += ( H - Y[j] ) * X[j, k]
    return float((1 / m) * s)
    
print(grad_desc(theta, my_data))


    
            
                
                
