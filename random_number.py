# How to generate random numbers
import random

random_integer = random.randint(1 , 100)
print(random_integer)
random_decimal = float(random.random()) * 5
print(round(random_decimal, 2))

# Head and Tail

number = random.randint(0 , 1)
if number == 0:
    print("Heads")
else:
    print("Tails")

# Who is going to buy drinks today!

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length_of_inputs = len(names)
random_name = random.randint(-1 , length_of_inputs)
print(f"{names[random_name]} is going to buy the meal today!")