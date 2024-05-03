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

# command = ""
# car_started = False

# while True:
#     command = input("> ").lower()

#     if command == "help":
#         print("start - to start the car\nstop - to stop the car\nquit - to exit")
#     elif command == "start":
#         if car_started:
#             print("Car has already started.")
#         else:
#             car_started = True
#             print("Car started... Ready to go!")
#     elif command == "stop":
#         if not car_started:
#             print("Car is already stopped.")
#         else:
#             car_started = False
#             print("Car stopped!")
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that...")

# / # / # / # / # / #

# prices = [10, 20, 30]
# result = 0

# for price in prices:
#     result += price

# print(f"Total: {result}.")

# / # / # / # / # / #

# numbers = [2, 2, 2, 2, 5]

# for x in numbers:
#     output = ""
#     for y in range(x):
#         output += "x"
#     print(output)

# / # / # / # / # / #

# numbers = [45, 12, 5, 99, 2]
# highest = 0

# for number in numbers:
#     if number > highest:
#         highest = number

# print(highest)

# / # / # / # / # / #

# numbers = [55, 16, 84, 100, 55, 12, 5, 97, 55, 100]

# for number in numbers:
#     if numbers.count(number) > 1:
#         numbers.remove(number)

# print(numbers)

# / # / # / # / # / #

# numbers = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
# }

# number = input("Phone: ")

# for _ in number:
#     print(numbers[_], end=" ")

# / # / # / # / # / #

# def generate_emoji(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😀",
#         ":(": "😞",
#     }

#     output = ""

#     for word in words:
#         output += emojis.get(word, word) + " "

#     return output


# text = input("> ")
# print(generate_emoji(text))

# / # / # / # / # / #

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi, I am {self.name}.")


# juan = Person("Juan")
# mariano = Person("Mariano")

# juan.talk()
# mariano.talk()

# / # / # / # / # / #

from utils import find_max

numbers = [38, 11, 100, 89, 10, 68, 41]

find_max(numbers)

# / # / # / # / # / #
