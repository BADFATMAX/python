import numpy as np


class ModelNeuron:

    def __init__(self):
        self.n1 = Neuron()
        self.n2 = Neuron()
        self.n3 = Neuron()
        self.predicted_output = 0
        self.hidden_layer_output = np.array([])

    def forward_model(self, inputs):
        self.n1.forward(inputs)
        self.n2.forward(inputs)

        self.hidden_layer_output = np.concatenate((self.n1.output, self.n2.output), axis=1)

        self.n3.forward(self.hidden_layer_output)
        self.predicted_output = self.n3.output

    def backward_model(self, inputs, error):
        d_predicted_output = error * Neuron.sigmoid_derivative(self.predicted_output)
        error_hidden_layer = np.dot(d_predicted_output, self.n3.weigth().T)
        d_hidden_layer = error_hidden_layer * Neuron.sigmoid_derivative(self.hidden_layer_output)
        self.n3.backward(self.hidden_layer_output, d_predicted_output)
        d_hidden_layer_first, d_hidden_layer_second = np.split(d_hidden_layer, 2, axis=1)
        self.n1.backward(inputs, d_hidden_layer_first)
        self.n2.backward(inputs, d_hidden_layer_second)


class Neuron:

    def __init__(self):
        self._weigths = np.random.uniform(size=(2, 1))
        self.bias = np.random.rand()
        self.output = 0
        self.lr = 0.1

    def forward(self, inputs):
        activation = np.dot(inputs, self._weigths)
        activation += self.bias
        self.output = Neuron.sigmoid(activation)

    def backward(self, inputs, output):
        self._weigths = self._weigths + inputs.T.dot(output) * self.lr
        self.bias += np.sum(output, axis=0, keepdims=True) * self.lr

    def weigth(self):
        return self._weigths

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
        return x * (1 - x)



def loss(predict, expect):
    return expect - predict


# forward and backward возвращать значение

def main():
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    expected_output = np.array([[0], [1], [1], [0]])

    for i in range(5):
        error = []
        model = ModelNeuron()
        for epoch in range(20000):
            model.forward_model(inputs)
            error = loss(model.predicted_output, expected_output)
            model.backward_model(inputs, error)
        print(error)
        print(model.predicted_output)


if __name__ == '__main__':
    main()
