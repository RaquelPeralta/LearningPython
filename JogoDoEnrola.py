from UtilsRP import array_to_string, screen_clear, get_the_last_word

# Home screen:
print("")
print("Welcome to the ancient game of Rolling the Paper.")
print("")
print("This is a multiplayer game.")
print("One at a time will write part of a sentence.")
print("The program will show only the last word of the sentence to the next player, to continue the game.")
print("In the end, you will all read the story you created together.")
print("")

# the "play again" functionality
play_again = "Y"
while play_again == "Y":

    # to catch invalid characters when entering a number
    while True:
        try:
            numberOfRounds = int(input("To make sure everyone plays, how many rounds do you want to play? "))
            break
        except ValueError as ve:
            print("Invalid character. Enter a whole number.")

    sentences = [""]

    # Functions:
    def round_i():
        '''Receives and saves each player part of the sentence'''
        i = 0
        while i < numberOfRounds:
            if i == 0:
                print("Player 1 can start. Have a nice game!")
                sentences[0] = input("1: ")
                screen_clear()
                i = i + 1
            else:
                sentences.append(input(f"{i+1} : {get_the_last_word(sentences[i-1])} "))
                screen_clear()
                i = i + 1

    def end_of_game():
        print(array_to_string(sentences))


    # The game running:
    round_i()
    print("")
    end_of_game()
    print("")

    play_again = input("Play again? (Y/any) ").upper()



