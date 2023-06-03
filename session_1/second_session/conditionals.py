#Boolean
name ='Claire'
age = '22'
height = '1.7'
my_variable = True
my_variable2 = False
# print(my_variable)
# print(type(my_variable))

# Boolean Expressions - Expressions produce the boolean value

# Comparison Operators
# == is equal to - compares if two things are equal
# != is not equal to - check if two things are not equal
# > greater than
# < less than
# >= greater or equal to
# <= less than or equal to
# print(5 > 3)
# print(3.5 > 6.3)
# print('Claire' == 'claire')

#Mathematical Operators - Addition, Division, Subtraction, Multiplication
#Boolean Operations- not (reversing value), and, or
is_sunny = True
is_warm = True

# print(not is_sunny)
# print(is_sunny != is_warm)
# print(is_sunny or is_warm)

# temperature = 18
# # syntax (grammer of code) / semantics (logic of code)
# if temperature < 18:
#     print("Weather is too cold!")
# elif temperature > 30: 
#     print("Weather is too hot!")
# else:
#     print("Weather is nice!")

#elif statement - only checked if first if is false
#multiple if statements - will be checked even if first if is true

#tasks

# Q1
# sara_has_helmet = True

# if sara_has_helmet == True:
#     print("Let's send it!")
# else:
#     print("No way, my brain is my moneymaker!")

# Q2

# sara_has_helmet = True
# rei_has_rope = False

# if sara_has_helmet == rei_has_rope == True:
# # if sara_has_helmet == True and rei_has_rope == True
#     print("Let's send it!")
# elif sara_has_helmet == rei_has_rope == False:
#     print("I guess let's just go hiking?")
# elif sara_has_helmet == True and rei_has_rope == False:
#     print("Who's unprepared now, Rei??")
# else:
#     print("No way, my brain is my moneymaker!")

#Q3

# light_colour = 'Amber'
# car_detected = True

# if light_colour == 'Red' and car_detected == True:
#     print("Flash!")
# else:
#     print("Do nothing!")

# Q4

# riders_height = input(f"How tall are you in cm?")

# if int(riders_height) > 120:
#     print("Hop on!")
# else:
#     print("Sorry, not today.")

# Q5

# user_name = input("What is your username?")
# pass_word = input("What is your password?")

# if user_name == 'lucyg' and pass_word == 'quartzgleam?1':
#     print("Logged in successfully.")
# else:
#     print("Access denied.")

#Q6

symbol_1 = '@'
symbol_2 = '.'
email = input("Enter your email:")

if symbol_1 in email and symbol_2 in email:
    print("Valid email!")
else:
    print("Invalid email!")

# Q7