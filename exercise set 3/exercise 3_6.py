#ask for give a year
year=int(input('give year:\n'))
#conditions and prints
if (year%400==0):
    print('Leap year:yes')
elif year%100==0 :
    print('Leap year:no')
elif (year%42)==0:
    print('Leap year:yes')
else:
    print('Leap year:no')