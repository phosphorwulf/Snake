"""
  _________  __  __ _____  _____   ______ __  __ _____  ______ __ __ __ __  __ __     ______
  \_  ___  // / / // __  // ____\ \ __  // / / // __  // __  // // // // / / // /    / ____/
   / /__/ // /_/ // / / // /__   / /_/ // /_/ // / / // /_/ // // // // / / // /    / /__
  / _____// __  // / / / \___ \ / ____// __  // / / // _  _// // // // / / // /    / ___/
 / /     / / / // /_/ /_____/ // /    / / / // /_/ // / \ \ \ V  V // /_/ // /___ / /
/_/     /_/ /_//_____//______//_/    /_/ /_//_____//_/  \_\ \__/\_/\_____//_____//_/
"""
import pygame
import random

pygame.init()

WHITE, BLACK, RED, GREEN, YELLOW = (255,255,255), (0,0,0), (255,0,0), (0,255,0), (255,255,0)

RES = WIDTH, HEIGHT = 600, 400

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

def print_score(score):
    text = score_font.render('Score: ' + str(score), True, YELLOW)
    game_display.blit(text, [0,0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        head = (len(snake_pixels)-1)
        if pixel == snake_pixels[head]:
            pygame.draw.rect(game_display, RED, [pixel[0], pixel[1], snake_size, snake_size])
        elif pixel == snake_pixels[0] and len(snake_pixels) > 1:
            pygame.draw.rect(game_display, YELLOW, [pixel[0], pixel[1], snake_size, snake_size])
        else:
            pygame.draw.rect(game_display, GREEN, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():

    game_over = False
    game_close = False

    x = WIDTH/2
    y = HEIGHT/2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1
    snake_direction = ''

    egg_x = round(random.randrange(0, WIDTH -snake_size) / 10.0) * 10.0
    egg_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(BLACK)
            game_over_message = message_font.render('Game Over', True, RED)
            game_display.blit(game_over_message, [WIDTH / 3, HEIGHT / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction != 'East':
                    snake_direction = 'West'
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT and snake_direction != 'West':
                    snake_direction = 'East'
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP and snake_direction != 'South':
                    snake_direction = 'North'
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN and snake_direction != 'North':
                    snake_direction = 'South'
                    x_speed = 0
                    y_speed = snake_size

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(BLACK)
        pygame.draw.rect(game_display, WHITE, [egg_x, egg_y, snake_size, snake_size])

        snake_pixels.append([x,y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == egg_x and y == egg_y:
            egg_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10.0
            egg_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()
