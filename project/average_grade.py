# DL 1st, average grade practice

class_grades = {}

classes = int(input("How many classes do you have: \n"))

num = 1

for i in range(0,classes): 
    grade = float(input("What is your grade in one of your classes: "))
    class_grades[num] = {'grade': grade}
    num = num + 1

total_grade = 0
count = 1

for i in class_grades:
    total_grade = total_grade + class_grades[count]['grade']
    count = count + 1
average = total_grade / classes
result = round(average,2)
print("The average grade of all of your classes is:", result)