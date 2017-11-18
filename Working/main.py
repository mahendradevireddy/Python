import re

print("Magic calculator")
print("enter what you need for quit type 'quit':")
run= True
previous=0
while run:
    fun()

def fun():
    global run
    global previous
    print("Enter the equation")
    equation = input()
    if equation == 'quit':
        run= False
    else:
         previous=eval(equation)
         print(previous)





