def vatCalculate(total):
    res = total+(total*0.07)
    return res

price = int(input("Price: "))
print(vatCalculate(price))