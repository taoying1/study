import random
secret=random.randint(1,100)
guess=0
tries=0
while guess!=secret and tries<6:
    guess=int(input("What's you guess:"))
    if guess<secret:
        print("Too low")
    elif guess>secret:
        print("Too high")
    tries+=1
if guess==secret:
    print("You got it!")
else:
    print("No more guesses!")
    print("The secret number is %d"%secret)