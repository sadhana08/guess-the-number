# Guess the number (secrete no by computer)
import random

def human_guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f"Enter a number between 1 and {x} :"))
        if guess < random_number:
            print("Oops.TRY AGAIN.Your value is too low! ")
        elif guess > random_number:
            print("Oops.TRY AGAIN.Your value is too high!")

        
    print("Great you have won!")

#human_guess(10)   use this for calling the above

# Guess the number (secrete no by human)
def comp_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'c': #correct
        # If low and high are equal in radiant it will give us an error
        if low == high:
            guess = high              #or low
        else :
            guess = random.randint(low,high)
        feedback = input(f"The value {guess} is too low (l) or too high (h) or correct (c) ")
        if feedback == 'h':           #high value
              high = guess - 1
        elif feedback == 'l':          #low value
              low = guess + 1
    print("Hey that's right!")

comp_guess(10)








