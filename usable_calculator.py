def get_input(op):
    many = input("how many numbers would you like to "+op+"? ")
    if not many.isdecimal():
        print("no")
        get_input(op)
    num = int(many)
    numlist = []
    for i in range(num):
        acer = (input("enter a number(s): "))
        if not acer.isdecimal():
            print("no")
            get_input(op)
        numlist.append(int(acer))
    return numlist




def add():
    numlist = get_input("add")
    sun = 0     
    for j in numlist:
        sun = sun + j
    print (sun)
    
    
def subtract():
    numlist = get_input("subtract")
    diff = numlist[0]
    for x in range(1, len(numlist)):
        
        diff = diff - numlist[x]
    print(diff)
    
    
    
def divide():
    numlist = get_input("divide")
    div = numlist[0]
    for p in range(1, len(numlist)):
        div = div / numlist[p]
    print(div)
    
        
        
        
def multiply():
    numlist = get_input("multiply")
    prod = 1
    for k in numlist :
        prod = prod * k
    print(prod)
    
def goback():
    
    bob = input("would you like to go back to the start? (y/n)")
    if bob == "y":
        dothing()
    
        
    
    
def dothing():
    
    print("what do you want to do?")

    print("add\nsubtract\ndivide\nmultiply")

    choice = input()
    if choice == "add":
        add()
    elif choice == "subtract":
        subtract()
    elif choice == "divide":
        divide()
    elif choice == "multiply":
        multiply()
    goback()
dothing() 