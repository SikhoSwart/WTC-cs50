#prompt user to enter a file name
filename = input("File name: ").lower()

#check if file ends with .gif, .jpg, .jpeg, .png, .pdf, .txt or .zip 
if ".gif" in filename:
    print("image/gif")
elif ".jpg" in filename or ".jpeg" in filename:
    print("image/jpeg")
elif ".png" in filename:
    print("image/png")
elif ".pdf" in filename:
    print("application/pdf")
elif ".txt" in filename:
    print("text/plain")
elif ".zip" in filename:
    print("application/zip")
else:
    print("application/octet-stream")
