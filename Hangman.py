import random
from os import system, name
from UtilsRP import array_to_string, screen_clear

# global vars:
word = []
word_progress = []
errors = []
word_input = ""
hangman_list = [
    """


""",
    """
     o


""",
    """
     o
     |

""",
    """
     o
    (|

""",
    """
     o
    (|)

""",
    """
     o
    (|)
    |
""",
    """
     o
    (|)
    | |
"""]

# functions for game logic:
def setup_solo():
    '''builds the array with the random word to guess'''
    word.clear()
    word_progress.clear()
    errors.clear()
    word_input = ""

    word_list = ["AMETHYST", "BUNDLE", "AXOLOTL", "SPYGLASS"]
    word_input = random.choice(word_list)

    # create the lists:
    i = 0
    while i < len(word_input):
        word.append(word_input[i])
        word_progress.append("_")
        i = i + 1


def setup_multiplayer():
    '''builds the array with the chosen word to guess'''
    word.clear()
    word_progress.clear()
    errors.clear()
    word_input = ""

    word_input = input("Player 1, insert the word that you want the other players to guess. ").upper()
    # create the lists:
    i = 0
    while i < len(word_input):
        word.append(word_input[i])
        word_progress.append("_")
        i = i + 1
    screen_clear()


def validate_letter(letter):
    '''validates the chosen letter'''
    screen_clear()  # to clear the previous round
    if letter in errors or letter in word_progress:  # to check if the letter is repeated
        print("Repeated letter. Try again.")

    elif letter in word:  # to check if the letter is in the word
        # to replace all of the correct letters:
        print("Nice!")
        i = 0
        while i < (len(word)):
            if word[i] == letter:
                word_progress[i] = letter
                i+=1
            else:
                i +=1

    else:  # if it's not repeated nor correct, it's an error
        print("Nope.")
        errors.append(letter)
        errors.sort()


def end_of_game(hangman):
    '''when the game loop ends, it validates if the player won or lost'''
    if word_progress == word:   # to check if player won
        print(array_to_string(word_progress))
        print(hangman)
        print("Congratulations! You win!")
    else:   # to check if the player lost their lives
        hangman = hangman_list[errors.__len__()]
        print("You lose!")
        print(hangman)
        print("Correct word: " + array_to_string(word))
        print("Errors: " + array_to_string(errors))


# gamemode functions:
def hangman_solo():
    setup_solo()

    while word_progress != word and errors.__len__() < 6:

        # interface:
        hangman = hangman_list[errors.__len__()]    # to check how to draw the hangman at each phase

        print("Word progress: " + array_to_string(word_progress))
        print("Errors: " + array_to_string(errors))
        print(hangman)
        letter = input("Choose a letter: ").upper()
        validate_letter(letter)

    end_of_game(hangman)


def hangman_multiplayer():
    setup_multiplayer()

    while word_progress != word and errors.__len__() < 6:

        # interface:
        hangman = hangman_list[errors.__len__()]  # to check how to draw the hangman at each phase

        print("Word progress: " + array_to_string(word_progress))
        print("Errors: " + array_to_string(errors))
        print(hangman)
        letter = input("Choose a letter: ").upper()
        validate_letter(letter)

    end_of_game(hangman)