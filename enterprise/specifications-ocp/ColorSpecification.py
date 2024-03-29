from Specification import Specification

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    def is_satisfied(self, item):
        return item.color == self.color