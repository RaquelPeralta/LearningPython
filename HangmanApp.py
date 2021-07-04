import Hangman

# choosing the gamemode:
print("Press S for a solo game where you will try to guess my words.")
print("Press M for a multiplayer game where you will try to guess a word inserted by another player.")
gamemode = input(" ").upper()

# validate the gamemode choice
while gamemode != "S" and gamemode != "M":
    print("")
    print("Invalid choice. Try again.")
    print("Press S for a solo game where you will try to guess my words.")
    print("Press M for a multiplayer game where you will try to guess a word inserted by another player.")
    gamemode = input(" ").upper()

if gamemode == "S":
    Hangman.hangman_solo()

if gamemode == "M":
    Hangman.hangman_multiplayer()

print("")
play_again = input("Play again? (Y/any) ").upper()

while play_again == "Y":
    # choosing the gamemode:
    print("Press S for a solo game where you will try to guess my words.")
    print("Press M for a multiplayer game where you will try to guess a word inserted by another player.")
    gamemode = input(" ").upper()

    # validate the gamemode choice
    while gamemode != "S" and gamemode != "M":
        print("")
        print("Invalid choice. Try again.")
        print("Press S for a solo game where you will try to guess my words.")
        print("Press M for a multiplayer game where you will try to guess a word inserted by another player.")
        gamemode = input(" ").upper()

    if gamemode == "S":
        Hangman.hangman_solo()

    if gamemode == "M":
        Hangman.hangman_multiplayer()

    print("")
    play_again = input("Play again? (Y/any) ").upper()


