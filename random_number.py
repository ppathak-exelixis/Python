# How to generate random numbers
import random

random_integer = random.randint(1 , 100)
print(random_integer)
random_decimal = float(random.random()) * 5
print(round(random_decimal, 2))

# Head and Tail

number = random.randint(1 , 10)
if number%2 == 0:
    print("Heads")
else:
    print("Tails")