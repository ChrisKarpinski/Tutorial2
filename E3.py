# Exercise 3 - Tutorial 2:


def isDivisible(numberOne, numberTwo): 
    
    if int(numberOne)%int(numberTwo) == 0:
        
        print (numberOne, "is divisible by", numberTwo)
    else:
        
        print (numberOne, "is not divisible by", numberTwo)
        

firstNumber = input("Enter the first number: ")

secondNumber = input("Enter the second number: ")

isDivisible(firstNumber, secondNumber)
