class Customer:
    Name = ""
    lastName = ""
    Age = 0
    def addCart(self):
        print("Added product to",self.Name,self.lastName,"'s cart")

customer1 = Customer()
customer1.Name = "Mawin"
customer1.lastName = "Meaw"
customer1.addCart()

customer2 = Customer()
customer2.Name = "Min"
customer2.lastName = "Mana"
customer2.addCart()

customer3 = Customer()
customer3.Name = "Hong"
customer3.lastName = "Pleng"
customer3.addCart()