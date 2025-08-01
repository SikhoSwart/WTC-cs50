#while loop to prompt user again if exceptions are raised
while True:
    try:
        #prompt user for fraction formatted as X/Y
        frac = input("Fraction: ")
        #separate the fraction to get each integer
        frac = frac.split("/")
        #Store eeach integer in a variable
        x = int(frac[0])
        y = int(frac[1])
        #calculate the percentage
        perc = int((x/y)*100)

    #handle exceptions
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

    else:
            #handle cases where x>y and 'x/y' < 0
        if x > y:
            continue
        if (x/y) < 0:
            continue
        #1% or less remains, output E 
        if perc <= 1:
            print("E")
        #if 99% or more remains, output F
        elif perc >= 99:
            print("F")
        else:
            print(f'{perc:.0f}%')

        break
