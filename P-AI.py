class controller:
    layers = []
    interation = 0

    def __init__(self):
        pass

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



class layer:
    weights = [] #input, output

    def __init__(self):
        pass

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


test = layer() 
test.weights = [[2]]

test1 = layer()
test1.weights = [[1, 0.5]]

test2 = layer()
test2.weights = [[0.25], [3]]

control = controller()
control.layers = [test, test1, test2]

print()
print(control.check([2.0]))