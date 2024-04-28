class Customer:
    def __init__(self,Id,Name,Age,Wallet_balance):
        self.Id = Id
        self.Name = Name
        self.Age = Age
        self.__Wallet_balance=Wallet_balance
    def get_Wallet_balance(self):
        return self.__Wallet_balance
    def set_Wallet_balance(self,amount):
        if(0<amount and amount<1000):
            self.__Wallet_balance += amount
Cust_obj = Customer(101,"Gaurav",23,1000)
print(Cust_obj.Id)
print(Cust_obj.Name)
print(Cust_obj.Age)
print(Cust_obj.get_Wallet_balance())
Cust_obj.set_Wallet_balance(400)
print(Cust_obj.get_Wallet_balance())

            
            
