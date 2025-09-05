#DL 1st, idiot proof

def validate_name(name):
    name = name.strip().lower()
    if len(name) == 0:
        return False
    if name.count(" ") > 2 or name.count(" ") < 1:
        return False
    first_name, last_name = name.split(" ")
    if len(first_name) or len(last_name) == 0:
        return False
    name = first_name.capitalize() + " " + last_name.capitalize()
    return name


while True:
    name = input("What is your full name (First and Last): ")
    if not validate_name(name) = False
        name = validate_name(name)
        print(name)
        print(validate_name(name))
        break
    else:
        print("Please write a valid name")


name = input("What is your full name: ").strip().title
phone = input("What is your phone number : ")
GPA = input("What is your GPA: ")




print(f"name: {name}\n\nphone: {phone}\n\nGPA: {GPA}")