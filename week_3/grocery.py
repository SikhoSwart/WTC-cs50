#empty dict to store grocery items
grocery = {}

while True:
    try:
        item = input("Item: ")
    except EOFError:
        break
    except KeyError:
        pass
    else:
        #if item already exists in dict, increase value by 1
        if item in grocery:
            grocery[item] += 1
        #add item to dict if it doesn't exist yet
        else:
            new = {item: 1}
            grocery.update(new)
#sort grocery list, forms new list
sort_grocery = sorted(grocery)
for i in sort_grocery:
    print(grocery[i], i.upper())

