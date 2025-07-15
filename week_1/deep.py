#Store users answer in a variable
answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

#convert users answer to lowercase to make it case sensitive
answer = answer.lower()

#strip answer to get rid of eextra spaces
#use match tot test for each condition
#print "yes" for "42" or "Forty two", "no" otherwise
match answer.strip():
    case "42":
        print("Yes")
    case  "forty two" | "forty-two":
        print("Yes")

    case _:
        print("No")

