class controller:
    layers = []
    interation = 0

    def __init__(self):
        pass

class layer:
    weights = [] #input, output

    def __init__(self):
        pass

    def check(self, inputs):
        #assert that formatting matches
        assert len(inputs) == len(self.weights), "input in controller" + "_" + "at layer" + "_" + "does not match size"
        
        #create output array
        output = []
        for _x in range(0, len(self.weights[0])):
            output.append(0)

        #multiply and add for outputs
        for input in range(0, len(inputs)):
            for weight in range(0, len(self.weights)):
                output[weight] += inputs[input] * self.weights[input][weight]
                # print(str(inputs[input]) + ", " + str(self.weights[input][weight]) + ", " + str(inputs[input] * self.weights[input][weight]))

        return output


test = layer() 
test.weights = [[0.25, 0.5], [0.75, 2]]
print(test.check([1, 2]))