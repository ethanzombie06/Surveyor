import pygame
import enemies

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

square = enemies.enemy(10, pygame.Vector2(0, 0))

camera_offset = pygame.Vector2(0, 0)
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # draw player in the center
    pygame.draw.circle(screen, "white", center, 20)

    keys = pygame.key.get_pressed()

    # move camera when player "moves"
    speed = 200  # world units per second
    if keys[pygame.K_w]: camera_offset.y -= speed * dt
    if keys[pygame.K_s]: camera_offset.y += speed * dt
    if keys[pygame.K_a]: camera_offset.x -= speed * dt
    if keys[pygame.K_d]: camera_offset.x += speed * dt

    # draw enemy (world_pos - camera_offset)
    pygame.draw.circle(screen, "red", square.pos - camera_offset, 10)

    pygame.display.flip()

pygame.quit()
