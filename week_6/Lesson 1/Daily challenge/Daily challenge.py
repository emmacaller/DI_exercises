str = input("Please put in string 10 characters long")

first_letter = str[0]
last_letter = str[-1]
jumble_part = str[6] + str[3] + str[8]


if len(str)==10:
   print(f" Your first character is {first_letter} and your last charcter is {last_letter}")

i=0

while i<=10: # condition
    print(str[0:i])
    i= i+1
# print(str[0])
# print(str[0: 2])
# print(str[0: 3])
# print(str[0: 4])
# print(str[0: 5])
# print(str[0: 6])
# print(str[0: 7])
# print(str[0: 8])
# print(str[0: 9])
# print(str[0: 10])



print(f"This is your new password, {jumble_part}")