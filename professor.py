import random

def main():
    n = get_level()
    score = 0
    for _ in range(10):
        #list to count number of invalid answers
        eee = ["eee"]
        x = generate_integer(n)
        y = generate_integer(n)
        while True:
            print(f"{x} + {y} =", end="")
            guess = int(input())
            if guess == (x + y):
                score += 1
                break
            elif guess != (x + y) and len(eee) != 3:
                print('EEE')
                #increase the length of eee
                eee.append("eee")
                continue
            else:
                print('EEE')
                print(f"{x} + {y} = {x + y}")
                break
    print(f'Score: {score}')


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            #check if level is 1, 2 or 3
            if level in [1, 2, 3]:
                return level


def generate_integer(level):
    n = level
    if n == 1:
        #1 digit numbers
        num = random.randint(0, 9)

    elif n == 2:
        #2 digit numbers
        num = random.randint(10, 99)

    else:
        #3 digit numbers
        num = random.randint(100, 999)

    return num

if __name__ == "__main__":
    main()
