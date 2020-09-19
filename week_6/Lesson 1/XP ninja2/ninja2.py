# EX 1
# cars_available = 100
# drivers_reg = 30
# passenger_today = 90
# empty_cars = cars_available - drivers_reg #70
#
#
# print(f"There are {cars_available} cars available and today we have\n{drivers_reg} drivers registered")

# EX 2

password = input("Please insert password")
password_length = len(password)
flag = 0

while True:
if  (len(password)<6):
    flag = -1
    break
elif  (len(password)>12):
      flag = -1
      break
elif not re.search("[$#@]", password):
     flag = -1
elif not re.search("[A-Z]", password):
    flag = -1
    break
elif not re.search("[a-z]", password):
     flag = -1
     break
elif not re.search("[0-9]", password):
     flag = -1
     break
else: flag = 0
     print("Valid password")
     break

if flag == -1
    print("Not valid password")







