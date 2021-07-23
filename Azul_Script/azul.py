import random
from warnings import showwarning
import pygame

colors = [
    "blue",
    "yellow",
    "red",
    "black",
    "white"
]

def generate_board():
    board = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]
    row_1 = []
    while len(row_1) < 5:
        color = random.choice(colors)
        while color in row_1:
            color = random.choice(colors)
        row_1.append(color)
    board[0] = row_1

    for i in range(4):
        for j in range(5):
            board[i+1][j] = board[i][j-1]

    board = shuffle_board(board, "row")
    board = shuffle_board(board, "column")

    return board

def shuffle_board(board, row_column):
    shuffled_board = []
    for row in board:
        shuffled_board.append(row.copy())
    used_indexes = []
    for i in range(5):
        index = random.randint(0, 4)
        while index in used_indexes:
            index = random.randint(0, 4)
        used_indexes.append(index)
        if row_column == "row":
            shuffled_board[i] = board[index]
        for row in shuffled_board:
            print(row)
        print(index)
        print(i)
        print("-----------------------")
        for row in board:
            print(row)
        print("xxxxxxxxxxxxxxxxxxxxxxxxx")
        if row_column == "column":
            for j in range(5):
                shuffled_board[j][i] = board[j][index]
    return shuffled_board

# for row in generate_board():
#     print(row)

pygame.init()
background = (176, 159, 130)
X = 200*5
Y = 200*5
display_surface = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Image')
board = generate_board()

while True :
    display_surface.fill(background)
    for i in range(5):
        for j in range(5):
            color = board[i][j]
            display_surface.blit(pygame.image.load(r'C:\Users\jerem\desktop\scripts\Azul_Script\images\{}.png'.format(color)), (i*200, j*200))

    pygame.image.save(display_surface,"screenshot.jpg")

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        pygame.display.update() 