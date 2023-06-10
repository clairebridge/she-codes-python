#Function
#Functions we have seen before:
#input(), len(), int(), print()

# name = input("What is your name?")
# age = input("How old are you?")
# if age >= 18:
#     print("Welcome")
# else:
#     print("you cannot enter")


#Task seperation
# def ask_user_name():
#     name = input("What is your name?")
#     print (name)
#     return name

# def ask_user_age():
#     age = input("How old are you?")
#     if age >= 18:
#         print("Welcome")
#     else:
#         print("you cannot enter")

# ask_user_name()

#Parameters
# total = 0 #Global variable
# def add(number1, number2): #number1 =, number2 =
#     result = number1 + number2
#     return result

# answer = add(1,3)
# print (answer)
# print(result) #local variable - only exists within a function
# prompt = "Could I please have an integer?:"
# def get_integer ():
#     user_input = get_integer(prompt)
#     print (user_input)
#     return user_input


#Q1
# def get_integer():
#     prompt = input("Could I please have an integer?")
#     print (prompt)
#     user_input = int(prompt)
#     print(f"So your integer is {user_input}? Thanks!")
    
# get_integer()

#Q2
# def celcius_convert(current_temp):
#     convert = ((current_temp - 30) /2) 
#     print ("The temperature is",convert,"degrees in celcius.")

# celcius_convert(350)

# Q3
# def even_or_odd(random_number):
#     if (random_number % 2) == 0:  #% symbol = Modulo =  the remainder after dividing one number by another. So therefore, any number divided by 2, if remainder is 0, the number is even. More than one leftover, is odd.
#         print ("The number is even!")
#     else:
#         print ("The number is odd!")

# even_or_odd(13)

#Q4
# def total_cost(price, num_units):
#     total = float(price * num_units)
#     formatted_total = ("{:.2f}".format(total))
#     print ("$",str(formatted_total))

# total_cost(12.67,2)


