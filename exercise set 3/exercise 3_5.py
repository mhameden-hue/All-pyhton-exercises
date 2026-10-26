#give amount of points
points=float(input('Exam points:\n'))
#conditions and prints
if 0<=points<=50:
    print('Grade:0')
elif 51<=points<=60:
    print('Grade:1')
elif 61<=points<=70:
    print('Grade:2')
elif 71<=points<=80:
    print('Grade:3')
elif 81<=points<=90:
    print('Grade:4')
elif 91<=points<=100:
    print('Grade:5')
    #if not in range(0-100)
else:
    print('NOT VALUABLE')