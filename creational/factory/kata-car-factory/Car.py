from CarType import CarType
from CarColor import CarColor
from CarVariation import CarVariation

class Car:
    def __init__(self, type: CarType, variation: CarVariation, color: CarColor) -> None:
        self.type = type
        self.variation = variation
        self.color = color

    def __str__(self):
        return f'{self.type} {self.variation} {self.color}'