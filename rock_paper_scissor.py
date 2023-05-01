rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list = [rock , paper , scissors]
computer_input = random.randint(0 , 2)
user_input = int(input("To play this game you need to choose 0 for Rock, 1 for Paper & 2 for Scissor. Please enter here ->>> "))
if list[computer_input] == list[user_input]:
  print("We are draw \U0001F923")
elif list[user_input] == rock and list[computer_input] == scissors:
   print("Congratuations, you WON!!!\U0001f600")
elif list[user_input] == paper and list[computer_input] == rock:
  print("Congratulations, you WON!!!\U0001f600")
elif list[user_input] == scissors and list[computer_input] == paper:
  print("Congratulations, you WON!!!\U0001f600")
