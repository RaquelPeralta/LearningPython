import random

def hangman_solo():

    # setup:

    word = []
    word_progress = []
    errors = []
    word_list = ["AMETHYST", "BUNDLE", "AXOLOTL", "SPYGLASS"]
    random_word_index = random.randrange(0, len(word_list))
    word_input = word_list[random_word_index]
    # create the lists:
    i = 0
    while i < len(word_input):
        word.append(word_input[i])
        word_progress.append("_")
        i = i + 1

    # hangman progress:
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

    # logic:

    while word_progress != word and errors.__len__() < 6:

        # interface:

        hangman = hangman_list[errors.__len__()]    # to check how to draw the hangman at each phase

        print("Word progress:")
        print(word_progress)
        print("Errors:")
        print(errors)
        print(hangman)
        letter = input("Choose a letter: ").upper()

        # validating the chosen letter:

        if letter in errors or letter in word_progress:  # to check if the letter is repeated
            print("")
            print("Repeated letter. Try again.")

        elif letter in word:  # to check if the letter is in the word
            print("")

            # to replace all of the correct letters:
            i = 0
            while i < (len(word)):
                if word[i] == letter:
                    word_progress[i] = letter
                    i = i + 1
                else:
                    i = i + 1

        else:   # if it's not repeated nor correct, it's an error
            print("")
            print("Nope.")
            errors.append(letter)
            errors.sort()

    # when the game loop ends:

    if word_progress == word:   # to check if player won
        print(word_progress)
        print(hangman)
        print("Congratulations! You win!")
        input()

    else:   # to check if the player lost their lives
        print("You lose!")
        print(hangman)
        print("Correct word:")
        print(word)
        print("Errors:")
        print(errors)
        input()

def hangman_multiplayer():
    # setup:
    word_input = input("Player 1, insert the word that you want the other players to guess. ")
    word = []
    word_progress = []
    errors = []

    # create the lists:
    i = 0
    while i < len(word_input):
        word.append(word_input[i])
        word_progress.append("_")
        i = i + 1

    # hangman progress:
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

    # logic:

    while word_progress != word and errors.__len__() < 6:

        # interface:

        hangman = hangman_list[errors.__len__()]  # to check how to draw the hangman at each phase

        print("Word progress:")
        print(word_progress)
        print("Errors:")
        print(errors)
        print(hangman)
        letter = input("Choose a letter: ").upper()

        # validating the chosen letter:

        if letter in errors or letter in word_progress:  # to check if the letter is repeated
            print("")
            print("Repeated letter. Try again.")

        elif letter in word:  # to check if the letter is in the word
            print("")

            # to replace all of the correct letters:
            i = 0
            while i < (len(word)):
                if word[i] == letter:
                    word_progress[i] = letter
                    i = i + 1
                else:
                    i = i + 1

        else:  # if it's not repeated nor correct, it's an error
            print("")
            print("Nope.")
            errors.append(letter)
            errors.sort()

    # when the game loop ends:

    if word_progress == word:  # to check if player won
        print(word_progress)
        print(hangman)
        print("Congratulations! You win!")
        input()

    else:  # to check if the player lost their lives
        print("You lose!")
        print(hangman)
        print("Correct word:")
        print(word)
        print("Errors:")
        print(errors)
        input()
