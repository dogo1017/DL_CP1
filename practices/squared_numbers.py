#DL 1st, squared numbers practice

numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
print(f"\nOriginal: {numbers[1]}, Squared: ".join(list(map(lambda number: f"{number * number}", numbers))))