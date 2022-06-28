number = int(input("Enter number: "))
for i in range(number):
    print((number-(i+1))*" " + "*"*(2*(i+1)-1))