from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet.getFonts()
# zero command-line arguments:
if len(sys.argv) == 1:
    #randomise font
    f = random.choice(figlet.getFonts())
    f = Figlet(font=f)

#two command-line arguments
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    try:
        f = Figlet(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
    
user = input("Input: ")
print(f.renderText(user))
