class controller:
    layers = []
    interation = 0

    def __init__(self):
        pass

class layer:
    weights = [] #input, output

    def __init__(self, wieghts):
        pass

    def check(self, inputs):
        #assert that formatting matches
        assert len(inputs) == len(self.weights), "input in controller" + "_" + "at layer" + "_" + "does not match size"
        
        #create the ouput array
        output = []
        for _x in range(0, len(self.weights[0])):
            output.append(0)

        #sum the weights 
        for input in range(0, len(inputs)):
            for weight in range(0, len(self.weights[input])):
                output[weight] += input * self.weights[input][weight]

        return output