import random, copy


class Layer:
    weights = [] # Which order dimensions go in. like the order is the INPUT first, like the first number you put in is the weight the input corrosponds to, and the second number - wait... the second number is the OUTPUT the INPUT WEIGHT corrosponds to.

    def __init__(self):
        self.weights = []

    def check(self, inputs):

        #assert that formatting matches
        assert len(inputs) == len(self.weights), "input in controller " + "TODO" + " at layer " + "TODO" + " does not match size"

        #create output array
        output = []
        # a for loop that loops over everything in self.weights
        for _x in range(0, len(self.weights[0])):
            # The python function 'append' is documented at https://docs.python.org/3/tutorial/datastructures.html and the source code is somewhere, I assume. Github: https://github.com/python/cpython THIS HELPFUL COMMENT WAS WRITTEN BY ThatCreeper!!!!!11!!
            output.append(0)

        #multiply and add for outputs
        # loops through inputs
        for input in range(0, len(inputs)):
            #loops through input
            for weight in range(0, len(self.weights[input])):
                # runs the code output[weight] += inputs[input] * self.weights[input][weight] which adds inputs[input] multiplied self.weights[input][weight] to output[weight]. self.weights[input][weight] is self explanitory
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
            # does something, i presume
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

class System:
    controllers = []
    cycle = {}

    def __init__(self):
        pass

    def addController(self, controller=Controller(), number=1):
        if type(controller) == type:
            for _x in range(0, number):
                self.controllers.append(controller())
        elif issubclass(Controller, type(controller)):
            for _x in range(0, number):
                self.controllers.append(copy.deepcopy(controller))



test = Controller(layers=[1, 2, 2, 1])
for x in test.layers:
    print(x.weights)
