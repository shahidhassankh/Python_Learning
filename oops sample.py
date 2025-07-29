"""class Laptops:
    def spec(self):
        print(self)
        self.RAM="4gb"
        self.Model="dell"
        self.developer="shahid"
Lap1=Laptops()
Lap1.spec()
print(Lap1.developer)"""

"""class Vehicles:
    def __init__(self,m,model):
        self.make=m
        self.model=model

class Car(Vehicles):
    def __init__(self,c,p,m,model):
        self.color=c
        self.power=p
        super().__init__(m,model)
c1=Car("Red","151 Bhp","2006","Kia Seltos")
print(c1.mak,c1.color)"""
        
        #mutlple inheritance

"""class father:
    def skills(self):
        print("father:carpenter,gardening" )

class mother:
    def skills(self):
        print("mother:cooking,caring")

class child(father,mother):
    def skills (self):
        father.skills(self)
        mother.skills(self)
        print("child:playing football")
c=child()
c.skills()"""

           #multilevel inheritance
#Grandparent (Base class)
      #↓
 #  Parent (Derived from Grandparent)
     # ↓
  # Child (Derived from Parent)


"""class grandfather:
    def vintageclub(self):
        print("grandfather:real madrid")
class father(grandfather):
    def modernclub(self):
        print("father:barcelona")
class child(father):
    def chappclub(self):
        print("child:kerala blasters")
c=child()
c.vintageclub()
c.modernclub()
c.chappclub()"""
   
         #Hierarchieal inheritance

     #Parent
     #/     \
#Child1     Child2


"""class india:
    def side(self):
        print("india is divided into two sides")
class southside(india):
    def south_looks(self):
        print("south india: rural and tropical")
class northside(india):
    def north_looks(self):
        print("north india:urban and polluted")
s=southside()
s.side()
s.south_looks()

n=northside()
n.side()
n.north_looks()"""

       