class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return Combine2Specification(self, other)
    
class Combine2Specification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2
    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)