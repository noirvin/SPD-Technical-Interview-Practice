
'''
check if a given year is a leap year
assumption: input is going to be years from gregorian calendar
'''
def leap_check(year):
    # check if year is divisible by 4 and either indivisible by 100 or divisible by 400,
    # then it's leap year
    if year%4==0 and (year%100!=0 or year%400==0):

        return True
    # when it's a common year
    else:
        return False




print(leap_check(1987),leap_check(-1987),leap_check(2000),leap_check(1200))
