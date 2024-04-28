from collections import defaultdict
def def_value():
    return "not a valid value"
d={}
size_d=int(input())
if size_d>16:
    print(def_value())
else:
    for i in range(size_d):
        d[i]=i**2
    print(d)
    
