import pygame
import sys
import random

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Example")

# Player attributes
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Enemy attributes
enemy_width = 30
enemy_height = 30
enemy_speed = 3

# Scoring
score = 0
font = pygame.font.Font(None, 36)

# Game over screen
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render("Game Over", True, blue)
game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))

# Enemy list
enemies = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed


    # Boundary checking
    player_x = max(0, min(screen_width - player_width, player_x))
    player_y = max(0, min(screen_height - player_height, player_y))

    # Create enemies
    if len(enemies) < 5 and random.randint(1, 100) <= 5:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])

    # Move enemies and check for collisions
    for enemy in enemies:
        enemy[1] += enemy_speed
        if player_x < enemy[0] + enemy_width and player_x + player_width > enemy[0] and player_y < enemy[1] + enemy_height and player_y + player_height > enemy[1]:
            running = False
        if enemy[1] > screen_height:
            enemies.remove(enemy)
            score += 10


    # Fill the screen with white
    screen.fill(white)

    # Draw player
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, blue, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, blue)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(60)

# Game over
screen.fill(white)
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
sys.exit()
