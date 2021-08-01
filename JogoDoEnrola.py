from UtilsRP import array_to_string, screen_clear

frases = ["", "", "", "", "", "", "", "", "", ""]

def getTheLastWord (string):
    '''Returns the last word in a string'''
    # turning the string into an array, and returning the last element
    array = string.split()
    return array[-1]

# Round i:
i = 0
while i < frases.__len__():
    if i == 0:
        frases[i] = input(f"{i + 1} : ")
        screen_clear()
        i = i + 1
    else:
        frases[i] = input(f"{i+1} : {getTheLastWord(frases[i-1])} ")
        screen_clear()
        i = i + 1

print(array_to_string(frases))