import random


def dice():
    '''returns a random number 1-6'''
    result = random.randint(1, 6)
    return result


# class Player:
#
#     def __init__(self, x, y):
#         self.x = x
#
#     def move(self, result, horizontal_move, vertical_move):
#         self.x = x + result


map = [
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print(map[0])
print(map[1])
print(map[2])
print(map[3])

print("How to move:")
print(" press W to move 1 space up")
print(" press A to move 1 space to the left")
print(" press S to move 1 space down")
print(" press D to move 1 right")

D = ""
while D != "D":
    print ("Press D to roll the dice.")
    D = input("").upper()

result = dice()

# Receive the movement input from player:
move = ""
while move.count("w")+move.count("a")+move.count("s")+move.count("d") != result:
    if len(move) == result:     # if the player uses other letters, we will remind them the correct letters to move
        print("How to move:")
        print(" press W to move 1 space up")
        print(" press A to move 1 space to the left")
        print(" press S to move 1 space down")
        print(" press D to move 1 right")
    if result == 1:
        print("move 1 space")
    else:
        print(f"move {result} spaces")
    move = input("")

# map[x][y]   # the 1st index indicates the line, the 2nd indicates the column

x = 0 + move.count("s") - move.count("w")
y = 0 + move.count("d") - move.count("a")

map[x][y] = 2

print(map[0])
print(map[1])
print(map[2])
print(map[3])


