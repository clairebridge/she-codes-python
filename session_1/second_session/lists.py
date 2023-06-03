#store multiple data points, can take different data types
#str, int, float, list
# print(digits)
# print(type(digits))

#Lists are index based which starts from 0.

#digits[5] Call a element in a list #IndexError: list out of range
#print(digits[-1]) Last element in a list
#slicing a list
#print(digits[3:5]) #Start (inclusive) and End index (exclusive)
#print(digits[0:5:2]) Third argument - lets you skip values on extraction... putting 2 will makde printed list 1, 3, 5
#print(len(digits)) Length of list

digits = [1,2,3,4,5]
# print(digits)
digits.append(6) #add value to list
# print(digits)
popped_element = digits.pop(0) #remove defined index, 
# print(popped_element)
digits[1] = 90

#print(digits)

letters = ['a','b','c','d',['Emily','Julie']]
#print(letters[4][0]) #Nested list - Get the first list, then get the first element from another list

# if 'a' in letters:
#     print('It is in the list')
# else:
#     print('It is not in the list.')



#Q1

# foods = ["orange","apple","banana","strawberry","grape","blueberry",["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]

# print(foods[0])
# print(foods[2])
# print(foods[-1])
# print(foods[0:3])
# print(foods[-3:10])
# print(foods[6][-1])

# Q2
# lyrics = [["Monica", "in my life"],["Erica", "by my side"],["Rita's", "all I need"],["Tina's", "what I see"],["Sandra", "in the sun"],["Mary", "having fun"],["Jessica", "here I am"]]
# fill_lyric = "A little bit of"

# print(fill_lyric, ' '.join(lyrics[0]),';')
# print(fill_lyric, ' '.join(lyrics[1]),';')
# print(fill_lyric, ' '.join(lyrics[2]),';')
# print(fill_lyric, ' '.join(lyrics[3]),';')
# print(fill_lyric, ' '.join(lyrics[4]),';')
# print(fill_lyric, ' '.join(lyrics[5]),';')
# print("A little bit of you makes me your man (ah!)")
# print("*trumpet solo*")

#Q3
# first_name = input("What is your first name?")
# middle_name = input("What is your middle name?")
# last_name = input("What is your last name?")

# full_name = []

# full_name.append(first_name)
# full_name.append(middle_name)
# full_name.append(last_name)

# print(' '.join(full_name))

#Q4

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

d.append(a)
d.append(b)
d.append(c)

print(d)

e = a + b + c

print(e)
