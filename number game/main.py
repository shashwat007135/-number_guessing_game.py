import random

print("🎯 Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 20")

number = random.randint(1, 20)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess == number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

if guess != number:
    print(f"❌ Game Over! The number was {number}")

