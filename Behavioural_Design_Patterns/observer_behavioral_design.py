# The Observer pattern is used to create a messaging system where an observable object sends messages to all of its registered observers. 

# Observer Pattern:
# This pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. In this code, Observable class is the subject that can be observed, and Observer is the object that needs to be notified of any changes to the subject. Observable has three methods: register_observer, remove_observer, and notify_observers. Observer has one method called update that is called by Observable when it needs to notify the observers.

# Observer pattern example
class Observable: 
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received message: {message}")
        
        
# Usage example
if __name__ == '__main__':
        # Observer pattern usage
    observable = Observable()
    observer1 = Observer()
    observer2 = Observer()
    observable.register_observer(observer1)
    observable.register_observer(observer2)
    observable.notify_observers("Hello world!") # Received message: Hello world! (x2)
