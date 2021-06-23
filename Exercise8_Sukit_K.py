usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "admin"  and passwordInput == "1234":
    print("Done !")
    print("----- Shop -----")
    print("1. Apple 20")
    print("2. Mango 15")
    print("3. Banana 7")
    userSelected = int(input(">>"))
    if userSelected == 1:
        amount = int(input("Amount>> "))
        print("result = ",20*amount)
    elif userSelected == 2:
        amount = int(input("Amount>> "))
        print("result = ",15*amount)
    elif userSelected == 3:
        amount = int(input("Amount>> "))
        print("result = ",7*amount)
else:
    print("Error!")