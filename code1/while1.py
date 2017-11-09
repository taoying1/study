number=23
while True:
    guess = int(input("Enter an integer:"))
    if number==guess:
        print("Congratulations, you guess it!")
        print("but you do not win any prizes!")
        break
    elif guess < number:
        print("No, it is a little higher than that.")
    else:
        print("No,it is a little lower than that.")
print("The while loop is over!")