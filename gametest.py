import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500 # Window size
WHITE = (255, 255, 255) # Background color
RED = (255, 0, 0) # Player color

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Game")

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2 # see saved link for explanation
speed = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    
    # key input
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += speed

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    pygame.display.update()

pygame.quit()
