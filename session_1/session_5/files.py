# default values for open -- open(file="cats.csv", mode="r", encoding="utf-8")
import csv

# reading & opening a file
# with open(file="cats.csv", encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file)
#     for row in csv_reader:
#         print(row)

# writing a file
# with open(file="dogs.csv", mode = "w") as my_file:
#     csv_writer = csv.writer(my_file)
#     csv_writer.writerow(["hello"])


colour = []

with open(file="colours_20_simple.csv", mode="r", encoding="utf-8") as my_file:
    csv_reader = csv.reader(my_file, delimiter=",")
    for line in csv_reader:
        colour.append(line)

print(colour[0])

# for age_group in population:
#     print(f"{age_group[0]} * {age_group[1]}")
