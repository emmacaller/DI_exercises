#EX1

# output= bool(0)  # False
# print(output)
# x= (1==True)
# y=(1 == False)
# a = True + 4
# b = False + 10
#
# print("x is", x)
# print("y is", y )
# print("a:",a)
# print("b:", b)

#EX 2

# a = 10
# b= 5
# a = int(a)
# b= int(b)
#
# if a>b:
#     print("Hello World")
# else: print("a is smaller than b")

# EX 3

# user_input = input("insert a month from 1-12")
# user_input= int(user_input)
#
# if 3<=user_input<=5:
#     print("Spring")
# elif 6<=user_input<=8:
#     print("summer")
# elif 9<=user_input<=11:
#     print("Autumn")
# elif 12>=user_input<=2:
#     print("Winter")

# EX 4

# words = len("Lorem ipsum dolor sit amet, consectetur adipiscing elit")
#
# print(f"{words}")

# EX 5

# if we can detect A or a - print fail message
# if no A or a is detected - calculate how many characters in a message

user_input= input("print the longest sentance without the letter'A'")
length =len(user_input)

if "a" in user_input:
    print("You have a failed message ")
else:print(f"You have written {length} many letters")
