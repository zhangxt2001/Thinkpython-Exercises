from datetime import datetime
# This is about Friday the 13th after Jan.13 2023
def if_leap(year):
    '''(int)->Bool
if the inputted year is leap year then return True, otherwise
return False
>>> if_leap(1900)
False
>>> if_leap(2000)
True
'''
    if year//4==year/4:
        if year//100==year/100 and year//400!=year/400:
            return False
        return True
    else:
        return False
    
def num_of_days(year,month):
    '''
Returns the number of days between the 13th of the target
month and January 13th 2023, which happens to be a friday
thirteenth
'''
    future = datetime(year,month,13)
    now = datetime(2023,1,13)
    duration = future-now
    return duration.days


def if_13_friday(year,month):
    '''(int,int)->Bool
Checks if there is a friday 13th in a given
year and month. Returns True if there is a
Friday the 13th.
'''
    days_apart = num_of_days(year,month)
    while days_apart > 366:
        for i in range(2023,year):
            if if_leap(i):
                days_apart -= 366
            else:
                days_apart -= 365
    for i in range(2023,year):
        if if_leap(i):
            days_apart += 2
        else:
            days_apart += 1
    diff_week = days_apart - ((days_apart)//7)*7
    if diff_week == 0:
        return True
    else:
        return False


def print_13_friday(target_year):
    '''(int)->...
This function prints out all the 13th friday
from 2023-01-13 up to target-12-31
'''
    month = list(range(1,13))
    for i in range(2023,target_year+1):
        for j in month:
            if if_13_friday(i,j):
                date_str = str(i)+'-'+str(j).zfill(2)+'-'+str(13)
                print(date_str , 'is Friday the thirteenth')