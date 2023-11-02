from unittest import TestCase

from CarFactory import CarFactory
from CarType import CarType
from CarColor import CarColor
from CarVariation import CarVariation
from Car import Car


class CarFactoryTest(TestCase):
    def setUp(self) -> None:
        self.car_factory = CarFactory()
        return super().setUp()
    
    def test_make_mercedes(self):   
        mercedes: Car = self.car_factory.make_car(CarType.Mercedes, CarVariation.Sedan, CarColor.Black)        
        self.assertEqual(mercedes.type, CarType.Mercedes)
        self.assertEqual(mercedes.color, CarColor.Black)
        self.assertEqual(mercedes.variation, CarVariation.Sedan)
        self.assertEqual(str(mercedes), 'Mercedes sedan black')

    def test_make_BMW(self):   
        bmw: Car = self.car_factory.make_car(CarType.BMW, CarVariation.Cabriolet, CarColor.Silver)        
        self.assertEqual(bmw.type, CarType.BMW)
        self.assertEqual(bmw.color, CarColor.Silver)
        self.assertEqual(bmw.variation, CarVariation.Cabriolet)        
        self.assertEqual(str(bmw), 'BMW cabriolet silver')


    def test_make_Audi(self):   
        audi: Car = self.car_factory.make_car(CarType.Audi, CarVariation.Coupe, CarColor.White)        
        self.assertEqual(audi.type, CarType.Audi)
        self.assertEqual(audi.color, CarColor.White)
        self.assertEqual(audi.variation, CarVariation.Coupe)        
        self.assertEqual(str(audi), 'Audi coupe white')        