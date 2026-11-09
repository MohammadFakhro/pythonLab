#Name: Mohammad Fakhro
#Class: CSCI 1411-004
#Due Date: 10/20/2026
#Description: Takes a standard date format like '01/01/2008 and converts it into a string where the month is the name so 01 = January

#Status: Active

def month_to_name(month):

    match month:
        case '01':
            monthName = 'January'
        case '02':
            monthName = 'February'
        case '03':
            monthName = 'March'
        case '04':
            monthName = 'April'
        case '05':
            monthName = 'May'
        case '06':
            monthName = 'June'
        case '07':
            monthName = 'July'
        case '08':
            monthName = 'August'
        case '09':
            monthName = 'September'
        case '10':
            monthName = 'October'
        case '11':
            monthName = 'November'
        case '12':
            monthName = 'December'

            
    return monthName
    

def split_date(rawDate):
    month,day,year = rawDate.split('/')
    return month,day,year

def date_convert(DateInput):
    mm,dd,yyyy = split_date(DateInput)
    monthN = month_to_name(mm)
    longDateStr = monthN + ' ' +  dd + ', ' + yyyy
    return longDateStr

def main():
    DateInput = input("Enter date: ")
    print(DateInput, 'in long format is', date_convert(DateInput))

