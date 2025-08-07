import emoji

#user input
word = input("Input: ")

#emojize the input
word = emoji.emojize(word,language='alias')
print(word)
