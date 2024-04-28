class Account:
    def __init__(self):
        self.acc_num = None
        self.acc_bal = None

    def current_balance(self,acc_num,cur_bal):
        self.acc_num = acc_num
        self.acc_bal = cur_bal

    def debit(self,amt):
        if(self.acc_bal >= amt):
            self.acc_bal -= amt
        else:
            print("insufficient funds")
    def credit(self,acc_obj,amt):
        acc_obj.acc_bal += amt

acc1 = Account()
acc2 = Account()
acc1.current_balance(123,50000)
acc2.current_balance(134,40000)
acc1.debit(1000)
           
        
