n = int(input("Enter the number:-"))
count=0
local_n = str(n)
for i in local_n:
    if(n % int(i) == 0):
        count+=1
print(count)
