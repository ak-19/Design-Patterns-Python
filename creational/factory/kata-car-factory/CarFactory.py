from CarType import CarType
from CarVariation import CarVariation
from CarColor import CarColor

from Mercedes import Mercedes
from BMW import BMW
from Audi import Audi

class CarFactory:
    type_map = {
        CarType.Mercedes: Mercedes,
        CarType.BMW: BMW,
        CarType.Audi: Audi
    }
    def make_car(self, carType: CarType, carVariation: CarVariation, carColor: CarColor) -> None:
        if carType not in CarFactory.type_map:
            raise ValueError(f'Car type {carType} not supported')
        
        return CarFactory.type_map[carType](carVariation, carColor)