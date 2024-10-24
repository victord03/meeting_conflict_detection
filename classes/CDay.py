import numpy as np

class CDay:
    name: str
    timeline: dict

    def __init__(self, name=""):
        self.name = name
        self.timeline = {float(x):"" for x in np.arange(9, 18.5, 0.5)}

    def __str__(self):
        return f"{self.name}\n\t{self.timeline}"

    def __iter__(self):
        return iter(self.__dict__.items())