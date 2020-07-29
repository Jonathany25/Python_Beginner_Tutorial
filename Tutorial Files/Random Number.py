import random

replay = "yes"
score = 0
played = 0

while replay.lower() == "yes":
    number = (random.randint(1, 9))
    numstr = str(number)
    guess = int(input("Your Guess: "))
    played += 1
    if number == guess:
        print("Winner")
        score += 1
    elif guess > number:
        print("Too Huge")
        print("The number was " + numstr + ".")
    elif guess < number:
        print("Too Small")
        print("The number was " + numstr + ".")
    print("You have played " + str(played) + " times.")
    replay = input("Play Again?\n")





