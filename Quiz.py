score = 0
answer1 = input("What is the capital of India? ")
if answer1. lower() == "new delhi":
    print("Correct!")
    score = score + 1
else:
    print("wrong! Answer is New Delhi")
answer2 = input("What is 10 + 10? ")

if answer2 == "20":
    print("correct!")
    score = score + 1
else:
    print("Wrong! Answer is 20")
answer3 = input("who created python? ")

if answer3.lower() == "guido van rossum":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! Answer is Guido van Rossum")
print(f"\nYour score: {score}/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good!")
elif score == 1:
    print("Keep practicing!")
else:
    print("Better luck next time!")
