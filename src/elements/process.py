"""
Single process created from a function. Consists of:
- form:
    - input
    - label
    - function
- execution button
- message window
"""


class Process:

    @classmethod
    def from_function(function, name=None, version=None, description=None):
        slf = Process(
            function=function, name=name, version=version, description=description
        )
        slf.create_inputs()
        slf.create_logger
        return slf

    @classmethod
    def from_module(module):
        f = None
        n = None
        v = None
        d = None
        slf = Process(function=f, name=n, version=v, description=d)
        slf.create_inputs()
        slf.create_logger
        return slf

    def __init__(self, function, name=None, version=None, description=None) -> None:

        pass

    def create_inputs(self):
        pass

    def create_logger(self):
        pass
