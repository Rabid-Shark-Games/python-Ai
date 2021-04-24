def inputlogger(func, inputs = {}):
    def function(*args, **kwargs):
        return func
    function.inputs = {}

    for x in inputs.keys():
        assert isinstance(inputs[x], (type, tuple)), "Incorrect Input Formatting In Decorator For " + func.__name__
        function.inputs[x] = inputs[x]

    return function