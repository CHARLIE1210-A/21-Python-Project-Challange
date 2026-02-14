import pygame
import random

# ================= SETTINGS =================
CELL_SIZE = 30
COLS = 10
ROWS = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

SHAPES = [
    [[1, 1, 1, 1]],          # I
    [[1, 1], [1, 1]],        # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

COLORS = [
    (0, 255, 255),
    (255, 255, 0),
    (128, 0, 128),
    (255, 165, 0),
    (0, 0, 255)
]

# ================= PIECE =================
class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))


# ================= GAME =================
class Tetris:
    def __init__(self):
        self.grid = [[(0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]
        self.current = Piece()
        self.score = 0

    def draw_grid(self, screen):
        for y in range(ROWS):
            for x in range(COLS):
                pygame.draw.rect(
                    screen,
                    self.grid[y][x],
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

    def draw_piece(self, screen):
        for y, row in enumerate(self.current.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen,
                        self.current.color,
                        (
                            (self.current.x + x) * CELL_SIZE,
                            (self.current.y + y) * CELL_SIZE,
                            CELL_SIZE,
                            CELL_SIZE
                        )
                    )

    def move_down(self):
        self.current.y += 1
        if self.collision():
            self.current.y -= 1
            self.lock_piece()
            self.current = Piece()

    def collision(self):
        for y, row in enumerate(self.current.shape):
            for x, cell in enumerate(row):
                if cell:
                    nx = self.current.x + x
                    ny = self.current.y + y
                    if ny >= ROWS or nx < 0 or nx >= COLS or self.grid[ny][nx] != (0, 0, 0):
                        return True
        return False

    def lock_piece(self):
        for y, row in enumerate(self.current.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current.y + y][self.current.x + x] = self.current.color
        self.clear_lines()
        
    def clear_lines(self):
        lines_cleared = 0
        
        for row in self.grid[:]:
            if (0,0,0) not in row:
                self.grid.remove(row)
                self.grid.insert(0, [(0, 0, 0) for _ in range(COLS)])
                lines_cleared += 1
        self.update_score(lines_cleared)
        
    def update_score(self, lines):
        scoring = {1: 100, 2: 300, 3: 500, 4: 800}
        self.score += scoring.get(lines, 0)
        
    def draw_score(self, screen):
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))
        
# ================= MAIN LOOP =================
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    game = Tetris()
    fall_time = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        fall_time += clock.get_rawtime()
        clock.tick(60)

        if fall_time > 500:
            game.move_down()
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.current.x -= 1
                    if game.collision():
                        game.current.x += 1
                elif event.key == pygame.K_RIGHT:
                    game.current.x += 1
                    if game.collision():
                        game.current.x -= 1
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                elif event.key == pygame.K_UP:
                    game.current.rotate()
                    if game.collision():
                        game.current.rotate()
                        game.current.rotate()
                        game.current.rotate()

        game.draw_grid(screen)
        game.draw_piece(screen)
        game.draw_score(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
