import pygame
import sys
import random
from collections import deque

# --- Constants ---
TILE_SIZE = 40

WALL = 1
PATH = 0
GOAL = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W

# --- Prompt user for any size and round up to odd values internally ---
def get_dimension_input(prompt, min_value=5):
    while True:
        try:
            val = int(input(prompt))
            if val >= min_value:
                return val + 1 if val % 2 == 0 else val
            else:
                print(f"Please enter a number >= {min_value}")
        except ValueError:
            print("Please enter a valid number.")

# --- Maze Generation ---
def generate_maze(width, height):
    maze = [[WALL for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        visited[y][x] = True
        maze[y][x] = PATH
        dirs = DIRS[:]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx * 2, y + dy * 2
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and not visited[ny][nx]:
                maze[y + dy][x + dx] = PATH
                carve(nx, ny)

    carve(1, 1)

    # --- Place goal at farthest reachable point from start ---
    def bfs_farthest_point(maze, start_x, start_y):
        visited = [[False for _ in row] for row in maze]
        queue = deque()
        queue.append((start_x, start_y, 0))
        visited[start_y][start_x] = True
        farthest = (start_x, start_y, 0)

        while queue:
            x, y, dist = queue.popleft()
            farthest = (x, y, dist)
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if not visited[ny][nx] and maze[ny][nx] == PATH:
                        visited[ny][nx] = True
                        queue.append((nx, ny, dist + 1))

        return farthest[:2]

    goal_x, goal_y = bfs_farthest_point(maze, 1, 1)
    maze[goal_y][goal_x] = GOAL
    print(f"Goal placed at: ({goal_x}, {goal_y})")

    # --- Add false paths (controlled loops only) ---
    def add_extra_paths(maze, attempts=width * height // 5):
        for _ in range(attempts):
            x = random.randint(1, width - 2)
            y = random.randint(1, height - 2)

            if maze[y][x] == WALL:
                # Vertical wall between two paths
                if x % 2 == 1 and y % 2 == 0:
                    if maze[y - 1][x] == PATH and maze[y + 1][x] == PATH:
                        maze[y][x] = PATH
                # Horizontal wall between two paths
                elif x % 2 == 0 and y % 2 == 1:
                    if maze[y][x - 1] == PATH and maze[y][x + 1] == PATH:
                        maze[y][x] = PATH

    add_extra_paths(maze)
    return maze

# --- Maze Rendering ---
def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if maze[y][x] == WALL:
                pygame.draw.rect(screen, BLACK, rect)
            elif maze[y][x] == GOAL:
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

def draw_player(pos):
    rect = pygame.Rect(pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, BLUE, rect)

def is_valid_move(x, y, maze):
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] != WALL

# --- Game Setup ---
cols = get_dimension_input("Enter maze width (>= 5): ")
rows = get_dimension_input("Enter maze height (>= 5): ")
WINDOW_WIDTH = TILE_SIZE * cols
WINDOW_HEIGHT = TILE_SIZE * rows
print(f"Creating maze {cols} x {rows}...")
maze = generate_maze(cols, rows)
player_pos = [1, 1]

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Random Maze Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# --- Main Game Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -1
    elif keys[pygame.K_RIGHT]:
        dx = 1
    elif keys[pygame.K_UP]:
        dy = -1
    elif keys[pygame.K_DOWN]:
        dy = 1

    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy

    if is_valid_move(new_x, new_y, maze):
        player_pos = [new_x, new_y]

    screen.fill(WHITE)
    draw_maze(maze)
    draw_player(player_pos)

    if maze[player_pos[1]][player_pos[0]] == GOAL:
        text = font.render("You Win!", True, (255, 0, 0))
        screen.blit(text, (WINDOW_WIDTH // 2 - 80, WINDOW_HEIGHT // 2 - 24))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
