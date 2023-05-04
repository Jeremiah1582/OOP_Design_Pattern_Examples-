# CREATIONAL DESIGN PATTERN: these are designs that deal with the creation of Objects

# Singleton Pattern:
# This pattern ensures that a class has only one instance, and provides a global point of access to that instance.   

class Singleton:
    _instance = None #In this code, Singleton class has a private static variable _instance that holds the singleton instance of the class.
    def __new__(cls):
        if not cls._instance: #When a new instance of the class is requested, __new__ method checks whether the _instance variable is already set,
            cls._instance = super().__new__(cls) #and if not, creates a new instance using super().__new__(cls) method.
        return cls._instance
    
# # Usage example
if __name__ == '__main__':
    # Singleton pattern usage
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(singleton1 == singleton2) # True
    