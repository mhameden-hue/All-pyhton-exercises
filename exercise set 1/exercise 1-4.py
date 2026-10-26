#total give minuets
minutes=int(input("give minuets:\n"))
#separate hours
hours=minutes//60
#separate minuets
minutes=minutes%60
#final result
print(hours, "h",'\t',minutes, "min", sep="")
