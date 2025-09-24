#DL 1st, letter grade practice
grade_percent = (input("What is the grade percentage of one of your classes: ")).strip().replace('%', '')
grade_percent = float(grade_percent)
grade_percent = round(grade_percent, 2)

if grade_percent >= 94:  
    print(f"Percent: {grade_percent}%\nLetter: A")
elif grade_percent >= 90 and grade_percent < 94:
    print(f"Percent: {grade_percent}%\nLetter: A-")
elif grade_percent >= 87 and grade_percent < 90:
    print(f"Percent: {grade_percent}%\nLetter: B+")
elif grade_percent >= 84 and grade_percent < 87:
    print(f"Percent: {grade_percent}%\nLetter: B")
elif grade_percent >= 80 and grade_percent < 84:
    print(f"Percent: {grade_percent}%\nLetter: B-")
elif grade_percent >= 77 and grade_percent < 80:
    print(f"Percent: {grade_percent}%\nLetter: C+")
elif grade_percent >= 74 and grade_percent < 77:
    print(f"Percent: {grade_percent}%\nLetter: C")
elif grade_percent >= 70 and grade_percent < 74:
    print(f"Percent: {grade_percent}%\nLetter: C-")
elif grade_percent >= 65 and grade_percent < 70:
    print(f"Percent: {grade_percent}%\nLetter: D")
elif grade_percent >= 60 and grade_percent < 65:
    print(f"Percent: {grade_percent}%\nLetter: D-")
else:
    print(f"Percent: {grade_percent}%\nLetter: F")