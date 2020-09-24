#EX1

# my_fav_numbers= { 6, 94 }
#
# my_fav_numbers.remove(94)
#
# print(f"{my_fav_numbers}")
#
# friend_fav_numbers={ 12, 65, 7}
#
# our_fav_numbers= my_fav_numbers|friend_fav_numbers
#
# print(f"{our_fav_numbers}")
#
# EX 2
# my_fav_numbers= ( 6, 94 )
# friend_fav_numbers=(12, 65, 7)
# our_fav_numbers= my_fav_numbers + friend_fav_numbers
# print(f"{our_fav_numbers}")\
#
# EX 3 floats
# defining a function to allow the range in a floats
# def range_float ( start, stop, step):
#     x =start
#     while x<= stop:
#         yield x
#         x = x + step
#
# float_pattern = range_float(1.5,5,.5)
#
# for i in float_pattern:
#     print(i)
#
# # EX 4
#
# for i in range(1,21):
#     print(i)
#
# EX 5

# user_input = input(" Put in a pizza topping of your choice , press quit to stop and ok now to start")
# list= [user_input ]
#
# while user_input != "quit":
#     user_input = input("give me a topping")
#     if user_input != "quit":
#         print(f"we will add {user_input} to your pizza")
#         list.append(user_input)
# print(f"{list}")
#
# EX 6

# family_list= [ 'emma', 'russell', 'francesca', 'mandy']
#
#
# for member in family_list:
#     family_age = int(input(f" {member}, what is your age?"))
#     if family_age <= 3:
#         print(' you ticket is FREE!')
#     elif 12 > family_age > 3:
#         print(" Your ticket is £10")
#     elif family_age > 12:
#         print("your ticket is £15")

# teanager_list= [' maria', 'tom', 'mia', 'milly', 'jack']
# allowed_list = [ ]
#
# for tean in teanager_list:
#     teen_age = int(input(f"{tean},What is your age?"))
#     if teen_age < 16:
#         print(" You are too young for this movie")
#     elif teen_age >= 16:
#         print(" you are allowed to watch this movie")
#         allowed_list.append(tean)
# print(f"{allowed_list}, you are allowed to watch this movie")

# EX 7

# user_list= [' maria', 'tom', 'mia', 'milly', 'jack']
#
# for user in user_list:
#     user_age = int(input(f" {user},How old are you?"))
#     if user_age <= 16:
#         user_list.remove(user)
# print(f" {user_list}")

# EX 8

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# print(f"{basket}")
# basket.remove("Blueberries")
# print(f"{basket}")
# basket.append("Kiwi")
# print(f"{ basket}")
# basket.insert(0,"Apples")
# print(f"{ basket}")
# count = basket.count("Apples"
# print(f"{ count}")

# Ex 9

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#
# while basket:
#     print(f"{basket}")
#     break


# EX 10 # while loop?

# my_list = [ 3,6,34,2,78,5,34,21]
#
# for number in my_list:
#     if number %2==0:
#         print(f"{number}")
#
# # use while loop for all even index.
# list1 = [10, 21, 4, 45, 66, 93]
# num = 0
#
# # using while loop
# while (num < len(list1)):
#
#     # checking condition
#     if num % 2 == 0:
#         print(list1[num], end=" ")
#
#         # increment num
#     num += 1
#
# EX 11
#
# for number in range(3,31,3):
#     print(f"{number}")
#
# my_list = [ 3, 6, 9, 12, 15, 18, 30]
#
# for number in my_list:
#     print(f"{number}")

# EX 12
# find all number in that range that divide by 7 and 5

# for number in range(1500,2701):
#     if (number%7==0) and (number%5==0):
#         print(f"{number}")