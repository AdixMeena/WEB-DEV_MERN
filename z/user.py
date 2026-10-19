user = input("ENTER YOUR USER_NAME:  ")

result =  len(user) <= 12 and user.find(" ") == -1 and user.isalpha()
if result is True:
    print("Valid")
else:
    print("NOt valid")


