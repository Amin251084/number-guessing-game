import random

print("Welcome to the Number Guessing Game")
play_again = True

while play_again == True:

    number = random.randint(1, 100)
    guess = 0
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:

        while True:
            try:
                guess = int(input("Guess a number between 1 and 100:"))
                break
            except ValueError:
                print("You must enter a number!")
                print("----------------------------------")

        distance = abs(number - guess)

        if 0 < guess < number:
            attempts += 1
            print(f"My number is higher than {guess}")
            
            if distance <= 5:
                print("You're very close")
            elif 5 < distance <= 15:
                print("You're close")
            else:
                print("You're far away")

            print(f"Guess number: {attempts} of {max_attempts}")
            print(f"Attempts remaining: {max_attempts - attempts}")
            print("----------------------------------")

        elif number < guess <= 100:
            attempts += 1
            print(f"My number is lower than {guess}")
            
            if distance <= 5:
                print("You're very close")
            elif 5 < distance <= 15:
                print("You're close")
            else:
                print("You're far away")

            print(f"Guess number: {attempts} of {max_attempts}")
            print(f"Attempts remaining: {max_attempts - attempts}")
            print("----------------------------------")
            

        elif guess == number:
            attempts += 1
            print(f"Yes its {number} you won!")

            if attempts == 1:
                print("Your score: ★ ★ ★ ★ ★")
            elif attempts == 2:
                print("Your score: ★ ★ ★ ★")
            elif attempts == 3:
                print("Your score: ★ ★ ★")
            elif attempts == 4:
                print("Your score: ★ ★")
            elif attempts == 5:
                print("Your score: ★")

            break

        else :
            print("Invalid number. Please enter a number between 1 and 100.")
            print("----------------------------------")

    if guess != number:
        print(f"Oh you lost ): The number was {number}")

    while True:
        p = input("Would you like to play again? (y/n)")

        if p.lower() == "y":
            print("Okay, let's play again")
            break
        elif p.lower() == "n":
            print("Have a good day! Bye")
            play_again = False
            break
        else:
            print("Please enter only 'y' or 'n'")
            print("----------------------------------")
            continue