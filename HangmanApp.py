import Hangman

# the "play again" functionality
play_again = "Y"
while play_again == "Y":

    # choosing the gamemode:
    gamemode = ""
    while gamemode != "S" and gamemode != "M":
        print("Press S for a solo game where you will try to guess my words.")
        print("Press M for a multiplayer game where you will try to guess a word inserted by another player.")
        gamemode = input("").upper()
        print("")
        if gamemode != "S" and gamemode != "M":
            print("Invalid choice. Try again.")

    if gamemode == "S":
        Hangman.hangman_solo()

    if gamemode == "M":
        Hangman.hangman_multiplayer()

    print("")
    play_again = input("Play again? (Y/any) ").upper()
