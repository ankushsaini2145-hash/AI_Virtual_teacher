user=input ("Enter Username:")
password=input("Enter Password:")
user=user.lower()
if user=="admin":
    if password=="123":
        print ("Succesful Login")
    else:
        print ("Password is Wrong")
else:
    if user=="admin":
        print ("login")
    else:
        print ("Wrong details")