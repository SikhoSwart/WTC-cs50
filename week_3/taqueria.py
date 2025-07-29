#Food items dictionary
food = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#variable to store total amount
total = 0

while True:
    try:
        #title user input for case sensitivity
        item = input('Item: ').title()
        #add the food prices to the total
        total += food[item]
    except EOFError:
        break
    except KeyError:
        pass
    else:
        print(f'Total: ${total:.2f}')
