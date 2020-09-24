#1
# Write a program that counts the number of element for a list, without the len function.

# name_list=['Alex','Mike','Dylan','Yossi']
# count =0
# for name in name_list:
#     count += 1
#     print(count)
#

#2
#Write a program that prints every name that starts by 'a'

# name_list=['Alex','Mike','Dylan','yossi','Alan']
#  if 'A' is in name_list:
#      print("Yes")



#3
#Write a Python program that prints all the numbers from 0 to 10 except 3 and 6
#
# for x in range(0,11):
#     if(x==3) or (x==6):
#         continue
#     print((x))

#4
# You have a list of users, and you want to remove every user that is below 16 years old.
# Write a program that ask every user their age, and if they are less than 16 years old,
# remove them from the list.
# At the end, print the final list.

# user_list = ["mandy", "russell", "emma","francesca"]
#
# for user in user_list:
#     user_age= int(input(f"Hi {user},What is your your age"))
#     if user_age < 16:
#         user_list.remove(user)
#
# print(f"{user_list}")
#  #5
# Use a FOR loop to print the numbers from 1 to 20, inclusive.Exercise (easy)
# Make a list of the numbers from one to one million, and then use a FOR loop
# to print the numbers.
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

# for x in range(0,21):
#     print(x)

# number_list = [ 1, 78, 500, 89, 345, 100030]
#
# for number in number_list:
#     print(number)

# EX 5
# Make a list of the numbers from one to one million, and
# then use min()and max() to make sure your list actually
# starts at one and ends at one million. Also, use the sum()function
# to see how quickly Python can add a million numbers .

# number_list = [ 1, 78, 500, 89, 345, 100030]
#
# sum_numbers = sum(number_list)
# print(f"{sum_numbers}")

# EX 6
# Write a program that returns the index of the first occurrence of an item in a list

# my_list = [ "apples", "pears", "smoothie", "russell", "emma", "pears", "tobacco"]
#
# first_occurrence= my_list.index("pears")
# print(f"{first_occurrence}")

# ex 6
# Write a little program that concatenate two lists together without using the + sign.

# my_list = [ "apples", "pears", "smoothie", "russell", "emma", "pears", "tobacco"]
# my_list2 = [ "apples", "pears", "smoothie", "russell", "emma", "pears", "tobacco"]
#
# ful_list =my_list + my_list2
# print(f"{ful_list}")

#ex 7
# Create a board as following by using for loops:
#     X
#     XX
#     XXX
#     XXXX
#     XXXXX
#     XXXXXX
#     XXXXX
#     XXXX
#     XXX
#     XX
#     X

#
# rows = 6
# for num in range(rows):
#     for i in range(num):
#         print("x", end = " ")
#     print(" ")
#
# rows = 4
# for num in range(4,0, -1):
#     for i in range(0, num):
#         print('x', end=' ')
#     print(" ")

# 8 Make a list of the multiples of 3 from 3 to 30.
# Use a forloop to print the numbers in your list.Exercise (medium)

# for num in range(3,31,3):
#     print(num)

# vowels = ['a', 'e', 'i', 'u']
#
# vowels.insert(3, 'o')
#
# print(vowels)

# EX 9
# Write a program that insert an item at a defined index.
# 1.	Take a list of popular car manufacturers
# 2.	Paste it into your code, and store it in a variable.
# 3.	Convert it into a list using Python (don’t do it by hand!)
# 4.	Print out a message saying how many manufacturers/companies are in the list
# 5.	Print the list of manufacturers in reverse/descending order (Z-A)
# 6.	Using loops or list comprehension:
# 7.	Find out how many manufacturers’ names have the letter ‘o’ in them.
# 8.	Find out how many manufacturers’ names do not have the letter ‘i’ in them
# 9.	Print the above information out with meaningful output messages.
# 10.	(Bonus: There are a few duplicates in the list:
# 11.	Remove these programmatically. (Hint: you can use sets to help you)
# 12.	Print out the companies without duplicates, in a comma-separated list with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, ...”), and also print out a message saying how many companies are now in the list).
# 13.	(Bonus: print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name)

# car_makes = "honda, toyota, ford, BMW, toyota "
#
# car_list=car_makes.split()
# lengh=len(car_list)
# print(f' There are, {lengh}, many companies in this list')

# car_list.sort(reverse=True)
# print(f"{car_list}")
#
# my_set = {"honda", "toyota", "ford", "BMW", "toyota" }
# length_set =len(my_set)
# print(f" {my_set}, There are {length_set} companies in this list")
#
# my_list =list(my_set)
# print(f"{my_list}")
#
# my_list.sort()
# print(f"{my_list}")
# Exercise (hard)
# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *



#
#
