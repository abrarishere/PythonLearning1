import random

number = random.randint(1,100)
guesses = 0
while True:
  guess = int(input("Ghess a number between 1 and 100 (q to quit): "))
  guesses +=1
  if guess > number:
    print("Too High")
  elif guess < number:
    print("Too Low")
  else:
    print(f"You got it in {guesses} guesses!")
    status = input("Play again? (y/n)").lower()
    if status == "n":
      break
    else:
      print()

print("Thanks for playing!")