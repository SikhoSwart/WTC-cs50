#prompt user to enter an expression
#use split to seperate the expression into three parts
expr = input("Expression: ").split()
x = int(expr[0]) #convert first number to int
y = expr[1] #the operation eg. +, -, *, /
z = int(expr[2]) #convert second number to int

#check each operator, y, and perform a calculation
match y:
    case "+":
        print(f'{x+z:.1f}')
    case "-":
        print(f'{x-z:.1f}')
    case "*":
        print(f'{x*z:.1f}')
    case "/":
        print(f'{x/z:.1f}')
