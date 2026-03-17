table = [
    [2, 4, 6],
    [3, 6, 10],
    [5, 10, 15]
]

for i, row in enumerate(table, start=1):
    first_num = row[0]
    valid = True
    for j in row:
        if j % first_num != 0:
            valid = False
            break
    if valid:
        print(f"Row {i}: Valid")
    else:
        print(f"Row {i}: Invalid")
