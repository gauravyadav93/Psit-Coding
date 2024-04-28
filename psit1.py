#WAP to find greatest number among 3 number
#using if else ladder

num1 =int(input("enter first number"))
num2 =int(input("enter second number"))
num3 =int(input("enter third number"))
if num1>num2 and num1>num3:
    print("the number is greatest among all", num1)
elif num2>num1 and num2>num3:
    print("the number is greatest among all", num2)
elif num3>num1 and num3>num2:
    print("the number is greatest among all", num3)
else:
    print("wrong input")
            
        
        
