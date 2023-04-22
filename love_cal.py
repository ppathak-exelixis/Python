print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



name1_lower = name1.lower()
name2_lower = name2.lower()
t = int(name1_lower.count("t")) + int(name2_lower.count("t"))
r = int(name1_lower.count("r")) + int(name2_lower.count("r"))
u = int(name1_lower.count("u")) + int(name2_lower.count("u"))
e = int(name1_lower.count("e")) + int(name2_lower.count("e"))
true = t + r + u + e
l = int(name1_lower.count("l")) + int(name2_lower.count("l"))
o = int(name1_lower.count("o")) + int(name2_lower.count("o"))
v = int(name1_lower.count("v")) + int(name2_lower.count("v"))
e = int(name1_lower.count("e")) + int(name2_lower.count("e"))
love = l + o + v + e
score_join = str(true) + str(love)
score = int(score_join)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")