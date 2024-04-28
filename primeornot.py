num = int(input("Enter Number:-"))
if(num > 1):
    for i in range(2, int(num/2)+1):
        if(num%i) == 0:
            print(num, "The number is not prime")
            break
    else:
        print(num, "The number is prime")
else:
    print("The number is not prime")
            
