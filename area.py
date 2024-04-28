#create a function to calculate area of circle

def area_circle(r):   # the highlighted part is known as function signature and r is called formal parameters
    result = 3.14*r*r
    return result

r =int(input("enter the radius"))

print(area_circle(r)) # here r is called actual parameters

    
