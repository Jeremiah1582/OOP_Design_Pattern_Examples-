# structural 
#Structural design patterns are software design patterns that are concerned with the organization of classes and objects to form larger structures and to provide new functionality. They focus on the aggregation of classes and objects to create complex structures and define the relationships between them.

# ------------------2 Bridge Design Pattern -------------------
# This pattern decouples an abstraction (what it does) from its implementation (how it does it) so that both can vary independently.

# explained: In the main part of the code, two implementation objects are created (ConcreteImplementationA and ConcreteImplementationB), and two abstraction objects (Abstraction and ExtendedAbstraction) are created with different implementation objects passed to their constructors. The client_code function is then called with each of these abstraction objects to demonstrate that they behave differently depending on their implementation.

# The code defines four classes: 
from abc import ABC, abstractmethod

# Abstraction and ExtendedAbstraction are two classes that define the abstraction interface, which means the methods that a client will use to interact with an implementation.
class Abstraction:
    #constructor/initializer method
    def __init__(self, implementation: "Implementation") -> None: 
        self.implementation = implementation

    def operation(self) -> str:
        return f"Abstraction: Base operation with:\n{self.implementation.operation_implementation()}"


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return f"ExtendedAbstraction: Extended operation with:\n{self.implementation.operation_implementation()}"

# Implementation is an abstract class that defines the implementation interface. This interface contains methods that will be implemented by ConcreteImplementationA and ConcreteImplementationB.
class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

# ConcreteImplementationA and ConcreteImplementationB are two classes that provide different implementations for the methods defined in the implementation interface.
class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."

# The client_code function takes an abstraction object and calls its operation method, which in turn calls the operation_implementation method of the implementation object.
def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation())


implementation = ConcreteImplementationA()
abstraction = Abstraction(implementation)
client_code(abstraction)

implementation = ConcreteImplementationB()
abstraction = ExtendedAbstraction(implementation)
client_code(abstraction)