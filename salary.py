def net_salary(bs):
    hra = (35/100)*bs
    pa = (20/100)*bs
    res = bs+hra+pa
    return res
bs = int(input("enter the basic salary:-"))
print(net_salary(20000))
