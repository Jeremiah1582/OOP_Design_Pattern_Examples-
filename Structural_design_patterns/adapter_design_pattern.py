# structural 
# Structural design patterns are concerned with the composition of classes and objects.

# -------------------1) Adapter pattern: -----------------------------
# This pattern allows incompatible interfaces to work together by creating a middleman to translate one interface into another.

# explained: The code defines three classes. Target is the interface that the client expects to use, Adaptee is an existing class that the client cannot use directly, and Adapter adapts the Adaptee to the Target interface.

class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."



class Adaptee:#The Adaptee class has a method called specific_request that returns a specific string in reverse order.
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):#
    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()[::-1]}"
    #The Adapter class takes an Adaptee object as a parameter and has a method called request that returns a translated version of the Adaptee's specific_request method. The Adapter uses string slicing to reverse the string returned by the Adaptee and adds a prefix to indicate that it has been translated.


def client_code(target: Target) -> None:
    print(target.request())
    # client_code function takes a Target object as a parameter and calls its request method. 
    # the client_code function creates an instance of the Adapter class, passing in an Adaptee object, and passes that instance to the client_code function. 
    # When the client_code function calls the request method of the Adapter object, it receives a translated version of the Adaptee's specific_request method.
    

adaptee = Adaptee()
adapter = Adapter(adaptee)
client_code(adapter)  # Adapter: (TRANSLATED) Special behavior of the Adaptee.


