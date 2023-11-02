from Car import Car
from CarType import CarType
from CarVariation import CarVariation
from CarColor import CarColor


class BMW(Car):
    def __init__(self, carVariation: CarVariation, carColor: CarColor):
        super().__init__(CarType.BMW, carVariation, carColor)