class Variable():

    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return str(self.value)

    def value():
        doc = "The value property."
        def fget(self):
            return self._value
        def fset(self, value):
            self._value = value
        def fdel(self):
            del self._value
        return locals()
    value = property(**value())
