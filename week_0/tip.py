def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(cash):
    #Remove the $ prefix
    cash = cash.removeprefix("$")
    #Convert the string to a float
    float_cash = float(cash)
    return float_cash


def percent_to_float(perc_tip):
    #Remove the % suffix and convert to float
    perc_tip = float(perc_tip.removesuffix("%"))
    float_perc = float(perc_tip/100)
    return float_perc


main()
