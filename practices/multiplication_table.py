#DL 1st, multiplication table practice

rows = [1,2,3,4,5,6,7,8,9,10,11,12]
columns = [1,2,3,4,5,6,7,8,9,10,11,12]
column_values = []

for row in rows:
    for column in columns:
        column_values.append(column*row)
    print(*column_values)
    column_values.clear()



