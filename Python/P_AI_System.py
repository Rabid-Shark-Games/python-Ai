import copy
import Python.P_AI_Controller as Controller



class System:
    controllers = []
    cycle = {}

    def __init__(self):
        pass

    def addController(self, controller=Controller.Controller(), number=1):
        if type(controller) == type:
            for _x in range(0, number):
                self.controllers.append(controller())
        elif issubclass(Controller.Controller, type(controller)):
            for _x in range(0, number):
                self.controllers.append(copy.deepcopy(controller))

    def check(self, controllers=[], input=[]):
        if type(controllers) == list: #If Multiple Controllers Are Selected
            assert len(controllers) == len(input), "Must Give Valid Amount Of Input" #ensure correct amount of inputs

            for x in range(0, len(controllers)):
                if isinstance(controllers[x], (str, int, float)): #If Value Can Be Cast To Int
                    controllers[x] = int(controllers[x])

                    assert controllers[x] < len(self.controllers), "Must Choose Valid Controller To Check" #ensure controllers are correctly selected
                    self.controllers[controllers[x]].check(input[input])

        elif isinstance(controllers, (str, int, float)): #If One Selected And Castable To Int
            controllers = int(controllers)

            assert controllers < len(self.controllers), "Must Choose Valid Controller To Check" #ensure controllers are correctly selected
            
            if type(input[0]) == list:
                input = input[0] 
            assert type(input[0]) != list, "Must Format Inputs In A Valid Way"
            for x in input:
                assert isinstance(x, (str, int, float)), "Must Use Valid Inputs"
                

            self.controllers[controllers].check(input)