# CREATIONAL DESIGN PATTERN: these are designs that deal with the creation of Objects

    
# Factory Pattern:    
# This pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. In this code, Product class is the object that needs to be created, and ProductFactory is the class that creates the object.

# Factory pattern example
class Product:
    def __init__(self, name, price): #
        self.name = name
        self.price = price

class ProductFactory:
    def create_product(self, name, price): # create_produc creates a new Product object with the given name and price.
        return Product(name, price)
    

# # Usage example
if __name__ == '__main__':
     # Factory pattern usage
    factory = ProductFactory()
    product = factory.create_product("Shoe", 50)
    print(product.name, product.price) # Shoe 50