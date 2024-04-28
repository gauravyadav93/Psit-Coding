list1 = [12,10,20,2]
max1 = list1[0]
#print(max(list1))
for i in range(1,len(list1)):
    if max1<list1[i]:
        max1=list1[i]
print(max1)
       
