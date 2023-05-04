# The Template Method is a behavioral design pattern that defines the skeleton of an algorithm in a base class, but lets subclasses override specific steps of the algorithm without changing its structure.

from abc import ABC, abstractmethod

# In this example, we have an abstract base class AbstractClass with two abstract methods primitive_operation1 and primitive_operation2. These methods are called by the template_method method, which defines the overall structure of the algorithm.

class AbstractClass(ABC):

    @abstractmethod
    def primitive_operation1(self) -> None:
        pass

    @abstractmethod
    def primitive_operation2(self) -> None:
        pass

    def template_method(self) -> None:
        self.primitive_operation1()
        self.primitive_operation2()

# We then have two concrete classes, ConcreteClass1 and ConcreteClass2, which inherit from AbstractClass and provide their own implementations of primitive_operation1 and primitive_operation2.
class ConcreteClass1(AbstractClass):

    def primitive_operation1(self) -> None:
        print("ConcreteClass1: primitive operation 1")

    def primitive_operation2(self) -> None:
        print("ConcreteClass1: primitive operation 2")

class ConcreteClass2(AbstractClass):

    def primitive_operation1(self) -> None:
        print("ConcreteClass2: primitive operation 1")

    def primitive_operation2(self) -> None:
        print("ConcreteClass2: primitive operation 2")


# Finally, we have a client_code function which takes an instance of AbstractClass and calls its template_method method. This allows the client to use any concrete implementation of AbstractClass without having to know which implementation it is using.
def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()
    
if __name__ == "__main__":
    print("Client: Testing ConcreteClass1...")
    client_code(ConcreteClass1())

    print("\nClient: Testing ConcreteClass2...")
    client_code(ConcreteClass2())
