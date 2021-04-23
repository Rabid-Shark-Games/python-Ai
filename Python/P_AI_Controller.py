import random
import Python.P_AI_Layer as Layer



class Controller:
    layers = []
    rng = random.Random()
    interation = 0

    def __init__(self, layertype=Layer.Layer, layers=[], seed=0):
        #initialize random number generator
        self.rng.seed(seed)

        #handle layer generation
        if len(layers) == 0: #empty controller
            pass
        elif type(layers[0]) == Layer.Layer: #pre-created layers
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
