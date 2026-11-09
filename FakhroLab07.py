##########################################
#
# Name: Mohammad Fakhro
# Class: CSCI 1411-004
# Due Date: 9/29/2026
# Description: Find Composite and Prime Numbers by prompting the user for a number n > 2
# Status: Active
##########################################
import math
def main():
    error = True

    while (error):
        x = eval(input('Enter a number greater than or equal to 2 '))
        if( x < 2):
            print('Number must be greater than or equal to 2')
        if(x >= 2):
            error = False
        print('This Program generates and displays list of all prime and composit numbers between 2 and ',x)
    
        prime = []
        composite = []

        for j in range(2, x + 1):
            is_prime = True

        
            for i in range(2, int(math.sqrt(j) + 1)):
               
               if(j % i == 0):
                   is_prime = False
                   break

                
            if(is_prime):
                prime.append(j)
            else:
                composite.append(j)
            
                
                
        print('List of Prime Numbers:', prime)

        if(len(composite) == 0):
            print('There are no composite numbers in the range')
        else:
            print('List of Composite Numbers:', composite)
                  
                    

                   
            
        
    
        
