from UtilsRP import array_to_string, screen_clear

# Home screen:

print("Welcome to the ancient game of Rolling the Paper.")
print("")
print("This is a multiplayer game.")
print("One at a time will write part of a sentence.")
print("The program will show only the last word of the sentence to the next player, to continue the game.")
print("In the end, you will all read the story you created together.")
print("")
numberOfPlayers = ("To make sure everyone plays, how many players are joining this round? ")

sentences = [""]


# Functions:

def get_the_last_word (string):
    '''Returns the last word in a string'''
    # turning the string into an array, and returning the last element
    array = string.split()
    return array[-1]


def round_i():
    '''Receives and saves each player part of the sentence'''
    i = 0
    while i < (numberOfPlayers * 3):
        if i == 0:
            print("Player 1 can start. Have a nice game!")
            sentences[0] = input("1: ")
            screen_clear()
            i = i + 1
        else:
            sentences[i] = input(f"{i+1} : {get_the_last_word(sentences[i-1])} ")
            screen_clear()
            i = i + 1


def end_of_game():
    print(array_to_string(sentences))
    input("")


# The game running:

round_i()
end_of_game()



