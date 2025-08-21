import sys

#line counter
count = 0
#number of command-line args
length = len(sys.argv)

if length < 2:
    sys.exit("Too few command-line arguments")
elif length > 2:
    sys.exit("Too many command-line arguments")
else:
    #python file
    py_file = sys.argv[1]

if py_file.endswith(".py") == False:
    sys.exit("Not a python file")

else:
    py_sys_argv[1]
    try:
        with open(py_file) as file:
            for line in file:
                #don't count spaces
                if len(line.strip()) == 0:
                    continue
                #don't count comments
                if line.strip().startswith("#"):
                    continue
                count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
print(count)

