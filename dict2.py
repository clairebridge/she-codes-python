import csv
# QUESTION 2
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    }

with open(file="colours_865.csv", mode="r", encoding="utf-8") as my_file:
    csv_reader = csv.DictReader(my_file, delimiter=",",)
    for row in csv_reader:
        for colour in colour_counts:
            if colour.upper() in row["English"].upper():
                colour_counts[colour] += 1
                break

print(colour_counts)
# assert colour_counts == {'blue': 101, 'green': 77, 'yellow': 32, 'red': 51, 'purple': 20, 'orange': 23}
assert colour_counts == {'blue': 101, 'green': 78, 'yellow': 34, 'red': 51, 'purple': 20, 'orange': 26}
