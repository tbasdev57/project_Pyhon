import random

play = True

while play:

    print("Welcome to the number guess game")

    number_to_guess = random.randint(1,10)

    guess = int(input("Guess a number between 1 and 10: "))

    count_number_of_tries = 1

    while guess != number_to_guess:

        if guess == -1 or (guess >= 1 and guess <= 10):

            if guess == -1:
                print(f"psst, the number is {number_to_guess}")
                guess = int(input("Guess again: "))
            else:
                print("Wrong guess")

                if guess > number_to_guess: 
                    print("Your guess was higher than the number.")
                    if guess == number_to_guess + 1:
                        print("You missed by 1")
                else: 
                    print("Your guess was lower than the number.")
                    if guess == number_to_guess - 1:
                        print("You missed by 1")

                if count_number_of_tries == 4:
                    break

                guess = int(input("Guess again: "))

                count_number_of_tries += 1
        else:
            print("Ooops, wrong input.")
            guess = int(input("Guess again: "))
        

    if number_to_guess == guess:
        print("Well done, you won!")
        print(f"You took {count_number_of_tries} goes to complete the game")
    else:
        print("Sorry, you loose")
        print(f"the number you needed to guess was {number_to_guess}")
    print("game over")

    again = input("Play again? (y/n) ")
    if (again != "Y") and (again != "y"):
        play = False