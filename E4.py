# Exercise 4 - Tutorial 2

def isDivisible(number): 
    
    for x in range (2,7): 
    
        if number%x == 0: 
        
            print(str(number), "is divisible by", str(x))
        
        else:
        
            print(str(number), "is not divisible by", str(x))
            
            
            
aNumber = int(input("Enter an integer: "))

isDivisible(aNumber)
