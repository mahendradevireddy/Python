import re

print("Magic calculator")
run= True
previous=0

def fun():
    global run
    global previous
    equation=""
    if previous==0:
        equation=input("Enter equation")
    else:
        equation=input(str(previous))


    if equation == 'quit':
        print("Good bye folk")
        run= False
    else:
        equation=re.sub('[a-zA-Z" ",.:()]','',equation)

        if previous==0:
             previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)

            print(previous)


while run:
    fun()






