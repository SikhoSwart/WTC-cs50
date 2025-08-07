import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        #check if level is positive
        if level > 0:
           break

#randomise number
random_num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        #check if guess is positive
        if guess > 0:
            if guess < random_num:
                print("Too small!")
            elif guess > random_num:
                print("Too large!")
            else:
                print("Just right!")
                break
