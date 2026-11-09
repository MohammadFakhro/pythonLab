#Author: Mohammad Fakhro
#Date: 10/13/2026
#Class: CSCI 1411-003
#Description: provides to random integer values, and you have provide the solution to the addition problem,
#Status: working

def main():
    import random
    number1 = random.randint (1, 10)
    number2 = random.randint (1, 10)
    print ('What is', number1, '+', number2, '?')
    answer = int(input ('? '))

    if answer == number1 + number2:
        print ('Your answer is correct')
    else:
        print ('Nope! The correct answer is', number1 + number2)
    
       
