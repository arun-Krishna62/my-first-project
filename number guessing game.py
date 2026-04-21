import random
secret = random.randint(1,10)
guess = int(input("Guess a number (1-10): "))
if guess == secret:
    print("correct! You won!")
else:
    print("Wrong! The number was",secret)
