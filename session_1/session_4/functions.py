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
# def get_integer(prompt):
#     response = input(prompt)
#     return int(response)

# prompt = "Could I please have an integer?"
# user_input = get_integer("Could I please have an integer PLEASE?")
# print(f"So your integer is {user_input}? Thanks!")


#Q2
# def celcius_convert(current_temp):
#     convert = ((current_temp - 32) * (5/9)) 
#     print(f"The temperature is currently {convert}")
#     return convert

# assert celcius_convert(32) == 0.0
# assert celcius_convert(0) == -17.77777777777778
# assert celcius_convert(350) == 176.66666666666669

# Q3
# def is_even(random_number):
#     if (random_number % 2) == 0:  #% symbol = Modulo =  the remainder after dividing one number by another. So therefore, any number divided by 2, if remainder is 0, the number is even. More than one leftover, is odd.
#         return True 
#     else:
#         return False

# assert not is_even(13)
# assert is_even(26)
# assert is_even(0)

# if is_even(13):
#     print("The number is even!")
# else:
#     print("The number is odd!")

#Q478
def total_cost(price, num_units):
    total = float(price * num_units)
    formatted_total = ("{:.2f}".format(total))
    return (f"${str(formatted_total)}")

print(total_cost(4.25,3))
assert total_cost(4.25,3) == "$12.75"
assert total_cost(3.79,1) == "$3.79"
assert total_cost(1.49,7) == "$10.43"


