#by Computer
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while (guess!=random_number):
        guess = int(input(f"Guess the number between 1 and {x}:"))
        if guess > random_number:
            print("Too high, guess again.")
        elif guess < random_number:
            print("Too low, guess again")
    print(f"Congratulations, you guessed the number {random_number} correctly.")




#by user
def computer_guess(x):
    low = 1
    high = x
    feedback = ' '
    while (feedback!='c'):
        if low!=high:
            guess = random.randint(low, high)
        else:
            guess = high # or low because low == high
        feedback = input(f"Is the guessed number {guess} too high (h), too low (l) or have the computer guessed correctly (c)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Computer guessed the number {guess} correctly!")

guess(2000)

        

        
