# # lists
#
# my_people = ["Tom", "Maria", "Mia", "Jack"]
#
# print(len(my_people)) # find length
#
# my_people.append("Russell") # too add to the list
# print(my_people)
#
# my_people.remove("Tom") # removes specific element
# my_people.pop(3) # removes elements at index 3
#
# print(my_people)
#
#break
#eg
 # for loop


# #manually
# pizza_toppings= []
# choice = input("What pizza toppings do you want? ( type STOP to stop)")
#
# choice = input("give me a topping, type 'Stop' to stop")
# pizza_toppings.append(choice)
#
# choice = input("give me a topping, type 'Stop' to stop")
# pizza_toppings.append(choice)
# print(pizza_toppings[0:1])
# print(pizza_toppings[0:2])

#in a loop # ex 1
# choice= input("What pizza toppings do you want?")
# pizza_toppings= [choice]

#
# while  choice != "stop":
#     choice = input ("give me a topping, (type 'Stop' to stop) ")
#     if choice != "stop":
#         pizza_toppings.append(choice)
# print(f"{pizza_toppings}")

#ex 2

# ask user for password, the password need to match these criterias
# should be minimum 6 characters long and maz 12
#if password doesnt match criteria display message error and ask again
#bonus: user only has 3 attemps to put right answer

# user_password = input("put in password")
# user_attemps = 0
#
# while user_attemps < 4:
#
#
# if len(user_password) <6
#     print("your password is too short")
# if len(user_password)>12
#     print("your password is too long")
#
#     user_attemps= user_attemps + 1


#for loop EX1
# ask how old they are one by one
#if they are below 16, remove from list

# family_members = ["mandy", "russell", "emma","francesca"]
#
# for member in family_members:
#     age_member=int(input(f"hello{member}how old are you?"))
#
#     if  age_member < 16:
#         family_members.remove(member)
#
# print(f"{family_members}")
#



