from random import seed
from random import randint

seed(1)

class system:
    system = []
    generation = 0
    seed = 1
    acceptancepercent = 0.75
    connectionAcceptancePercent = 0.9
    waitlist = []

    #[net]                  [layer]  [0 / 1]                      [pointer]
    #(controlls everything) (orders) (0 - neuron, 1 - connection) (way to see what object)

    def __init__(self, nets = 1, layers = 3):
        for x in range(0, nets):
            self.system.append([])
            for _ in range(0, layers):
                self.system[x].append([[], []])

    def createNet(self, net = 'auto'): # (self, int)
        if net == 'auto':
            self.system.append([[[], []]])
        else:
            self.system.insert(net, [[[], []]])

    def createLayer(self, net, layer = 'auto'): # (self, int, int)
        if layer == 'auto':
            self.system[net].append([[], []])
        else:
            self.system[net].insert(layer, [[], []])
    
    def createNeuron(self, id, net, layer, index = 'auto', type = 0, IO = 0): # (self, int, int, int, int, int, int)
        id = neuron(type, IO, id, self)
        if index == 'auto':
            self.system[net][layer][0].append(id)
        else:
            self.system[net][layer][0].insert(index, id)
        print(self.system)

    def createConnection(self, id, net, start, end, layer = 'auto', weight = 1): # (self, int, int, int, int, int, float)
        id = connection(start, end, weight, self, id)
        if layer == 'auto':
            for x in range(0, len(self.system)):
                for x2 in range(0, len(self.system[x])):
                    for x3 in range(0, len(self.system[x][x2][0])):
                        if self.system[x][x2][0][x3].name == start:
                            self.system[net][x2][1].append(id)
        else:
            self.system[net][layer][1].append(id)

    def check(self):
        for x in range(0, len(self.system)):
            #net
            for x2 in range(0, len(self.system[x])):
                #layer
                for x3 in range(0, len(self.system[x][x2][0])):
                    self.system[x][x2][0][x3].check()
                for x3 in range(0, len(self.system[x][x2][1])):
                    self.system[x][x2][1][x3].check()

    def Input(self, inputs, net = 'all', endNet = 'undefined'):
        if net == 'all':
            for x in range(0, len(self.system)):
                for x2 in range(0, len(self.system[x][0][0])):
                    self.system[x][0][0][x2].inputs.append(inputs[x][x2])
        elif net == endNet:
            for x in range(0, len(self.system[net][0][0])):
                self.system[net][0][0][x].inputs.append(inputs[x])
        else:
            for x in range(net, endNet + 1):
                for x2 in range(0, len(self.system[x][0][0])):
                    self.system[net][0][0][x].inputs.append(inputs[x][x2])

    def Output(self, net = 'all', layer = 'auto', index = 'auto'):
        output = []
        if net == 'all':
            if layer =='auto':
                for x in range(0, len(self.system)):
                    output.append([])
                    for x2 in range(0, len(self.system[x][-1][0])):
                        output[x].append(self.system[x][-1][0][x2].output)
            else:
                for x in range(0, len(self.system)):
                    output.append([])
                    for x2 in range(0, len(self.system[x][layer][0])):
                        output[x].append(self.system[x][layer][0][x2].output)
                
        else:
            if layer == 'auto':
                for x in range(0, len(self.system[net][-1][0])):
                    output.append(self.system[net][-1][0][x].output)
            else:
                if index == 'auto':
                    for x in range(0, len(self.system[net][layer][0])):
                        output.append(self.system[net][layer][0][x].output)
                else:
                    return self.system[net][layer][0][index].output
        return output

    def mutate(self, fitness, strength = 1, parentsnum = 1, list = 'default'):
        temp = []
        seed(self.seed)

        #get the list
        if list == 'default':
            tempin = self.system
        else:
            tempin = list
        
        #select the parents
        for x in range(0, len(tempin)):
            temp.append([])
            parents = []
            for x2 in range(0, parentsnum):
                num = randint(0, sum(fitness))
                for x3 in range(0, len(tempin)):
                    if num > fitness[x3]:
                        num -= fitness[x3]
                    else:
                        parents.append(x3)
                        break
            
            #combine parents
            temp[x] = tempin[parents[0]]
            passed = 0

            if parentsnum > 1:
                self.waitlist = []
                for x2 in range(1, len(parents)):
                    for x3 in range(1, len(tempin[parents[x2]]) - 1):
                        for x4 in range(0, len(tempin[parents[x2]][x3][0])):
                            print(tempin[parents[x2]][x3][0][x4])
                            passed = 0
                            for x5 in range(1, len(temp[x]) - 1):
                                for x6 in range(0, len(temp[x][x5][0])):
                                    if temp[x][x5][0][x6].search(tempin[parents[x2]][x3][0][x4]) >= self.acceptancepercent:
                                        temp[x][x5][0][x6].combine(tempin[parents[x2]][x3][0][x4], temp, tempin)
                                        passed = 1
                            if passed == 0:
                                temp[x][x3][x4].append()

                        for x4 in range(0, len(tempin[parents[x2]][x3][1])):
                            print(tempin[parents[x2]][x3][1][x4])
                            passed = 0
                            for x5 in range(0, len(temp[x])):
                                for x6 in range(0, len(temp[x][x5][1])):
                                    if temp[x][x5][1][x6] == 1:
                                        temp[x][x5][1][x6] * tempin[parents[x2]][x3][1][x4]
                                        passed = 1
                            if passed == 0:
                                temp[x][x3][x4].append()
                        
                            

class neuron:
    
    value = 0
    output = 0

    def __init__(self, type, IO, name, system):
        self.type = type
        self.IO = IO
        self.name = name
        self.inputs = []
        self.system = system

    def __repr__(self):
        return "<neuron type:" + str(self.type) + " IO:" + str(self.IO) + " name:" + str(self.name) + ">"

    def __str__(self):
        return self.__repr__()

    def __truediv__(self, other):
        raise Exception("YES.")

    def combine(self, other, temp, tempin):
        if (self.type == 2 or self.type == 3) and (other.type == 2 or other.type == 3):
            if self.type == 2 and other.type == 2:
                self.type = 2
            else:
                self.type = 3
        elif self.type == 1 and other.type == 1:
            self.type = 1
        else:
            self.type = 0
        if other.IO != 0 and self.IO == 0:
            self.IO = other.IO
        for x in range(0, len(tempin)):
            for x2 in range(0, len(tempin[x])):
                for x3 in range(0, len(tempin[x][x2][1])):
                    if other == tempin[x][x2][1][x3].startTrue:
                        self.system.waitlist.append(tempin[x][x2][1][x3])
                        self.system.waitlist[-1].startTrue == self
                    elif other == tempin[x][x2][1][x3].endTrue:
                        for x4 in range(0, len(self.system.waitlist)):
                            if self.system.waitlist[x4] == tempin[x][x2][1][x3]:
                                if len(temp) < len(tempin[x]):
                                    for x5 in range(0, len(temp)):
                                        for x6 in range(0, len(temp[x5][0])):
                                            if temp[x5][0][x6] == self.system.waitlist[x4].startTrue:
                                                temp[x5][1].append(self.system.waitlist[x4])
                                                temp[x5][1][-1].endTrue = self
                                else:
                                    temp[x2][1].append(self.system.waitlist[x4])
                                    temp[x2][1].endTrue = self

    def search(self, other, temp, dir = 0, tempin = []):
        #recursive search algorythm
        if dir == 0:
            tempself = []
            tempother = []
            for x in range(0, len(temp)):
                for x2 in range(0, len(temp[x])):
                    for x3 in range(0, len(temp[x][x2][1])):
                        if temp[x][x2][1][x3].startTrue == self:
                            tempself.extend(temp[x][x2][1][x3].endTrue.search(self, temp, 1))
                        elif temp[x][x2][1][x3].endTrue == self:
                            tempself.extend(temp[x][x2][1][x3].startTrue.search(self, temp, -1))
            for x in range(0, len(tempin)):
                for x2 in range(0, len(tempinp[x])):
                    for x3 in range(0, len(tempin[x][x2][1])):
                        if tempin[x][x2][1][x3].startTrue == other:
                            tempother.extend(tempin[x][x2][1][x3].endTrue.search(other, tempin, 1))
                        elif tempin[x][x2][1][x3].endTrue == other:
                            tempother.extend(tempin[x][x2][1][x3].startTrue.search(other, tempin, -1))
            tempremove = []
            for x in range(0, len(tempself)):
                found = 0
                for x2 in range(0, len(tempself)):
                    if found == 0 and tempself[x] == tempself[x2]:
                        found = 1
                    elif tempself[x] == tempself[x2]:
                        tempself.remove(tempself[x])
            for x in range(0, len(tempself)):
                found = 0
                for x2 in range(0, len(tempself)):
                    if found == 0 and tempself[x] == tempself[x2]:
                        found = 1
                    elif tempself[x] == tempself[x2]:
                        tempself.remove(tempself[x])
            for x in range(0, len(tempself)):
                for x2 in range(0, len(tempother)):
                    if tempself[x] == tempother[x2]:
                        tempremove.append(tempself[x])
                        tempself.remove(tempself[x])
                        tempother.remove(tempother[x2])
            return 2 * len(tempremove) / (len(tempself) + len(tempother) + 2 * len(tempremove))
        elif dir == 1:
            for x in range(0, len(temp)):
                for x2 in range(0, len(temp[x][-1][0])):
                    if temp[x][-1][0][x2] == self:
                        return self.name
            tempself = []
            for x in range(0, len(temp)):
                for x2 in range(0, len(temp[x])):
                    for x3 in range(0, len(temp[x][x2][1])):
                        if temp[x][x2][1][x3].startTrue == self:
                            tempself.extend(temp[x][x2][1][x3].endTrue.search(other, temp, 1))
            return tempself
        elif dir == -1:
            for x in range(0, len(temp)):
                for x2 in range(0, len(temp[x][0][0])):
                    if temp[x][0][0][x2] == self:
                        return self.name
            tempself = []
            for x in range(0, len(temp)):
                for x2 in range(0, len(temp[x])):
                    for x3 in range(0, len(temp[x][x2][1])):
                        if temp[x][x2][1][x3].endTrue == self:
                            tempself.extend(temp[x][x2][1][x3].endTrue.search(other, temp, 1))
            return tempself

        # if dir == 0:
        #     tempself = []
        #     tempother = []
        #     for x in range(0, len(self.system.system)):
        #         for x2 in range(0, len(self.system.system[x])):
        #             for x3 in range(0, len(self.system.system[x][x2][1])):
        #                 if self.system.system[x][x2][1][x3].startTrue == self:
        #                     tempself.append(self.system.system[x][x2][1][x3].endTrue.search(self, 1))
        #                 elif self.system.system[x][x2][1][x3].endTrue == self:
        #                     tempself.append(self.system.system[x][x2][1][x3].startTrue.search(self, -1))
        #                 elif self.system.system[x][x2][1][x3].startTrue == other:
        #                     tempother.append(self.system.system[x][x2][1][x3].endTrue.search(other, 1))
        #                 elif self.system.system[x][x2][1][x3].endTrue == other:
        #                     tempother.append(self.system.system[x][x2][1][x3].startTrue.search(other, -1))
        #     tempremove = []
        #     for x in range(0, len(tempself)):
        #         found = 0
        #         for x2 in range(0, len(tempself)):
        #             if found == 0 and tempself[x] == tempself[x2]:
        #                 found = 1
        #             elif tempself[x] == tempself[x2]:
        #                 tempself.remove(tempself[x])
        #     for x in range(0, len(tempother)):
        #         found = 0
        #         for x2 in range(0, len(tempother)):
        #             if found == 0 and tempother[x] == tempother[x2]:
        #                 found == 1
        #             elif tempother[x] == tempother[x2]:
        #                 tempther.remove(tempother[x])
        #     for x in range(0, len(tempself)):
        #         for x2 in range(0, len(tempother)):
        #             if tempself[x] == tempother[x2]:
        #                 tempremove.append(tempself[x])
        #     for x in range(0, len(tempremove)):
        #         for x2 in range(0, len(tempself)):
        #             if tempremove[x] == tempself[x2]:
        #                 tempself.remove(tempremove[x])
        #         for x2 in range(0, len(tempother)):
        #             if tempremove[x] == tempother[x2]:
        #                 tempother.remove(tempremove[x])
        #     return len(tempremove) / (2 * len(tempremove) + len(tempself) + len(tempother))

        # elif dir == 1:
        #     for x in range(0, len(self.system.system)):
        #         for x2 in range(0, len(self.system.system[x][-1][0])):
        #             if self.system.system[x][-1][0][x2] == self:
        #                 return self.name
        #     tempself = []
        #     for x in range(0, len(self.system.system)):
        #         for x2 in range(0, len(self.system.system[x])):
        #             for x3 in range(0, len(self.system[x][x2][1])):
        #                 if self.system.system[x][x2][1][x3].startTrue == self:
        #                     tempself.append(self.system[x][x2][1][x3].endTrue.search(other, 1))
        #     return tempself
        # else:
        #     for x in range(0, len(self.system.system)):
        #         for x2 in range(0, len(self.system.system[x][0][0])):
        #             if self.system.system[x][0][0][x2] == self:
        #                 return self.name
        #     tempself = []
        #     for x in range(0, len(self.system.system)):
        #         for x2 in range(0, len(self.system.system[x])):
        #             for x3 in range(0, len(self.system.system[x][x2][1])):
        #                 if self.system[x][x2][1][x3].endTrue == self:
        #                     tempself.append(self.system[x][x2][1][x3].startTrue.search(other, 1))
        #     return tempself

    def check(self):
        #get input
        
        self.value = sum(self.inputs)
        self.inputs = []
        if self.IO == -1:
            self.value = float(input('input for neuron ' + str(self.name) + ': '))
        elif self.IO == -2:
            self.value = 1

        #transform inputs

        if self.type == 0:
            self.output = self.value
        elif self.type == 1:
            if self.value > 0:
                self.output = self.value
            else:
                self.output = 0
        elif self.type == 2:
            if self.value >= 1:
                self.output = 1
            else:
                self.output = 0
        elif self.type == 3:
            if self.value >= 1:
                self.output = 1
            elif self.value <= -1:
                self.output = 1
            else:
                self.output = 0

        if self.IO == 1:
            print(self.output)


class connection:
    
    def __init__(self, start, end, weight, sys, name):
        self.start = start
        self.end = end
        self.weight = weight
        self.sys = sys
        self.name = name

        for x in range(0, len(sys.system)):
            #net
            for x2 in range(0, len(sys.system[x])):
                #layer
                for x3 in range(0, len(sys.system[x][x2][0])):
                    #index
                    if self.sys.system[x][x2][0][x3].name == self.start:
                        self.startTrue = self.system[x][x2][0][x3]
                    elif self.sys.system[x][x2][0][x3].name == self.end:
                        self.endTrue = self.system[x][x2][0][x3]
    
    def check(self):
        if not (self.startTrue.name == self.start and self.endTrue.name == self.end):
            for x in range(0, len(sys.system)):
                #net
                for x2 in range(0, len(sys.system[x])):
                    #layer
                    for x3 in range(0, len(sys.system[x][x2][0])):
                        #index
                        if self.sys.system[x][x2][0][x3].name == self.start:
                            self.startTrue = self.sys.system[x][x2][0][x3]
                        elif self.sys.system[x][x2][0][x3].name == self.end:
                            self.endTrue = self.sys.system[x][x2][0][x3]
        
        self.endTrue.inputs.append(self.weight * self.startTrue.output)
                            
    
    def __repr__(self):
        return "<connection start:" + str(self.start) + " end:" + str(self.end) + " weight:" + str(self.weight) + ">"

    def __str__(self):
        return self.__repr__()

    def search(self, other, temp, tempin):
        compare = [[[], []], [[], []]]
        sim = [[], []]
        compare[0][0] = self.startTrue.search(temp, self, -1)
        compare[0][1] = self.endTrue.search(temp, self, 1)
        compare[1][0] = other.startTrue.search(tempin, other, -1)
        compare[1][1] = other.endTrue.search(tempin, other, 1)

        for x in range(0, len(compare[0][0])):
            for x2 in range(0, len(compare[0][0])):
                if compare[0][0][x] == compare[0][0][x2]:
                    del compare[0][0][x2]
        for x in range(0, len(compare[0][1])):
            for x2 in range(0, len(compare[0][1])):
                if compare[0][1][x] == compare[0][1][x2]:
                    del compare[0][1][x2]
        for x in range(0, len(compare[1][0])):
            for x2 in range(0, len(compare[1][0])):
                if compare[1][0][x] == compare[1][0][x2]:
                    del compare[1][0][x2]
        for x in range(0, len(compare[1][1])):
            for x2 in range(0, len(compare[1][1])):
                if compare[1][1][x] == compare[1][1][x2]:
                    del compare[1][1][x2]
        for x in range(0, len(compare[0][0])):
            for x2 in range(0, len(compare[1][0])):
                if compare[0][0][x] == compare[1][0][x2]:
                    sim[0].append(compare[0][0][x])
                    del compare[0][0][x]
                    del compare[1][0][x2]
        for x in range(0, len(compare[0][1])):
            for x2 in range(0, len(compare[1][1])):
                if compare[0][1][x] == compare[1][1][x2]:
                    sim[1].append(compare[0][1][x])
                    del compare[0][1][x]
                    del compare[1][1][x2]
        return (2 * len(sim)) / (2 * len(sim) + (len(compare[0][0]) + len(compare[1][0] + len(compare[0][1]) + len(compare[1][1]))))

sys = system(2)
sys.createNeuron(1, 0, 0)
sys.createNeuron(2, 0, 1)
sys.createNeuron(3, 0, 2)
sys.createConnection(1, 0, 1, 2)
sys.createConnection(2, 0, 2, 3)

sys.createNeuron(1, 1, 0)
sys.createNeuron(2, 1, 1)
sys.createNeuron(3, 1, 2)
sys.createConnection(3, 1, 4, 5)
sys.createConnection(4, 1, 5, 6)

#0->0->0
#I  N  O
#x2

for x in range(0, 21):
    sys.Input([[x], [x]])
    sys.check()
    if sys.Output() == [[15.0], [15.0]]:
        print('success')
        break
#sys.mutate([1, 1])