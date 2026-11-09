############################################

#Author: Mohammad Fakhro
#Class: CSCI 1411-004
#Due Date : 9/22/2026

#Description: takes testscore and converts it into a letter grade and calculates average grade and prints both

#Status: Working

############################################




def main():
    test = ['','','']
    testScore = []
    for i in range(3):
        test[i] = input(f'Enter test score{i + 1}: ')
        if (test[i].isnumeric ()):
            testScore.append(int(test[i]))
        else:
            print("Error, test score must be numeric and positive")
            #close program if theres an error
            return
            
            


    average = ((testScore[0] + testScore[1]+ testScore[2])/3)
    print(f'Average test score is: {average:.3f}')


    
    if (average > 100.0):
        letterGrade = 'Undefined'
    elif (average >= 90.0):
        letterGrade = 'A'
    elif (average >= 80.0):
        letterGrade = 'B'
    elif (average >= 70.0):
        letterGrade = 'C'
    elif (average >= 60.0):
        letterGrade = 'D'
    elif ( average < 60.0):
        letterGrade = 'F'

    print('Your letter grade is: ',letterGrade)
        
        
        
