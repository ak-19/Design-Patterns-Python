from Specification import Specification

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    def is_satisfied(self, item):
        return item.size == self.size    