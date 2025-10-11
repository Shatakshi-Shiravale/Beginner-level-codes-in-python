import random

lower=int(input("enter lower bound"))
upper=int(input("enter upper bound"))
print("You have 5 guesses to guess the number")
x=random.randint(lower,upper)
guess=0
if upper<lower:
    print("Error, upper bound is smaller than lower bound")
else:
    while guess<5:
        guess = guess + 1
        x1 = int(input("enter your guess"))
        if guess==5 and x1!=x:
            print("Sorry! You couldn't guess the number.")
            break
        elif upper>=x1>x:
            print("Guess lower")
        elif lower<=x1<x:
            print("Guess higher")
        elif x1==x:
            print("Congratulations, you guessed the number in",guess, "trial(s).")
            break
        else:
            print("Number out of range")





