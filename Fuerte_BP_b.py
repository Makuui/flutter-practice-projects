# -*- coding: utf-8 -*-
"""
Created on Wed Jan 4 17:52:21 2021

@author: Maria Arlyn
"""

from random import random
import math
import numpy as np
import pandas as pd

class BP(object):
    def __init__ (self, numberinputs = 3, h_layers = [3, 3], numberoutputs = 2):
        
        self.numberinputs = numberinputs
        self.h_layers = h_layers
        self.numberoutputs = numberoutputs
        
        self.error_training = 0
        
        layers = [numberinputs] + h_layers + [numberoutputs]
        
        weights = []
        for i in range(len(layers) - 1):
            w = np.random.rand(layers[i], layers[i + 1])
            weights.append(w)
        self.weights = weights
        
        der = [] #deratives
        for i in range(len(layers) - 1):
            d = np.zeros((layers[i], layers[i + 1]))
            der.append(d)
        self.der = der
        
        act = [] #activations
        for i in range(len(layers)):
            a = np.zeros(layers[i])
            act.append(a)
        self.act = act
        
    def forwardprop(self, inputs):
        act = inputs
        self.act[0] = act
        
        for i, w in enumerate(self.weights):
            net_input = np.dot(act, w)
        
            act = self.sigmoid(net_input)
            self.act[i + 1] = act
        return act
    
    def backprop(self, error):
        for i in reversed(range(len(self.der))):
            act = self.act[i+1]
            delta = error * self.sigmoid_der(act)
            reshape_delta = delta.reshape(delta.shape[0], -1).T
            current_act = self.act[i]
            current_act = current_act.reshape(current_act.shape[0],-1)

            self.der[i] = np.dot(current_act, reshape_delta)
            error = np.dot(delta, self.weights[i].T)
    
    def train(self, inputs, targets, epochs, lrate):
        for i in range(epochs):
            sum_errors = 0

            for j, input in enumerate(inputs):
                target = targets[j]

                output = self.forwardprop(input)
                error = target - output
                self.backprop(error)
                
                self.gradientdescent(lrate)
                sum_errors += self.mse(target, output)
            print("Error: {} at epoch {}".format(sum_errors / len(items), i+1))
        
        self.error_training = sum_errors / len(items)
        print("Complete!\n")
        
    def gradientdescent(self, lrate=1):
        for i in range(len(self.weights)):
            weights = self.weights[i]
            der = self.der[i]
            weights += der * lrate
            
    def sigmoid(self, x):
        y = 1.0 / (1 + np.exp (-x) )
        return y


    def sigmoid_der(self, x):
        return x * (1.0 - x)
    
    def mse(self, target, output):
        return np.average((target - output) ** 2)
    
df = pd.read_csv("iris.data", sep=",")
df = df[df.cls != 'Iris-setosa']
X = df[ ["sepal_length","sepal_width","petal_length","petal_width"] ].to_numpy()
y = df["cls"].to_numpy()
labels = np.unique(y)

label_dict = dict(enumerate(labels))
reversed_label_dict = {value : key for (key, value) in label_dict.items()}
y = np.array([reversed_label_dict [l] for l in y])

if __name__ == "__main__":

    items = X
    targets = y
    
    
    #4-1-2 network
    BP1 = BP(4, [1], 2)
    
    #4-10-2 network
    BP2 = BP(4, [10], 2)
    
    #4-2-2-2 network
    BP3 = BP(4, [2,2], 2)


    BP1.train(items, targets, 50, 0.1)
    BP2.train(items, targets, 50, 0.1)
    BP3.train(items, targets, 50, 0.1)

print("1. 4-1-3 Network:\nFinal Error: {}\n".format(BP1.error_training))
print("2. 4-10-3 Network:\nFinal Error: {}\n".format(BP2.error_training))
print("3. 4-2-2-3 Network:\nFinal Error: {}\n".format(BP3.error_training))
