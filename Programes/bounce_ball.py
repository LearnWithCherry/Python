import pygame, sys
pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLUE  = (50, 100, 220)

x, y = WIDTH // 2, HEIGHT // 2
vx, vy = 5, 4               # velocity in x and y
radius = 25

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update position
    x += vx
    y += vy

    # Bounce on walls
    if x - radius <= 0 or x + radius >= WIDTH:
        vx = -vx
    if y - radius <= 0 or y + radius >= HEIGHT:
        vy = -vy

    # Draw
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
