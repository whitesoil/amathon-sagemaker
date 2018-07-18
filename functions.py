import numpy as np

def cross_entropy_error_general(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 훈련 데이터가 원-핫 벡터라면 정답 레이블의 인덱스로 반환
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    return -1 * np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))

def relu(x):
    return np.maximum(0,x)

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def step_function(x):
    y = x > 0 
    return y.astype(np.int)

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

def relu_grad(x):
    grad = np.zeros(x)
    grad[x>=0] = 1
    return grad

def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)