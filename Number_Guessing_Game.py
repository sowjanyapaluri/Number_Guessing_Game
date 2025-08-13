import random

def guess(x):
    random_number = random.randint(1, x)
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input(f"Please enter your guess (between 1 and {x}): "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        if guess < 1 or guess > x:
            print("The number is out of the specified range.")
            continue
        attempts += 1
        if guess < random_number:
            print("Your guess is too low.")
        elif guess > random_number:
            print("Your guess is too high.")
        else:
            print("Congratulations! You have guessed the correct number.")
            return
        print(f"Attempts remaining: {max_attempts - attempts}")
    print(f"All attempts used. The correct number was {random_number}.")

x = int(input("Enter the upper limit for the guessing range: "))
print("The maximum number of attempts allowed is 5.")
guess(x)