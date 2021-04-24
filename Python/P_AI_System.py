import copy
import Python.P_AI_Controller as Controller
import Python.P_AI_Decorators as Decorators



class System:
    controllers = []
    cycle = {}

    def __init__(self):
        pass

    @Decorators.inputlogger(inputs={"controller": (Controller.Controller, Controller.Controller()), "number": (int, str, float)})
    def addController(self, controller=Controller.Controller(), number=1):
        if type(controller) == type:
            for _x in range(0, number):
                self.controllers.append(controller())
        elif issubclass(Controller.Controller, type(controller)):
            for _x in range(0, number):
                self.controllers.append(copy.deepcopy(controller))
