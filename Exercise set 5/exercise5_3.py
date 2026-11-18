# use math moudle to calculate area
import math

# input radius
while True:
    radius = int(input('Give circle radius: '))

# calculate area
    area = math.pi * radius ** 2
    area = round(area, 2)
# print area
    print(f'The area of the circle is {area}')

    answer = input('Do you want to continue? (y/n): ')

    if answer == 'n':
        break