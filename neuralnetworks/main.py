import nnfs
from activations.activations import Activation_ReLU, Activation_SoftMax
from layers.layers import Layer_Dense
from loss.loss import Loss_CategoricalCrossEntropy
from nnfs.datasets import spiral_data

# Create the dataset
nnfs.init() # neural networks from scratch (this tutorial)

X, y = spiral_data(100, 3) # 100 samples, 3 classes, x-y coordinates

dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3, 3)
activation2 = Activation_SoftMax()

dense1.forward(X)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output)

loss_function = Loss_CategoricalCrossEntropy()
loss = loss_function.calculate(activation2.output, y)

print(f"Loss: {loss}")
