__author__ = 'jxzheng'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def sigmoid(x,b,y):
    '''Compute the sigmoid function'''
    n = len(x)
    C = len(b)/n
    cWeight = b[(y * n):(y * (n + 1))]
    weightStack = b.reshape([C, n])
    return np.exp(-np.inner(x,cWeight))/np.sum(np.exp(-np.inner(weightStack, x)))

def computeGradient(b, X, y, lamb):
    '''Compute the loss function according to the data'''
    #Obviously need to iterate over all samples
    n = X.shape[1] #dimension of weight and a single sample
    C = len(b)/n
    N = X.shape[0]

    gradient = np.zeros(len(b))
    for i in range(0,N):
        gradient[(y[i] * n):(y[i] * n + n)] += X[i,:]
        for c in range(0,C):
            gradient[(c * n):(c * n + n)] += -sigmoid(X[i,:], b, c) * X[i,:]

    gradient += lamb * gradient
    return gradient

def computeGradientSGD(b,X,y,lamb):
    n = X.shape[1]
    N = X.shape[0]
    C = len(b)/n

    index = random.randint(0,N-1)
    gradient = np.zeros(len(b))
    for c in range(0,C):
        gradient[(c * n):(c * n + n)] += -sigmoid(X[index,:], b, c) * X[index,:]
    gradient[(y[index] * n):(y[index] * n + n)] += X[index,:]
    gradient += lamb * gradient
    return gradient

def computeGradientSVRG(b,X,y,lamb):
    '''wait we may not need this'''


#TODO: check what's the regularizer here should be

digits_test = pd.read_csv('logistic_digits_test.txt')
digits_train = pd.read_csv('logistic_digits_train.txt')
#news_test = pd.read_csv('logistic_news_test.txt')
#news_train = pd.read_csv('logistic_news_train.txt')
#print(digits_test)

