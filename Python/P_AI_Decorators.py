import functools

def inputlogger(inputs):
    def inputlogger_decorator(func):
        @functools.wraps(func)
        def wrapper_inputlogger(*args, **kwargs):
            return func(*args, **kwargs)
        
        wrapper_inputlogger.inputs = {}
        for x in inputs.keys():
            if type(inputs[x]) != tuple:
                inputs[x] = (inputs[x])
            wrapper_inputlogger.inputs[x] = inputs[x]

        return wrapper_inputlogger
    return inputlogger_decorator
