from Product1 import Product1
from Product2 import Product2

class Factory:
    
    @staticmethod
    def create_product(product_type: int):
        if product_type == 1:
            return Product1()
        elif product_type == 2:
            return Product2()
        else:
            raise ValueError(f'Unknown product type: {product_type}')