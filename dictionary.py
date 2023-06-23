import csv


# lists
# numbers = [1,2,3]
# numbers[0]
# Dictionary
# Keys are unique
# Keys can only be immutable data types
# Immutable - String, integers, floats, booleans
# FORMAT == "Key": Value,
# student_phonebook = {
#     "Melissa":1121, 
#     "Claire":1245, 
#     "Lockie":2334, 
#     "Tom":2499
#     }

# print (student_phonebook)
# Change a value == student_phonebook["Claire"] = 5443
# print(student_phonebook["Asli"])
# Add a new value == student_phonebook["Anthony"] = 5534
# Delete a value == del student_phonebook["Lockie"]
# print (student_phonebook)
#print (type(student_phonebook))

# Iterate all the key value pairs
# for key in student_phonebook:
#     print(key, student_phonebook[key])

#Iterate all the values in a dictionary
# for value in student_phonebook.values():
#     print (value)

# for example in student_phonebook.items():
#     print(example)

# for key, value in student_phonebook.items():
#     print(key,value)



#QUESTION 1

# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Coffee": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
#     }

# total_cost = []

# for item, cost in groceries.items():
#     quantity = input(f"How many packets of {item} would you like? ")
#     quant = int(quantity)
#     value = float(cost * quant)
#     total_cost.append(value)
#     formatted_value = "{:.2f}" .format(sum(total_cost))
#     #dad example formatted_value = f"{sum(total_cost):.2f}"
# print(f"Your total is $ {formatted_value}")

# QUESTION 2
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    }

colour_list = []
with open(file="colours_865.csv", mode="r", encoding="utf-8") as my_file:
    csv_reader = csv.reader(my_file, delimiter=",")
    for line in csv_reader:
            colour_list.append(line)

blue_count = []
green_count = []
yellow_count = []
red_count = []
purple_count = []
orange_count = []

for type in colour_list:
    if "Blue" in (type[2]):
        blue_count.append(True)
    elif "Green" in (type[2]):
        green_count.append(True)
    elif "Yellow" in (type[2]):
        yellow_count.append(True)
    elif "Red" in (type[2]):
        red_count.append(True)
    elif "Purple" in (type[2]):
        purple_count.append(True)
    elif "Orange" in (type[2]):
        print(f"{type[2]}")
        orange_count.append(True)
    else:
        pass
    
colour_counts["blue"] = (sum(blue_count))
colour_counts["green"] =(sum(green_count))
colour_counts["yellow"] =(sum(yellow_count))
colour_counts["red"] =(sum(red_count))
colour_counts["purple"] =(sum(purple_count))
colour_counts["orange"] =(sum(orange_count))

# print (colour_counts)
# print (colour_list)


#  in line test ---- assert colour_counts['blue'] == 101
assert colour_counts == {'blue': 101, 'green': 78, 'yellow': 34, 'red': 51, 'purple': 20, 'orange': 26}
# print (colour_list[1][2])
# print ("Blue" in colour_list[1][2])







