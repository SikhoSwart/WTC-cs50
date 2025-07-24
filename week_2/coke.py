#set total amount to 0
total = 0

while True:
    #prompt user for coin
    coin = int(input("Insert Coin: "))
    #use only the accepted denominations
    if coin==25 or coin==10 or coin==5:
        total += coin
        #variable for amount due
        due = 50 - total

        if total < 50:
            print("Amount Due: ", due)

        else:
            #Calculate change owed
            change = total - 50
            print("Change Owed: ", change)
            break
    else:
        print("Amount Due: 50")
        break
