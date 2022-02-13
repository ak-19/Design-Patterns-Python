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

print('Filter products to only green products')
def filter_by_color(color, prods):
    for p in prods:
        if p.color == color:
            yield p

for p in filter_by_color(Color.GREEN, products):
    print(f'{p.name} is {p.color}')


print('Filter products to only large products')
def filter_by_size(size, prods):
    for p in prods:
        if p.size == size:
            yield p

for p in filter_by_size(Size.LARGE, products):
    print(f'{p.name} is {p.size}')


