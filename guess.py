import random

number = random.randint(1,10)

numberOfGuesses = 0

while numberOfGuesses < 5:
    print("Guess a number between 1 and 10")

    guess = input()
    guess = int(guess)

    numberOfGuesses = numberOfGuesses + 1

    if guess < number:
        print("Guess too low")
    if guess > number:
        print("Guess too high")
    if guess == number:
        break

if guess ==  number:
    print("You guessed the number! in " + str(numberOfGuesses) + " attempts!")
else:
    print("You didnt guess the number, the number was:", number)
