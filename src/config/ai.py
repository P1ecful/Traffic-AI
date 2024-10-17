import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

class Neuron:
  def __init__(self, weights, bias):
    self.weights = weights
    self.bias = bias

  def feedforward(self, inputs):
    total = np.dot(self.weights, inputs) + self.bias
    return sigmoid(total)

class OurNeuralNetwork:
  def __init__(self):
    self.h1 = Neuron(np.array([0, 1]), 0)
    self.h2 = Neuron(np.array([0, 1]), 0)
    self.o1 = Neuron(np.array([0, 1]), 0)

  def feedforward(self, x):
    out_h1 = self.h1.feedforward(x)
    out_h2 = self.h2.feedforward(x)

    out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
    return out_o1

