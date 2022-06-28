def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
        UserSelect = menuSelect()
        if (UserSelect == 1):
            totalprice = int(input("Enter price: "))
            print(vatCalculator(totalprice))
        elif (UserSelect == 2):
            print("Price with vat =",priceCalculator())
        else:
            print("Try again")
            UserSelect = menuSelect()
    else:
        print("Login fail!")
        login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    count = int(input("How many item? : "))
    totalPrice = 0
    for i in range(count):
        price = int(input("Enter price: "))
        totalPrice += price
    return vatCalculator(totalPrice)

login()