menuList = []

def showBill():
    total = 0
    print("---- My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total += int(menuList[number][1])
    print("Total :",total,"THB.")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price(THB) :")
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()