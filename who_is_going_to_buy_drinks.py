# Who is going to buy drinks today!

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length_of_inputs = len(names)
random_name = random.randint(0 , length_of_inputs - 1)
print(f"{names[random_name]} is going to buy the meal today!")