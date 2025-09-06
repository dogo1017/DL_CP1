#DL 1st, Stupid Proofing

while True:
    name = input("What is your full name (First and Last): ").strip()
    if " " in name:
        name = name.title()   
        break
    else:
        print("Please enter both first and last name.")


while True:
    phone = input("What is your phone number (10 digits): ").strip()
    digits = ""
    for ch in phone:
        if ch.isdigit():
            digits += ch
    if len(digits) == 10:
        phone = digits[0:3] + " " + digits[3:6] + " " + digits[6:10]
        break
    else:
        print("Phone number must have exactly 10 digits.")

while True:
    gpa = input("What is your GPA (0.0 - 4.0): ").strip()
    if gpa.replace(".", "", 1).isdigit():
        gpa = float(gpa)
        if gpa >= 0.0 and gpa <= 4.0:
            gpa = round(gpa, 1)
            break
        else:
            print("GPA must be between 0.0 and 4.0")
    else:
        print("Please enter a number for GPA.")

print(f"name: {name}")
print(f"phone: {phone}")
print(f"GPA: {gpa}")