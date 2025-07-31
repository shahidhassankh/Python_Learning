class people:
    def __init__(self):
        self .__name="messi"
        self .__age=38
    def display (self):    
        print(self.__name,self.__age)
class department(people):
    def __init__(self):  
     ab=people()
     ab.display()