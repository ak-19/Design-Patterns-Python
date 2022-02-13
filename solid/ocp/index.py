from enum import Enum

class Color:
    GREEN = 'Green'
    BLUE = 'Blue'
    WHITE = 'White'

class Size:
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'

class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

apple = Product('Apple', Color.GREEN, Size.SMALL)
house = Product('House', Color.BLUE, Size.LARGE)
car = Product('Car', Color.WHITE, Size.MEDIUM)

products = [apple, car, house]

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return Combine2Specification(self, other)

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    def is_satisfied(self, item):
        return item.size == self.size    

class Combine2Specification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2
    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)

class Filter:
    def filter(self, spec, items):
        for i in items:
            if spec.is_satisfied(i):
                yield i    

filter = Filter()

print('Filter products to only green products')
for p in filter.filter(ColorSpecification(Color.GREEN), products): 
    print(f'{p.name} is {p.color}')

print('Filter products to only large products')
for p in filter.filter(SizeSpecification(Size.LARGE), products):
    print(f'{p.name} is {p.size}')

print('Filter products that are large and blue')
blue_spec = ColorSpecification(Color.BLUE)
large_spec = SizeSpecification(Size.LARGE)
for p in filter.filter(blue_spec and large_spec, products):
    print(f'{p.name} is {p.size} and {p.color}')    


