from Car import Car
from CarType import CarType

class Mercedes(Car):
    def __init__(self, carVariation, carColor):
        super().__init__(CarType.Mercedes, carVariation, carColor)