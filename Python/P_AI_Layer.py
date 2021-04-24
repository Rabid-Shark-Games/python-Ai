from _typeshed import NoneType
import random
import Python.P_AI_Decorators as Decorators



class Layer:
    weights = [] #input, output

    def __init__(self):
        self.weights = []

    @Decorators.inputlogger({"inputs": (list)})
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
    @Decorators.inputlogger({"generator": (str), "seed": (NoneType, int, float, str, bytes, bytearray), "inp": (int, float, str), "out": (int, float, str)})
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
