import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
COLUMNS = SCREEN_WIDTH // GRID_SIZE
ROWS = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (128, 0, 128),  # Purple
    (255, 0, 0)     # Red
]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell and (x + off_x < 0 or x + off_x >= COLUMNS or y + off_y >= ROWS or board[y + off_y][x + off_x]):
                return True
    return False

def join_matrixes(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = cell

def remove_line(board, row):
    del board[row]
    return [[0 for _ in range(COLUMNS)]] + board

def create_board():
    return [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

def draw_board(screen, board):
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, COLORS[cell - 1], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_tetromino(screen, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, tetromino.color, ((tetromino.x + x) * GRID_SIZE, (tetromino.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()
    board = create_board()
    tetromino = Tetromino()

    running = True
    while running:
        screen.fill(BLACK)
        
        if check_collision(board, tetromino.shape, (tetromino.x, tetromino.y + 1)):
            join_matrixes(board, tetromino.shape, (tetromino.x, tetromino.y))
            tetromino = Tetromino()
            if check_collision(board, tetromino.shape, (tetromino.x, tetromino.y)):
                running = False  # Game over
        else:
            tetromino.y += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, tetromino.shape, (tetromino.x - 1, tetromino.y)):
                        tetromino.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(board, tetromino.shape, (tetromino.x + 1, tetromino.y)):
                        tetromino.x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(board, tetromino.shape, (tetromino.x, tetromino.y + 1)):
                        tetromino.y += 1
                elif event.key == pygame.K_UP:
                    rotated = [list(row) for row in zip(*tetromino.shape[::-1])]
                    if not check_collision(board, rotated, (tetromino.x, tetromino.y)):
                        tetromino.shape = rotated
        
        # Clear full rows
        for i, row in enumerate(board):
            if 0 not in row:
                board = remove_line(board, i)

        draw_board(screen, board)
        draw_tetromino(screen, tetromino)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == '__main__':
    main()
