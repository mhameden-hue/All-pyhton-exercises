# for loop to get rain amount for each month and calculate total rain amount

total = 0

for month in range(1, 13):
    # ask userfor rain amount of month
    rain = int(input('give rain amount of month:\n'))
    total = total + rain

# year avarage for rain
avarage =round( total / 12, 2)
print(f'year avarage for rain: {avarage} mm')