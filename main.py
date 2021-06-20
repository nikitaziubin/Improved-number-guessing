import random

max_allowed_nmber = 10
number = random.randint(1, max_allowed_nmber)
count = 0
guess = 0
while guess != number:
    count += 1
    guess = input('Guess a number between 1 and ' +  str(max_allowed_nmber) + ':')

    if guess.isnumeric():
        guess = int(guess)
    if guess > number:
            print("Your guess is too high, try again!")  
    elif guess < number:  
           print("Your guess is too low, try again!") 
else:
    print(f'You guessed it in {count} tries!')