# 1. INPUT AMOUNT: Ask how many students took the exam
students = int(input("How many students?\n"))

# 2. INITIALIZATION: Create a variable to store the sum of grades
total = 0

# 3. LOOP FOR GRADES: Ask each student's grade and add it to 'total'
for i in range(students):
    grade = float(input("Student grade:\n"))
    total = total + grade

# 4. CALCULATE & PRINT AVERAGE: Compute average after the loop ends
average = total / students
print(f"Average grade: {round(average, 1)}")

# 5. TEXT DESCRIPTION: Print result description based on the average range
if 0 <= average < 1:
    print("Bad result")
elif 1 <= average < 2:
    print("Weak result")
elif 2 <= average < 3:
    print("Average result")
elif 3 <= average < 4:
    print("Good result")
elif 4 <= average <= 5:
    print("Excellent result")