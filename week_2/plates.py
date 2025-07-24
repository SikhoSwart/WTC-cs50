def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #plates may contain a max of 6 chars and a min of 2 chars
    if (1 < len(s) < 7) == False:
        return False

    #plates must start with at least two letters
    if (s[0:2].isalpha()) == False:
        return False

    for i in range(len(s)):
        #check where the first number begins
        if s[i].isdigit():
            break
    #The first number used cannot be a ‘0’
    if s[i] == "0":
        return False
    #numbers must come at the end
    if s[i].isdigit():
        if (s[i:].isnumeric()) == False:
            return False
    
    #No periods, spaces, or punctuation marks are allowed
    if (s.isalnum()) == False:
        return False

    return  True


main()
