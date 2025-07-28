"""a,b=10,0
try:
    c=a/b
    print(c)
except Exception:
    print ("please enter a valid number")  

a,b=10,0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("eneter valid number")
except NameError:
    print("value not found")
except Exception as e:
    print("error",e)
print("program executed")        
"""


"""while True:
   try:
    a,b=map(int,input("enter you numbers :") .split())
    try:
     c=a/b
     print(c)
    except ZeroDivisionError:
     print("eneter wrong number ,try again ")
   except Exception as e:
    print("not found")"""
     



