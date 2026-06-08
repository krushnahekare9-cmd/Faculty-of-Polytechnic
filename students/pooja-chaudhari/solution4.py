#problem 1
def greet(): 
    n=input("enter your name:")
    a=int(input("enter your age:"))
    print("Hi",n + "!Next year you will be",a+1)
greet()
#problem 2
num=10
unum=int(input("Gives a num set 1 to 10:"))
if unum<num:
    print("Low")
elif unum>num:
    print("High")
else:
    print("Correct")
    
        
