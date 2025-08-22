import sys
import PIL
from PIL import Image

length = len(sys.argv)

if length < 3:
    sys.exit("Too few command-line arguments")
elif length > 3:
    sys.exit("Too many command-line arguments")
else:
    #image files
    input_image = sys.argv[1]
    output_image = sys.argv[2]

if input_image.endswith((".png", ".jpg", ".jpeg")) == False:
    sys.exit("Invalid input")
if output_image.endswith((".png", ".jpg", ".jpeg")) == False:
    sys.exit("Invalid output")
#get the extension frim input
suffix = input_image.split(".")
#check if extensions match
if output_image.endswith(suffix[1]) == False:
    sys.exit("Input and output have different extensions")

else:
    try:
        #open images
        shirt = Image.open("shirt.png")
        muppet = Image.open(input_image)
        #get size of shirt.png
        width, height = shirt.size
        #resoze input to match shirt,pmg
        muppet = PIL.ImageOps.fit(muppet, (width, height))
        muppet.paste(shirt, shirt)
        muppet.save(output_image)

    except FileNotFoundError:
        sys.exit("Input does not exist")
