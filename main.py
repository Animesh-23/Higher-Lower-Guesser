
from art import logo,vs
from replit import clear
from game_data import data
import random


def play_game():
  print(f"Compare A: {first_id['name']}, {first_id['description']}, from {first_id['country']}")
  print(vs)
  print(f"Against B: {second_id['name']}, {second_id['description']}, from {second_id['country']}")
  choice = input("Who has more followers? Type 'A' or 'B': ")
  return choice


first_id = random.choice(data)
second_id = random.choice(data)

winning = True
score = 0
print(logo)
while winning:
  choice = play_game()
  if (choice == "A" and first_id['follower_count'] > second_id['follower_count']) or (choice == "B" and first_id['follower_count'] < second_id['follower_count']):
    score += 1
    clear()
    print(logo)
    print(f"You're right. Current score is {score}")
    first_id = second_id
    while first_id['name'] == second_id['name']:
      second_id = random.choice(data)
  else:
    clear()
    print(f"Sorry that's wrong. Final score is {score}")
    winning = False
    
