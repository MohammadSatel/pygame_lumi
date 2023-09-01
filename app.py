import pygame
import random
import sys

pygame.init()

# Game window
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background color (space-like color)
background_color = (0, 0, 30)

# Player
player = pygame.Rect(200, 600, 50, 50)
player_color = (0, 0, 255)  # Player color is blue

# Player speed (adjust as needed)
player_speed = 5

# Rock class
class Rock:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, SCREEN_WIDTH - self.rect.width), 0)

rocks = []

# Scoring
score = 0

# Game over flag
game_over = False

# Start screen
start_screen = True
font = pygame.font.Font(None, 72)
start_text = font.render("Press SPACE to Start", True, (255, 255, 255))

# Load Rock Image
rock_image = pygame.image.load('lemi.png')  # Replace 'rock.png' with the actual image file path
rock_rect = rock_image.get_rect()

# Game loop
clock = pygame.time.Clock()
while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen = False
            game_over = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_screen = False

    screen.fill(background_color)
    screen.blit(start_text, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 50))
    pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player.left > 0:
        player.move_ip(-player_speed, 0)
    if keys[pygame.K_d] and player.right < SCREEN_WIDTH:
        player.move_ip(player_speed, 0)
    if keys[pygame.K_w] and player.top > 0:
        player.move_ip(0, -player_speed)
    if keys[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
        player.move_ip(0, player_speed)

    # Refill screen with background color
    screen.fill(background_color)

    # Draw and move rocks
    for rock in rocks:
        screen.blit(rock.image, rock.rect)
        rock.rect.move_ip(0, 5)  # Move rocks downward

    # Remove rocks that are out of screen
    rocks = [rock for rock in rocks if rock.rect.top <= SCREEN_HEIGHT]

    # Spawn new rocks at random positions from the top
    if random.randint(0, 100) < 5:
        rock = Rock(rock_image)
        rocks.append(rock)

    # Check for collisions with rocks
    for rock in rocks:
        if player.colliderect(rock.rect):
            game_over = True

    # Calculate and display score
    score += 1
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw the player
    pygame.draw.rect(screen, player_color, player)

    pygame.display.update()
    clock.tick(60)  # Limit frame rate to 60 FPS

# Game over screen
font = pygame.font.Font(None, 72)
game_over_text = font.render("Game Over", True, (255, 0, 0))
score_text = font.render(f"Score: {score}", True, (255, 0, 0))
screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
screen.blit(score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Event handler
pygame.quit()
sys.exit()
