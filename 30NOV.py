#WAP script to perform summation of value in dictionary
#Note:consider all values are integer value
#2. WAP to find frequency of each character in a string using dictionary.
D1 = {"A":34,"M":23,"N":2}
sum1 = 0
for key in D1:
    sum1 = sum1 + D1[key]
print(sum1)
#2 input : str1="ababsguwsasva"
#output :{a:2,B:2}
str1 ="ababanbmbcxz"
d1={}
for i in str1:
    if i in d1:
        d1[i]=d1[i]+1
    else:
        d1[i]=1  #here key is i and 1 is value.
print(d1)
d2 ={}
d2["a"]=1
print(d2)
        
    
    
