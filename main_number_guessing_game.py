import random

secret_number = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10:"))

if guess == secret_number:
    print("You got it!")
else:
    print(f"Sorry, you got it wrong.  The secret number is: {secret_number}")