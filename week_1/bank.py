#Store greeting in a variable
#strip removes any leading whitespace
greeting = input("Greeting: ").strip()

#check if greeting is "hello", lower makes it case sensitive
if greeting[0:5].lower() == "hello":
    print("$0")

#check if the first letter is h
elif greeting[0].lower() == "h":
    print("$20")

#any other greeting
else:
    print("$100")
