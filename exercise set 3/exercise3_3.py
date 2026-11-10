#weekly work hours
hours=int(input('give weekly work hours:\n'))
#hourly wage
wage=float(input('give hourly wage:\n'))
#calculate,conditions
if hours<=40:
    total_wage=round((hours*wage),2)
else:
    Normal_hours=40
    extra_hours=hours-40
    total_wage=round((Normal_hours*wage)+(extra_hours*wage*1.5),2)

#print
print("Your weekly wage:",total_wage,'$')



