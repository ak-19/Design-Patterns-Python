from unittest import TestCase as TC
from Factory import Factory

class ProductFactoryTest(TC):
    def setUp(self) -> None:
        self.factory = Factory()
        return super().setUp()
    
    def test_create_product1(self):
        product1 = self.factory.create_product(1)
        self.assertEqual("Product1", product1.get_name())

    def test_create_product2(self):
        product2 = self.factory.create_product(2)
        self.assertEqual("Product2", product2.get_name())

    def test_creation_of_unknown(self):
        with self.assertRaises(ValueError):
            product12 = self.factory.create_product(12)
            