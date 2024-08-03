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
user_choice = input("choose 0 for Rock 1 for Paper and 2 for scissors: ")
CPU_choice=random.randint(0,2)
CPU_choice=str(CPU_choice)

print(f"User choose: {user_choice}")
print(f"CPU choose: {CPU_choice}")

if user_choice=='0':
    print(rock)
elif user_choice=='1':
    print(paper)    
else:
    print(scissors)

print("CPU choice: ")
if CPU_choice=='0':
    print(rock)
elif CPU_choice=='1':
    print(paper)
else:
    print(scissors)

if user_choice == '0' and 'CPU_choice' == '2':
    print("User Won")
elif user_choice == '2' and CPU_choice == '1':
    print("User Won")
elif user_choice == '1' and CPU_choice == '0':
    print("User Won")
elif user_choice == CPU_choice:
    print("Draw")
else:
    print("CPU Won")