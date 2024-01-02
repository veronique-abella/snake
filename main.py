import pygame as pg
import random

pg.init()

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 20
FPS = 10

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Snake Game')

clock = pg.time.Clock()

def afficher_score(score):
    font = pg.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def jeu_snake():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    score = 0
    food = (random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE,
            random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pg.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
                elif event.key == pg.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pg.K_DOWN and direction != (0, -1):
                    direction = (0, 1)

        snake_head = (snake[0][0] + direction[0] * TILE_SIZE, snake[0][1] + direction[1] * TILE_SIZE)

        if (snake_head[0] < 0 or snake_head[0] >= WIDTH or
            snake_head[1] < 0 or snake_head[1] >= HEIGHT):
            running = False

        if snake_head in snake[1:]:
            running = False

        snake.insert(0, snake_head)

        if snake_head == food:
            score += 1
            food = (random.randint(0, (WIDTH - TILE_SIZE) // TILE_SIZE) * TILE_SIZE,
                    random.randint(0, (HEIGHT - TILE_SIZE) // TILE_SIZE) * TILE_SIZE)
        else:
            snake.pop()

        screen.fill(BLACK)
        for segment in snake:
            pg.draw.rect(screen, GREEN, (segment[0], segment[1], TILE_SIZE, TILE_SIZE))
        pg.draw.rect(screen, RED, (food[0], food[1], TILE_SIZE, TILE_SIZE))
        afficher_score(score)
        pg.display.flip()

        clock.tick(10)

    pg.quit()

if __name__ == "__main__":
    jeu_snake()
