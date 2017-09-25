# Exercise 1 Tutorial 2

def vowelCheck(character):
    
    if (character == "a" or character == "e" or character == "i" or character == "o" or character == "u"):
        
        print(character, "is a vowel")
    else:
        
        print(character, "is not a vowel")
        


inputChar = input("Enter a letter: ")

vowelCheck(inputChar)
