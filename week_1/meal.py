def main():
    #prompt user for time, call the convert function
    time = convert(input("What time is it? "))

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    #function to convert time in 24-hour format to float
    hours, minutes = time.split(":")
    #divide the minutes by 60, 1 hour = 60 minutes
    float_time = int(hours) + (int(minutes)/60)
    return float_time


if __name__ == "__main__":
    main()
