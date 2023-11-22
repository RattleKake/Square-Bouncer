import pygame

# Pygame setup
pygame.init()
GAME_WIDTH = 640
GAME_HEIGHT = 480
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Square Bouncer Scenario")
clock = pygame.time.Clock()
running = True

# Map setup
ground_height = 0
ceiling_height = 0
wall_left_width = 0
wall_right_width = 0

bouncer_x = 0
bouncer_y = 0
bouncer_width = 0
bouncer_height = 0

with open("map.sbm", "r") as file:  # Read values from files and set values
    values_array = []

    for line in file:
        values_array.append(line.strip())

    ground_height = int(values_array[0])
    ceiling_height = int(values_array[1])
    wall_left_width = int(values_array[2])
    wall_right_width = int(values_array[3])

    bouncer_x = int(values_array[4])
    bouncer_y = int(values_array[5])
    bouncer_width = int(values_array[6])
    bouncer_height = int(values_array[7])

rect_ground = pygame.Rect(0, GAME_HEIGHT - ground_height, GAME_WIDTH, GAME_HEIGHT)
rect_ceiling = pygame.Rect(0, 0, GAME_WIDTH, ceiling_height)
rect_wall_left = pygame.Rect(0, 0, wall_left_width, GAME_HEIGHT)
rect_wall_right = pygame.Rect(GAME_WIDTH - wall_right_width, 0, GAME_WIDTH, GAME_HEIGHT)

map_list = [rect_ground, rect_ceiling, rect_wall_left, rect_wall_right]

# Bouncer setup
bouncer_x = 0
bouncer_y = 0
bouncer_width = 0
bouncer_height = 0
bouncer_speed_x = 0
bouncer_speed_y = 0

with open("map.sbm", "r") as file:  # Read values from files and set values
    values_array = []

    for line in file:
        values_array.append(line.strip())

    bouncer_x = int(values_array[4])
    bouncer_y = int(values_array[5])
    bouncer_width = int(values_array[6])
    bouncer_height = int(values_array[7])
    bouncer_speed_x = int(values_array[8])
    bouncer_speed_y = int(values_array[9])

rect_bouncer = pygame.Rect(bouncer_x, bouncer_y, bouncer_width, bouncer_height)

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
color_index = 0

bouncer_speed = pygame.Vector2(bouncer_speed_x, bouncer_speed_y)

trail_list = []

while running:

    # Poll for events
    for event in pygame.event.get():

        # If the close button on the window is clicked, set running to false
        if event.type == pygame.QUIT:
            running = False

    # Fill background black
    screen.fill("black")

    # Draw maps
    for i in map_list:
        pygame.draw.rect(screen, "gray", i)

    # Draw trail
    for i in trail_list:
        pygame.draw.rect(screen, color_list[color_index], i)

    # Draw bouncer
    pygame.draw.rect(screen, color_list[color_index], rect_bouncer)
    pygame.draw.rect(screen, "white", rect_bouncer)

    # Bounce against wall
    if rect_bouncer.left <= rect_wall_left.right or rect_bouncer.right >= rect_wall_right.left:  # Bounce horizontally

        # Change color
        if color_index < len(color_list) - 1:
            color_index += 1
        else:
            color_index = 0

        # Change direction
        bouncer_speed.x *= -1

    if rect_bouncer.bottom >= rect_ground.top or rect_bouncer.top <= rect_ceiling.bottom:  # Bounce vertically

        # Change color
        if color_index < len(color_list) - 1:
            color_index += 1
        else:
            color_index = 0

        # Change direction
        bouncer_speed.y *= -1

    # Move bouncer around
    rect_bouncer.x += bouncer_speed.x
    rect_bouncer.y += bouncer_speed.y

    # Make a trail
    trail_list.append(pygame.Rect((rect_bouncer.x, rect_bouncer.y, rect_bouncer.width, rect_bouncer.height)))

    print(clock.get_fps())

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Update display every 60 ticks

# Quit the game
pygame.quit()
