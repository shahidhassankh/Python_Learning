
print("===to do list=== \n" "1: add task\n" "2: show task\n" "3: mark task as done\n" "4: exit\n") 
num1=int(input("choose your choice :"))
if num1==1:
    num2=int(input("how many task you want to add :")) 
    print(num2)
    for i in range(num2):
       num3=input("enter the task names: ")
       print(num2)
       print("tasks are  added")

