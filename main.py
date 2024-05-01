# print("Juan Cardenas")
# print("o----")
# print(" ||||")
# print("*" * 10)

# / # / # / # / # / #

# price = 10
# rating = 4.9
# name = "Mosh"
# is_published = False

# print(price)

# full_name = "John Smith"
# age = 20
# is_new = True

# name = input("What is your name? ")
# print("Hi " + name)

# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# print(name + " likes " + color + ".")

# / # / # / # / # / #

# birth_year = input("Birth year: ")
# print(type(birth_year))
# age = 2024 - int(birth_year)
# print(type(age))
# print(age)

# / # / # / # / # / #

# pounds = input("What is your weight in pounds?: ")
# kilograms = "{:.2f}".format(int(pounds) / 2.205)
# print(kilograms)

# / # / # / # / # / #

# course = "Python for Beginners"
# course = "Python's for Beginners"
# course = 'Python for "Beginners"'
# course = '''
# Hi John,

# Here is our first email to you.

# Thank you.
# The support team
# '''

# name = "Jennifer"
# print(name[1:-1])

# / # / # / # / # / #

# x = (2 + 3) * 10 - 3
# print(x)

# / # / # / # / # / #

# house_price = 1000000
# good_credit = True

# if good_credit:
#     down_payment = house_price * 0.1
# else:
#     down_payment = house_price * 0.2

# print(f"Down payment = ¢{down_payment}.")

# / # / # / # / # / #

# name = "Juan Cardenas"

# if len(name) < 3:
#     print("Name must be at least 3 characters long.")
# elif len(name) > 50:
#     print("Name can be maximum of 50 characters long.")
# else:
#     print("Name looks good!")

# / # / # / # / # / #

# weight = float(input("Weight: "))
# unit = input("(L)bs or /K(g): ").lower()

# if unit == "l":
#     new_weight = "{:.2f}".format(weight / 2.205)
#     print(f"You are {new_weight} kilograms.")
# elif unit == "k":
#     new_weight = "{:.2f}".format(weight * 2.205)
#     print(f"You are {new_weight} pounds.")

# / # / # / # / # / #

# secret_number = 9
# guess_count = 0
# limit = 3

# while guess_count < limit:
#     guess_number = float(input("Guess: "))
#     guess_count += 1

#     if guess_number == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, you failed!")

# / # / # / # / # / #

command = ""

while True:
    command = input("> ").lower()

    if command == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif command == "start":
        print("Car started... Ready to go!")
    elif command == "stop":
        print("Car stopped!")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that...")

# / # / # / # / # / #
