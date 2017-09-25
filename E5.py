# Exercise 5 - Tutorial 2

def smallest(a,b,c): 
    
    minimum = a
    
    if b < minimum: 
        minimum = b
    if c < minimum: 
        minimum = c
        
    return minimum    
    
    
def largest(a,b,c): 
    
    maximum = a
    
    if b > maximum: 
        maximum = b
    if c > maximum: 
        maximum = c
        
    return maximum       
    
def middle(a,b,c):
    
    if a > smallest(a,b,c) and a < largest(a,b,c):
        middle = a
    elif b > smallest(a,b,c) and b < largest(a,b,c): 
        middle = b
    else: 
        middle = c
    return middle    
    
    
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

print ("The smallest number is", smallest(n1,n2,n3))
print("The middle number is", middle(n1,n2,n3))
print("The largest number is", largest(n1,n2,n3))
