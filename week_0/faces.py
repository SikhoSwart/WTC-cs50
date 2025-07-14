def convert(string):
    conv_str = string.replace(":)", "\N{slightly smiling face}")
    conv_str = conv_str.replace(":(", "\N{slightly frowning face}")
    return conv_str

def main():
    user_in = input("Enter a string! ")
    print(convert(user_in))

main()
