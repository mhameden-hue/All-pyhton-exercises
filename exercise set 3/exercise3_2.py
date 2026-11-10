# summer day's temperature as an integer
temp=int(input('give the temperature:\n'))
#chek temerature and print
if 0<=temp<=10:
    print('COLD')
elif 11<=temp<=15:
    print('CHILLY')
elif 16<=temp<=20:
    print("NORMAL TEMPERATURE")
elif 21<=temp<=25:
    print("WARM")
elif 26<=temp<=30:
    print("HOT")
