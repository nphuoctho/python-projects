import random

print(
    "Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!"
)

low = int(input("Enter the Lower Bound of the range: "))
high = int(input("Enter the Upper Bound of the range: "))

num = random.randint(low, high)
chances = 7
guess_count = 0

while guess_count < chances:
    guess_count += 1
    guess = int(
        input(f"Attempt {guess_count}: Make your guess between {low} and {high}: ")
    )

    if guess == num:
        print(
            f"Congratulations! You've guessed the number {num} correctly in {guess_count} attempts."
        )
        break
    elif guess < num:
        print("Try Again! You guessed too small.")
    elif guess > num:
        print("Try Again! You guessed too high.")
    elif guess != num and guess_count == chances:
        print("Better Luck Next Time!")
