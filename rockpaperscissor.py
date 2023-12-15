import random
choice = ("paper","scissors","rock")
running =True
while running:
  player = None
  computer =random.choice(choice)
  while player not in choice:
    player = input("Enter a choice (paper,scissors,rock): ")
  if player == computer:
    print("It's a tie")
  elif player == "paper" and computer == "rock":
    print("You win")
  elif player == "scissors" and computer== "paper":
    print("You win")
  elif player == "rock" and computer == "scissors":
    print("You win")
  else:
    print("You lose")
  if input("If you want to play again type (y) otherwise (n) ").lower() == "n":
    running = False

print("Thanks for playing") 