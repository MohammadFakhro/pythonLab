#
# Name: Mohammad Fakhro
# Class: CSCI 1411-004
# Due Date: 9/15/2026
# Description: Create a algorithim that takes item name, quantity of the item, price, and sales tax rate and than output those variables, and then calculate and display the total amount in dollars, sales tax and grand total all in dollars

# Status: Active

def main():

    #prompt user for variables
    itemName = input('Enter item name: ')
    itemQuantity = eval(input('Enter quantity of the item: '))
    itemPrice = eval(input('Enter the price of the item: '))
    salestaxRate = eval(input('Enter the sales tax rate: '))

    # print variables
    print('Item name:', itemName)
    print('Quantity', itemQuantity)
    print('Price: ', '$', itemPrice, sep = '' )

    #calculate, and then round
    displayTotal = (itemQuantity * itemPrice)
    salestaxAmount = (displayTotal *( salestaxRate / 100))
    grandTotal = (displayTotal + salestaxAmount)
    
    #print calculations from befores, and use format for the decimals
    print('Total amount: ', '$',f' {displayTotal:.2f}', sep ='')
    print('Sales tax amount: ', '$', f'{salestaxAmount:.2f}',sep = '')
    print('Grand total: ', '$', f'{grandTotal:.2f}', sep ='')

