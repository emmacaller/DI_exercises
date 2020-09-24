# # rick_dict = {
# #     'first name':'Rick',
# #     'last name':'Sanchez'
# # }
# # print("The last name of rick is:", rick_dict['last name'])
#
# # my_list = [ 1,2,3,"rick", 5]
# #
# # obj=" "
# # i=0
# #
# # while obj != "rick":
# #     obj= my_list[i]
# #     print(obj)
# #     i+=1
# #     if obj=="rick":
# #         break
#  # DICTIONARY EXAMPLES
#
# my_animals = {
#     "firstpet": "Fish",
#     "secondpet": "dog",
#     "thirdpet": "horse",
# }
#
# rose = {
#     "height": 50,
#     "petals":20,
#     "color":"pink",
#     "thorns": True
# }
#
# rose = {
#     "height": 50,
#     "petals":20,
#     "color":"pink",
#     "thorns": True
# }
#
# # print(rose["height"])
#
# print(f"{rose['height']} is the height and {rose['petals']} number of petals")
#
# pets_flowers = [my_animals,rose]
# print(f"{pets_flowers}")
#
# #modify data
#
# rose["color"] = "yellow"
# rose['shape'] = "vertical" # if you use a key that doesnt exist it will create it

# print(f"My favorite pet was my second pet which was my {my_animals['secondpet']} and my fave flower was rose because it was {rose['color']}")
# print(f"My favorite pet was my second pet which was my {my_animals['thirdpet']} and my fave flower was rose because it was {rose['color']}")
#
# i=1
# print("my fave flowers are:")
# for flower in pets_flowers
#     print(f"My favorite pet was my second pet which was my {i['thirdpet']} and my fave flower was rose because it was {rose['color']}") ")
#     i+=1
# SCREENSHOT TO CLARIFY


# for item in rose.keys(): #will always see the keys
#     print(item, "-->", rose[item]) #to print keys next to values
#
# #UNPACKING
# # unpacking a container means splitting in to variables
#
#
# products={
#     "computer":1000,
#     "iphone": 2000,
#     "Apple wheels":5000,
#     "P55": 600
# }
# #ask the user how much money does he want to spend
# # #print every item that he can affort
# #
# # user_money =int(input(" how much money do you want to spend?"))
# # print("you can affort:")
# #
# # for product, price in products.items():
# #     if price<=user_money:
# #         print(f"{product}(£[price])")
#
# #make a dictionary called contact and add three of your friends with their phone number
#
# contacts = {
#     "rick": "059768635",
#     "morty": "058978676",
#     "summer":"058976534"
# }
# # add another person manually
#
# contacts['emma']= '059873657'
# # print(contacts)
#
# #write a loop that print every conntact with his number
#
# for name, phone_nb in contacts.items():
#     print(f"{name}:\t {phone_nb}")
#
# #write a code that searches if a given name exists in the contacts
# searched_name ="rick"
#
# for name in contacts.keys():
#     if name.lower == searched_name.lower():
#         print(f"{ We have had that that{name} before, this the same user?")

    # if searched_name in contacts.keys():
    #     print()

#write a code that searches if a given number exists in contact, if it exists then print his name
# searched_number = '059873657'
# for name, phone_nb in contacts.items():
#      if phone_nb == searched_number:
#         print(f"{searched_number} We already have this number saved {phone_nb}it belongs to {name}")

#given another dictionary of contacts, add it to your dictionary

# rick_contacts = {
#     "Hannah" : "-587876369",
#     "jessica": " 0787654354"
# }
#  for name, phone_nb in rick_contacts.items():
#      contacts[name] =phone_nb
#
# # count how many contacts are in  your dictionary
# nb_of_contacts =len(contacts.keys())
# print(f" There are {nb_of_contacts} contacts")
#
# # contacts.update(rick_contacts) #a fuction to do this for you
#
# #print the contacts in alphabetic order with their number
#
# sorted_contacts = sorted(contacts.keys())
# for contact in sorted_contacts:
#     print(f"{contact} \t -> {contacts[contact]}")

# given two dicts
products_wallmart = {
    "Computer": 1000,
    "Iphone": 2000,
    "Apple Wheels": 5000,
    "PS5": 600
}
products_amazon = {
    "Samsung Galaxy": 800,
    "Computer": 1500,
    "Apple Wheels": 3000,
    "XBox": 600,
}

# print only the products that exist in both dictionaries, and the lowest price
# output should be:
# compuer(1000)
# Apple Wheela (3000)

for product in products_wallmart.keys():
    if product in products_amazon.keys():
        lowest_price = min(products_wallmart[product], products_amazon[product])
        print(f"{product}(${lowest_price}")