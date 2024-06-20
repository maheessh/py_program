import pygame
import time

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Car Game')

# Load car image
car_image = pygame.image.load('car.png')
car_width = car_image.get_width()
car_height = car_image.get_height()

# Car initial position
x = (screen_width * 0.45)
y = (screen_height * 0.8)
x_change = 0
y_change = 0

# Headlights status
headlights_on = False

# Turn signals status
left_signal_on = False
right_signal_on = False

# Function to draw car with lights
def draw_car(x, y):
    screen.blit(car_image, (x, y))

    if headlights_on:
        # Draw headlights
        pygame.draw.polygon(screen, white, [(x + 10, y), (x + 30, y - 100), (x + 70, y - 100), (x + 90, y)])

    if left_signal_on:
        # Draw left turn signal
        pygame.draw.circle(screen, yellow, (x, y + car_height // 2), 10)

    if right_signal_on:
        # Draw right turn signal
        pygame.draw.circle(screen, yellow, (x + car_width, y + car_height // 2), 10)

# Main game loop
running = True
clock = pygame.time.Clock()
car_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key down events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -car_speed
                left_signal_on = True
            elif event.key == pygame.K_RIGHT:
                x_change = car_speed
                right_signal_on = True
            elif event.key == pygame.K_UP:
                y_change = -car_speed
            elif event.key == pygame.K_DOWN:
                y_change = car_speed
            elif event.key == pygame.K_h:
                headlights_on = not headlights_on

        # Key up events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
                left_signal_on = False
            elif event.key == pygame.K_RIGHT:
                x_change = 0
                right_signal_on = False
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    x += x_change
    y += y_change

    screen.fill(black)
    draw_car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
