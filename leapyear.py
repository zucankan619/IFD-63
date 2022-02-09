def is_leapyear(year):
    remainder=year%4
    if remainder==0:
        print('Your year is a Leap Year')
    else:
       print('Your year is not a Leap Year') 


is_leapyear(2020)
is_leapyear(2022)
is_leapyear(2050)
is_leapyear(2012)