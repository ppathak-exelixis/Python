print("Welcome to Ticket Calculator: ")
height = int(input("What's your height in cm? "))
H = 120
bill = 0
if height > H:
    print("Congratulations you can ride the rollercoaster!")
    age = int(input("What's your age ? "))
    if age < 12:
        bill += 5
        photo = input("do you want photo as well ? Y or N ")
        if photo == "Y":
            bill += 3
            print(f"Your Total bill is ${bill}")
        else:
            print(f"Your Total bill is ${bill}")
    elif age < 18:
        bill += 7
        photo = input("do you want photo as well ? Y or N ")
        if photo == "Y":
            bill += 3
            print(f"Your Total bill is ${bill}")
        else:
            print(f"Your Total bill is ${bill}")
    elif age >= 45 and age <= 55:
        bill += 0
        photo = input("do you want photo as well ? Y or N ")
        if photo == "Y":
            bill += 3
            print(f"Congratulations...we have waived off your ticket fee and only added photo fee...So your total bill is ${bill}")
        else:
            print(f"Your Total bill is ${bill}")
    else:
        bill += 12
        photo = input("do you want photo as well ? Y or N ")
        if photo == "Y":
            bill += 3
            print(f"Your Total bill is ${bill}")
        else:
            print(f"Your Total bill is ${bill}")
else:
    print("Sorry you need to raise your height to qualify for rollarcoster!!!")


