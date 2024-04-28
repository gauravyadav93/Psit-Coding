'''class super1:
    def __init__(self,num):
        self.num = num
class fact(super1):
    def __init__(self):
        super().__init__(4)
    def fact_num(self):
        fact = 1
        for i in range(1,self.num+1):
            fact = fact*i
        print(fact)
obj = fact()
obj.fact_num()'''


class super1:
    def __init__(self,num):
        self.num = num
class child(super1):
    def __init__(self):
        super().__init__(num)
    def armstrong(self):
        ori_num = num
        while(num!=0):
            rema = num%10
            arm += rem**3
            num = num/10
        if(ori_num == arm):
            print("num is armstrong")
        else:
            print("num is not armstrong")

num = int(input("enter num:"))
superobj=child(num)
superobj.armstrong()
        
