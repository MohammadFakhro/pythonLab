#
# Name: Mohammad Fakhro
# Class: CSCI 1411-004
# Due Date: 9/15/2026
# Description: Create an algorithim that takes user input for their first and last name and than generate a username and email address using concatanation

# Status: Active

def main():
    firstN = input('Enter your first name')
    lastN = input('Enter your last name')

    #conversion from uppercase to lowercase

    firstN = firstN.lower()
    lastN = lastN.lower()

    #concatenation

    username = lastN + firstN[0]
    emailAddr = firstN + '.' + lastN + '@ucdenver.edu'
    print(username)
    print(emailAddr)
