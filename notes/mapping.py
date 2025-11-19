#DL 1st, mapping notes

numbers = [345,43543,134,345,435,134,4,34,54,]
new_nums = []

"""for number in numbers:
    new_nums.append(number/3)

    print(new_nums)"""

def divide(num):
    return num/3

new_nums = map(lambda num: num/3, numbers)
print(list(new_nums))
for  num in new_nums:
    print(num)