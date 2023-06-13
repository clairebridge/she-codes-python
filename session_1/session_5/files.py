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

population = []

with open(file="cats.csv", mode = "w") as my_file:
    csv_reader = csv.reader(my_file)
    for line in csv_reader:
        population.append (line)
for age_group in population:
    print(f"{age_group[0]} {age_group[1]}")