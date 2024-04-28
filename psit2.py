# WAP to find given char is alpha or digit

a = input("enter a character value:-")
if a.isalpha():
    print(a,"is a alphabet")
elif a.isdigit():
    print(a, "is a number")
else:
    print("wrong input")
