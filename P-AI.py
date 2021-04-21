import random


class Layer:
    weights = [] #input, output

    def __init__(self):
        self.weights = []

    def check(self, inputs):

        #assert that formatting matches
        assert len(inputs) == len(self.weights), "input in controller " + "TODO" + " at layer " + "TODO" + " does not match size"
        
        #create output array
        output = []
        for _x in range(0, len(self.weights[0])):
            output.append(0)

        #multiply and add for outputs
        for input in range(0, len(inputs)):
            for weight in range(0, len(self.weights[input])):
                output[weight] += inputs[input] * self.weights[input][weight]
                print(str(inputs[input]) + ", " + str(self.weights[input][weight]) + ", " + str(inputs[input] * self.weights[input][weight]))

        return output

    @classmethod
    def generate(cls, generator="basic", seed=0, inp=10, out=10):
        
        #ensure that inp and out are both integers
        inp = int(inp)
        out = int(out)

        #create the random for generation
        rng = random.Random()
        rng.seed(seed)

        #create the output class
        temp = cls()

        #initiate the weights
        for neuron in range(0, inp):
            temp.weights.append([])
            for _weight in range(0, out):
                if generator == "basic":
                    temp.weights[neuron].append(rng.uniform(-1, 1))

        #return the temp object
        return temp



class Controller:
    layers = []
    rng = random.Random()
    interation = 0

    def __init__(self, layertype=Layer, layers=[], seed=0):
        #initialize random number generator
        self.rng.seed(seed)

        #handle layer generation
        if len(layers) == 0: #empty controller
            pass
        elif type(layers[0]) == Layer: #pre-created layers
            for layer in layers:
                self.layers.append(layer)
        elif type(layers[0]) == int or type(layers[0]) == float: #generated layers
            for layer in range(0, len(layers) - 1):
                self.layers.append(layertype.generate(seed=self.rng.random(), inp=layers[layer], out=layers[layer + 1]))

    def check(self, input):
        output = []

        for layer in range(0, len(self.layers)):

            #first layer
            if layer == 0:
                output = self.layers[layer].check(input)
            
            #middle layers
            elif layer != len(self.layers) - 1:
                output = self.layers[layer].check(output)

            #last layer
            else:
                return self.layers[layer].check(output)

            #debug info
            print(output)
            


test = Controller(layers=[1, 2, 2, 1])
for x in test.layers:
    print(x.weights)