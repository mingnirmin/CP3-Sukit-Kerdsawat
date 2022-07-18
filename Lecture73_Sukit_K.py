systemMenu = {"ไก่ทอด": 35, "หมูทอด": 45, "ข้าวเปล่า": 10, "ปลาทอด": 40}
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
        menuList.append([menuName,systemMenu[menuName]])

print(menuList)
showBill()