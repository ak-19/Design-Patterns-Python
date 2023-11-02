from unittest import TestCase as TC

from enums import Color, Size
from Product import Product
from ColorSpecification import ColorSpecification
from SizeSpecification import SizeSpecification
from Filter import Filter


class FilterTest(TC):
    def setUp(self) -> None:
        self.filter = Filter()
        self.products = [
            Product("Apple", Color.GREEN, Size.SMALL),
            Product("House", Color.BLUE, Size.LARGE),
            Product("Car", Color.WHITE, Size.MEDIUM),
        ]
        return super().setUp()

    def test_filter_by_color(self):
        green_spec = ColorSpecification(Color.GREEN)
        green_products = [p for p in self.filter.filter(green_spec, self.products)]
        self.assertEqual(1, len(green_products))
        self.assertEqual("Apple", green_products[0].name)

    def test_filter_by_size(self):
        large_spec = SizeSpecification(Size.LARGE)
        large_products = [p for p in self.filter.filter(large_spec, self.products)]
        self.assertEqual(1, len(large_products))
        self.assertEqual("House", large_products[0].name)

    def test_filter_by_color_and_size(self):
        blue_spec = ColorSpecification(Color.BLUE)
        large_spec = SizeSpecification(Size.LARGE)
        blue_and_large_products = [
            p for p in self.filter.filter(blue_spec and large_spec, self.products)
        ]
        self.assertEqual(1, len(blue_and_large_products))
        self.assertEqual("House", blue_and_large_products[0].name)
