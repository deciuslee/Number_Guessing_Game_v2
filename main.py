# Jonathan Lee
# Purpose: Number Guessing Game v2

# Original Requirements
# Randomly choose a number between 1 and 100 (inclusive)
# Have the player enter a guess via input
# Tell the player the guess is high, low, or correct
# If high or low, allow the player to enter another guess
# Give the player an option to quit at any time
# Reward the player for a correct guess (ex., "Good job!")
# Tell the player how many guesses it took to guess correctly

# New Requirements
# Ask the player for their name prior to playing the game
# After each game:
# Update a file called topPlayers.txt with the results of the game (see specifications for this file below)
# Only save the top five players and scores
# Display the updated top 5 players from the topPlayers.txt file
# Allow the player to play again without having to rerun the program
# Use the topPlayers.txt Download topPlayers.txt file as a starting file
# If you opt to use functions, move those functions into a single library file
# Anticipate exceptions and catch them (i.e., fail nicely)
# The game should feel like a nice game to play
# Make it easy for the player to play the game
# Do not make the player do a bunch of extra stuff to play

# import random number generator
import random
# import library function
from library import updateTopPlayers, displayTopPlayers

# Define number guessing game function
def numberGuessingGame():
    # Secret number
    number = random.randint(1, 100)
    attempts = 0


    print(" ======= Number Guessing Game v2 ======= ")
    print()

    # player name entry
    while True:
        playerName = input("Please enter your name: ")
        if playerName == "":
            print("Invalid entry. Name must be 1 or more characters long.")
        else:
            break

    print(f"Welcome, {playerName}! I'm thinking of a number between 1 and 100. Can you guess it?")
    print()

    # Begin infinite loop to play game multiple times until player quits.
    while True:
            try:
                playerInput = input("Please enter your guess or press 'q' to quit: ")
                # player quit option
                if playerInput.lower() == "q":
                  print(f"Thanks for playing. The correct number was {number}.")
                  break
                # converts guess into integer
                guess = int(playerInput)

                # Test for guesses <1 or >100.
                if guess < 1 or guess > 100:
                  print(f"Invalid input. Please enter a number between 1 to 100.")
                  continue
                attempts += 1
                # Tests for low and high guesses
                if guess < number:
                   print(f"Guess is too low! Please try again.")
                elif guess > number:
                   print(f"Guess is too high! Please try again.")
                # Correct guess
                else:
                   print(f"Congratulations! You guessed the correct number {number} in {attempts} attempts.")
                   updateTopPlayers(playerName, attempts)
                   break

            # This is for any exceptions.
            except ValueError:
                print(f"Invalid entry. Please enter a valid number between 1 and 100.")

    # Display list of top players, updated or not
    displayTopPlayers()

if __name__ == "__main__":
    # Replay option
    while True:
        numberGuessingGame()

        play_again = input(f"Nice work! Would you like to play again? (y/n): ").lower()
        if play_again == "n":
            print(f"Thanks for playing!")
            break
        elif play_again != 'y':
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")