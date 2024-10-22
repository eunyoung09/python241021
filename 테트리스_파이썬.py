import pygame
import random

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

# 게임 설정
CELL_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# 테트로미노 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.randint(1, len(COLORS) - 1)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetromino()
        self.score = 0

    def collision(self, x, y):
        for i, row in enumerate(self.current_piece.shape):
            for j, cell in enumerate(row):
                if cell and (y + i >= GRID_HEIGHT or x + j < 0 or x + j >= GRID_WIDTH or self.grid[y + i][x + j]):
                    return True
        return False

    def merge(self):
        for i, row in enumerate(self.current_piece.shape):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + i][self.current_piece.x + j] = self.current_piece.color

    def remove_lines(self):
        lines_to_remove = [i for i, row in enumerate(self.grid) if all(row)]
        for line in lines_to_remove:
            del self.grid[line]
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        self.score += len(lines_to_remove) ** 2 * 100

    def move(self, dx, dy):
        if not self.collision(self.current_piece.x + dx, self.current_piece.y + dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
            return True
        return False

    def drop(self):
        if not self.move(0, 1):
            self.merge()
            self.remove_lines()
            self.current_piece = Tetromino()
            if self.collision(self.current_piece.x, self.current_piece.y):
                return False
        return True

    def rotate(self):
        original_shape = self.current_piece.shape
        self.current_piece.rotate()
        if self.collision(self.current_piece.x, self.current_piece.y):
            self.current_piece.shape = original_shape

def draw_grid(screen, game):
    for y, row in enumerate(game.grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, COLORS[cell], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

def draw_piece(screen, piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, COLORS[piece.color], 
                                 ((piece.x + x) * CELL_SIZE, (piece.y + y) * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("테트리스")
    clock = pygame.time.Clock()
    game = Tetris()
    drop_time = 0
    running = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.drop()
                elif event.key == pygame.K_UP:
                    game.rotate()

        drop_time += clock.get_rawtime()
        if drop_time > 500:
            if not game.drop():
                running = False
            drop_time = 0

        draw_grid(screen, game)
        draw_piece(screen, game.current_piece)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"점수: {game.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()