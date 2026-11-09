# Name: Mohammad Fakhro
# Class: CSCI 1411-004
# Due Date: 10/20/2026
# Description: Temperature conversion program, This program how to use functions in a Python
# program. It also shows how to use parameters to pass data
# to a function and return data from a function using a return
# statement.


# Status: Active

def Faren_to_Cels(Fahrenheit):
    return (Fahrenheit - 32) * (5.0 / 9.0)

def Faren_to_CelsList(FList):
    for i in range(len(FList)):
        fahrenheit = FList[i]
        celsius = Faren_to_Cels(fahrenheit)
        FList[i] = round(celsius,2)

def main():
    FahrenheitList = []

    for i in range(5):
        fahrenheit = float(input("Enter temperature in degree Fahrenheit: "))
        FahrenheitList.append(fahrenheit)

    Faren_to_CelsList(FahrenheitList)
    print("The converted temperature list")
    print(FahrenheitList)
