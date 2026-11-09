############################################

#Author: Mohammad Fakhro
#Class: CSCI 1411-004
#Due Date : 9/18/2026

#Description: Calculates box perimter, trim segments, trim cost,
#amount of trim wasted and cost of trim wasted, by just entering
#the length of the box in inches and the width of the box in inches 

#Status: Working

############################################

import math


def main():
    lenBox = eval(input('Enter the length of the box in inches: '))
    widBox = eval(input('Enter the width of the box in inches: ' ))
    
    Perimeter = (2*lenBox) + (2* widBox)
    
    trim = Perimeter / 12
    numSegments = math.ceil(trim)
    costTrim = numSegments * 1.88 #trim cost for 12'' inches is $1.88
    print('Your box has perimeter of ',Perimeter, ' sq inchs', sep = '')
    print('Number of trim segments that you have to buy',numSegments)
    print('Total Cost $',costTrim, sep = '')
    print('Amount of trim wasted ',numSegments - trim ,' sq inchs', sep = '')
    print('Cost of wasted trim $',((numSegments - trim) * 1.88), sep = '')
