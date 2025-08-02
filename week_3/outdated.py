#list of months
mths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        # input date, in month-day-year order, strip whitespaces
        date = input("Date: ").strip()

        #handle date formatted like 9/8/1636
        if "/" in date:
            month, day, year = date.split("/")

        #hanndle date formatted like September 8, 1636
        elif "," in date:
            date = date.replace(", ", " ")
            month, day, year = date.split(" ")

            #switch the month to a number instead of a name
            month = mths.index(month) + 1
            
        #handle invalid days and months
        if int(day) > 31 or int(month) > 12:
            raise ValueError
        
    #handle exceptions
    except (NameError, KeyError, ValueError):
        pass

    else:
        print(f"{year}-{int(month):02}-{int(day):02}")
        break
