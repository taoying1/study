import easygui
import random
secret=random.randint(1,100)
guess=0
tries=0
easygui.msgbox("I'm the Roberts, and I have a secret!It is a number from 1 to 99.I'll give you 6 tries.")
while guess!=secret and tries<6:
    guess= easygui.integerbox("What's you guess:")
    if not guess: break
    if guess<secret:
         easygui.msgbox(str(guess)+" is too low")
    elif guess>secret:
        easygui.msgbox(str(guess)+" is too high")
    tries+=1
if guess==secret:
    print(easygui.msgbox("You got it!"))
else:
    print(easygui.msgbox("No more guesses!The secret number is %d"%secret))