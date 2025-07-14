"""
list

stud=[26,50,40,30]
for m in stud:
   # print(m)
   #print(m,end=" ")"""
   
"""
tuple

t=(3,6,8,10)
for s in t:
    print(s)"""


"""
set
num={7,8,9,10}
for l in num:
    print(l)"""

"""t={"shahid":30,40:20,"kochi":14}
#for d in t:
   # print(t.values())
   #print(t.items())
for k,val in t.items():
     #print(k,val)
     #print(k)
     #print(val)
"""

"""my_list=(4,6,8,10,15)
print(list (enumerate (my_list,5)))


my_list=(4,6,8,10,15)
print(tuple (enumerate (my_list,5)))

"""

"""my_list=(4,6,8,10,15)
print(set (enumerate (my_list,5)))"""



"""my_list=(4,6,8,10,15)
print(dict (enumerate (my_list,5)))"""


"""for k in range(1,11):
    print(k)"""

"""
for k in range(1,11,2):
    print(k)"""

"""num=int(input("enter the number :"))
for k in range(1,11):
    print(f"{k} + {num}  = {k+num}")

"""

"""num=int(input("enter the number :"))
for k in range(1,11):
    print(f"{k} * {num}  = {k*num}")
"""

"""
numb=int(input("enter your number:"))
for numb in range(1,17):
    if numb%2==0:
      print(numb)
"""        

"""fruits=["apple","orange","anaar","pineapple"]
for fruit in fruits:
    if fruit.startswith("a"):
        print(fruit)
"""

"""fruits=["Apple","orange","anaar","watermelon"]
for f in fruits:
     if f.lower()[0]=="a":
          print(f)"""

"""vowels=["aeroplane","orange","was","ear","nose","eyes","india","under"]
for v in vowels:
    if v.lower()[0] in "aeiou":
        print(v)"""

"""for num in range(1,11):
    if num==9:
        continue
    print(num)"""

"""for num in range(1,11):
    if num==8:
        break
    print(num)"""

"""for r in range(1,4):
    for j in range(1,r+1):
        print(j,end=" ")
    print("")"""
     
"""count=2
while count<=10:
    print(count)
    count+=1"""
    
"""num=int(input("enter your number :"))
count=1
while count<=10:
    print(f"{num} * {count}= {num*count}")
    count=count+1"""


while True:

 num=int(input("enter the first number :"))
 num1=int(input("enter the second number :"))
 print("eneter your choice : \n" "1.addition\n" "2.subtraction\n" "3.multiplication\n" "4.division\n")
 num3=int(input("enter your choice :" ))
 if num3==1:
  print(num+num1)
 elif num3==2:
    print(num-num1)
 elif num3==3:
    print(num*num1)
 elif num3==4:
    print(num/num1)     
 stud=str(input("do you want to continu : yes or no :"))
 if stud.lower()!="yes":
    break

    
    










