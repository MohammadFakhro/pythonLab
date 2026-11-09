############################################

#Author: Mohammad Fakhro
#Class: CSCI 1411-004
#Due Date : 9/22/2026

#Description: Takes a quantity and uses decision structure to calculate the discount percentage and amount and totalamount all in dollars and prints it out

#Status: Working

############################################


def main():
    quantity = input('Enter quantity: ')
    if(quantity.isnumeric()):
        quantity = int(quantity)
    else:
        print('Quantity must be numeric and positive')
        return

    discPerc = 0.00
    if(10 <= quantity <= 19):
        discPerc = 20.00
    elif(20 <= quantity <= 49):
        discPerc = 30.00
    elif(50 <= quantity <= 99):
        discPerc = 40.00
    elif(quantity >= 100):
        discPerc = 50.00
    else:
        discPerc = 0.00
        
        
    amount = quantity * 99
    discAmnt = amount * discPerc / 100.00
    totalAmnt = amount - discAmnt

    print(f'Discount Percentage is {discPerc:.2f}%')
    print(f'Discount Amount is ${discAmnt:.2f}')
    print(f'Total Amount is ${totalAmnt:.2f}')
    
