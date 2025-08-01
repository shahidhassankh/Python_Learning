from abc import ABC,abstractmethod
class parent (ABC):
    @abstractmethod
    def fun (self):
        pass
class child(parent):
    def display(self):
        print("who is the goat?")
    def fun(self):
        print("messsi is the goat")
ob=child()
ob.display()
ob.fun()       