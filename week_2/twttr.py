#prompt user to enter a text
text = input("Input: ")
#variable to store text without vowels
new_txt = ""
#list of vowels
vowels = ["a", "e", "i", "o", "u"]

#iterate through text
for i in text:
    #check if a character is a vowel, if it is, skip it
    if i.lower() in vowels:
        continue
    else:
        new_txt += i
print(new_txt)
