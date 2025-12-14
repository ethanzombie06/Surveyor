import pygame, enemies, weapons

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

camera_offset = pygame.Vector2(0, 0)
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

alive_enemies = [enemies.enemy(10, pygame.Vector2(0, 0)),enemies.enemy(10, pygame.Vector2(100, 0))] 

active_weapons = [weapons.radar(5, 200, center)]

# Timer for radar tick effect
radar_tick_timer = 0

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    

    keys = pygame.key.get_pressed()

    # move camera when player "moves"
    speed = 200  # world units per second
    if keys[pygame.K_w]: camera_offset.y -= speed * dt
    if keys[pygame.K_s]: camera_offset.y += speed * dt
    if keys[pygame.K_a]: camera_offset.x -= speed * dt
    if keys[pygame.K_d]: camera_offset.x += speed * dt

    for i in active_weapons:
        if isinstance(i, weapons.radar):
            # Radar follows player (center in world coordinates)
            i.postion = camera_offset + center
            # draw radar as a semi-transparent green circle
            radar_surface = pygame.Surface((i.size * 2, i.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(radar_surface, (0, 255, 0, 128), (i.size, i.size), i.size)
            radar_screen_pos = i.postion - camera_offset
            radar_pos = (radar_screen_pos.x - i.size, radar_screen_pos.y - i.size)
            screen.blit(radar_surface, radar_pos)

    # Radar tick: check collision and apply effect every 0.25s, only for radar weapons
    radar_tick_timer += dt
    radar_tick_this_frame = False
    for weapon in active_weapons:
        if isinstance(weapon, weapons.radar):
            if radar_tick_timer >= 0.4:
                radar_tick_this_frame = True
                enemies_to_remove = []
                for enemy in alive_enemies:
                    radar_world_pos = weapon.postion
                    if (radar_world_pos - enemy.pos).length() <= (weapon.size + enemy.size):
                        weapon.damage_target(enemy)
                        if enemy.health <= 0:
                            enemies_to_remove.append(enemy)
                for enemy in enemies_to_remove:
                    alive_enemies.remove(enemy)
                radar_tick_timer = 0
    
    # draw enemy (world_pos - camera_offset)
    for enemy in alive_enemies:
        enemy_screen_pos = enemy.pos - camera_offset
        pygame.draw.circle(screen, "red", enemy_screen_pos, 10)
        # Draw blue circle at enemy on tick frame only, if collides this frame
        if radar_tick_this_frame:
            for weapon in active_weapons:
                if isinstance(weapon, weapons.radar):
                    radar_world_pos = weapon.postion
                    if (radar_world_pos - enemy.pos).length() <= (weapon.size + enemy.size):
                        pygame.draw.circle(screen, "blue", enemy_screen_pos, 15)

    # draw player in the center
    pygame.draw.circle(screen, "white", center, 20)



    pygame.display.flip()

pygame.quit()
