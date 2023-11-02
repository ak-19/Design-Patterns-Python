from Car import Car

from CarType import CarType
from CarVariation import CarVariation
from CarColor import CarColor

class Audi(Car):
    def __init__(self, carVariation, carColor):
        super().__init__(CarType.Audi, carVariation, carColor)