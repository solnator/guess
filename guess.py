# score = 0
from random import randint

num = randint(1, 10)
for i in range(5):
    guess = eval(input("Enter your guess: "))
    if guess == num:
        print("You Won!")
        break
    else:
        print("sorry,Wrong Number")
    if guess > num:
        print("Your guess is higher than the Number.")
    if guess < num:
        print("Your guess is lower than the Number.")
if guess != num:
    print("You Loss!")
print("See You Soon:)")
