# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:24:15 2021

@author: Maria Arlyn
"""

from random import random
import math
import numpy as np
import pandas as pd


class SingleLayerPerceptron(object):
    def __init__(self, lrate=0.001, epoch=1000):
        self.lrate = lrate
        self.epoch = epoch
        self.weights = None
        self.bias = None
        
    def train(self, X, y):
        sample, feature = X.shape
        self.weights = np.zeros(feature)
        self.bias = 0

        for _ in range(self.epoch):
            predict_y = self.predict(X)
            weight_der = (1/sample) * np.dot(X.T, (predict_y - y))
            bias_der = (1/sample) * np.sum(predict_y - y)

            self.weights -= self.lrate * weight_der
            self.bias -= self.lrate * bias_der
            
    def relu(self, z):
        return np.maximum(0, z)
    
    def predict(self, X):
        predict_y = np.dot(X, self.weights) + self.bias
        return predict_y
    
    def mse(truth_y, predicted_y):
        return np.mean ((truth_y - predicted_y) **2)
    
def Train_Test(X, y, percentTrain=0.5):
    trainCount = math.floor(percentTrain * len(X))
    ind = np.arange(0, len(X)) #index
    trainIndex = np.random.choice(ind, trainCount, replace=False)
    trainIndex = np.sort(trainIndex)
    testIndex = np.array([i for i in np.arange(0, len(X)) if (i not in trainIndex)])
    
    x_train = np.array([x for i, x in enumerate(X) if (i in trainIndex)])
    y_train = np.array([y for i, y in enumerate(y) if (i in trainIndex)])
    x_test = np.array([x for i, x in enumerate(X) if (i in testIndex)])
    y_test = np.array([y for i, y in enumerate(y) if (i in testIndex)])
    return (x_train,y_train,x_test,y_test)
    
df = pd.read_csv("iris.data", sep=",")
X = df[ ["sepal_length","sepal_width","petal_length","petal_width"] ].to_numpy()
y = df['petal_width'].to_numpy()

if __name__ == "__main__":
    x_train, y_train, x_test, y_test = Train_Test (X, y, 0.8)
    items = x_train
    targets = y_train
    
#3-10-1 network
nn = SingleLayerPerceptron(lrate=0.01)
nn.train(items, targets)
    
input = x_test[0]
target = y_test[0]
    
predict_y = nn.predict(input)

print("3-1 Single Layer Perceptron")
print("Features: {},{},{}. Label: {}".format(input[0],input[1],input[2],target))
print()
print("Prediction {:0.5f}".format(predict_y))
print("Actual Target: {}".format(target))
print("MSE:", SingleLayerPerceptron.mse(target, predict_y))        