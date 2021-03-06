
def is_leap_year(n):
    '''
    Returns True if n is a leap year and False otherwise.

    is_leap_year: Nat -> Bool

    Examples:
       is_leap_year(1) => False
       is_leap_year(4) => True
       is_leap_year(100) => False
       is_leap_year(400) => True
    '''
    if n % 400 == 0:
        return True
    else:
        if n % 100 == 0:
            return False
        else:
            if n % 4 == 0:
                return True
            else:
                return False

def days_from_Jan_1(day2, month2, year2):
    day_start = int(1)
    month_start = int(1)
    jan_end_days = int(31)
    if is_leap_year(year2):
        feb_end_days = jan_end_days + int(29)
    else:
        feb_end_days = jan_end_days + int(28)
    mar_end_days = feb_end_days + 31
    apr_end_days = mar_end_days + 30
    may_end_days = apr_end_days + 31
    jun_end_days = may_end_days + 30
    jul_end_days = jun_end_days + 31
    aug_end_days = jul_end_days + 31
    sep_end_days = aug_end_days + 30
    oct_end_days = sep_end_days + 31
    nov_end_days = oct_end_days + 30
    if month2 == 1:
        return day2
    elif month2 == 2:
        return day2 + jan_end_days
    elif month2 == 3:
        return day2 + feb_end_days
    elif month2 == 4:
        return day2 + mar_end_days
    elif month2 == 5:
        return day2 + apr_end_days
    elif month2 == 6:
        return day2 + may_end_days
    elif month2 == 7:
        return day2 + jun_end_days
    elif month2 == 8:
        return day2 + jul_end_days
    elif month2 == 9:
        return day2 + aug_end_days
    elif month2 == 10:
        return day2 + sep_end_days
    elif month2 == 11:
        return day2 + oct_end_days
    else :
        return day2 + nov_end_days




def days_until_christmas(day, month, year):
    '''
    Returns xxxxx.

    Requires day to be a valid day in the month
    Requires 1 <= month <= 12

    '''
    if month==12 and day > 25 :
        days_to_year_end = days_from_Jan_1(31, 12, year) - days_from_Jan_1(day, month, year)
        year = year + 1
        days_to_xmas = days_to_year_end + days_from_Jan_1(25, 12, year)
        return days_to_xmas
    else:
        days_to_xmas =  days_from_Jan_1(25, 12, year) - days_from_Jan_1(day, month, year)
    return days_to_xmas

print(days_until_christmas(24, 12, 7503))
print(days_until_christmas(25, 12, 2019))
print(days_until_christmas(1, 1, 2020))
print(days_until_christmas(26, 12, 2019))
print(days_until_christmas(26, 12, 2020))

