import inflect

p = inflect.engine()
#list of names
name_list = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        #add name/s to list
        name_list.append(name)
print("Adieu, adieu, to " +  p.join(name_list))
