#resource https://www.geeksforgeeks.org/generating-strong-password-using-python/
import random
import array

def createPassword(length):
    digitsAndSymbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    lowerCaseChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upperCaseChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    masterList = digitsAndSymbols + lowerCaseChars + upperCaseChars

    

    createdPassword = ""
    tempPassword = random.choice(digitsAndSymbols) + random.choice(lowerCaseChars) + random.choice(upperCaseChars)

    for _ in range(length - 3):
        tempPassword = tempPassword + random.choice(masterList)
        passwordList = array.array('u', tempPassword)
        random.shuffle(passwordList)

    for _ in tempPassword:
        createdPassword = createdPassword + _
    print(createdPassword)
createPassword(12)