# Prompt user to enter name of variable
name = input("camelCase: ")
#variable to store snakeCase string
snake = ""

#iterate through the string
for i in name:
    #check if a character is upperecase
    if i.isupper():
        #if a character is upper, add an underscore before it
        snake = snake + "_" + i
    else:
        snake = snake + i
#print the string in lowercase
print(snake.lower())
