import random
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

images = [rock,paper,scissors]
user_choose= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors "))

if user_choose >= 0 and user_choose <=2 :
  print(images[user_choose])
else:
    print("You give a invalid input")

computer_choice = random.randint(0,2)
print(f" Computer choose: {computer_choice}")
print(images[computer_choice])
if user_choose >= 3 or user_choose < 0:
    print("You typed an invalid number. You lose!")
elif user_choose == 0 and computer_choice == 2:
    print("You win")
elif user_choose == 1 and computer_choice == 0:
    print("computer win")
elif user_choose == 2 and computer_choice == 1:
    print("You win")
else:
    print("Tie")


