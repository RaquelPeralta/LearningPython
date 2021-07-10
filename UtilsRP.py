# module of transversal functions to reuse in multiple projects

def array_to_string(array):
    '''turns an array of letters into a string, with the letters divided by spaces.'''
    string = ""
    for i in array:
        string += i + " "
    return string


def screen_clear():
    ''' clears entire screen.'''
    from os import name, system
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


