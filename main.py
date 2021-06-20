import random

number = random.randint(1, 10)
count = 0
guess = 0
while guess != number:
    count += 1
    guess = input('Guess a number between 1 and 5: ')
    if guess.isnumeric():
        guess = int(guess)
    elif guess > number:
      print("Your guess is too high, try again!")  
    elif guess < number:  
        print("Your guess is too low, try again!") 
else:
    print(f'You guessed it in {count} tries!')