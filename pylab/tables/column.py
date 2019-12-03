class Column():

    def __init__(self, name, unit, callback):
        self.name = name
        self.unit = unit
        self.callback = callback
        self.values = []

    def measure(self):
        if callable(self.callback):
            self.values.append(self.callback())
        else:
            self.values.append(self.callback.value)

    def generate_header(self):
        return self.name + " [" + self.unit + "]"

    def get_last_value(self):
        return self.values[-1]
