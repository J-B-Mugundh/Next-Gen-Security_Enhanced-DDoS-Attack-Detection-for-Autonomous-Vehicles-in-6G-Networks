import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
HORIZONTAL_LANES = 4
VERTICAL_LANES = 4
LANE_WIDTH = SCREEN_WIDTH // (HORIZONTAL_LANES + VERTICAL_LANES)
VEHICLE_WIDTH = 30
VEHICLE_HEIGHT = 60
VEHICLE_SPEED = 3
DDOS_ATTACK_FREQUENCY = 0.01
DDOS_DURATION = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Autonomous Vehicle DDoS Attack Simulation")

# Vehicle class
class Vehicle:
    def __init__(self, lane, orientation):
        self.lane = lane
        self.orientation = orientation
        if orientation == "horizontal":
            self.x = lane * LANE_WIDTH + (LANE_WIDTH - VEHICLE_WIDTH) // 2
            self.y = SCREEN_HEIGHT
        else:
            self.x = SCREEN_WIDTH
            self.y = lane * LANE_WIDTH + (LANE_WIDTH - VEHICLE_HEIGHT) // 2
        self.speed = VEHICLE_SPEED
        self.color = GREEN
        self.crashed = False

    def move(self):
        if not self.crashed:
            if self.orientation == "horizontal":
                self.y -= self.speed
            else:
                self.x -= self.speed

    def draw(self):
        if self.orientation == "horizontal":
            pygame.draw.rect(screen, self.color, (self.x, self.y, VEHICLE_WIDTH, VEHICLE_HEIGHT))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, VEHICLE_HEIGHT, VEHICLE_WIDTH))

# Check for collisions between vehicles
def check_collisions(vehicles):
    for i in range(len(vehicles)):
        for j in range(i + 1, len(vehicles)):
            vehicle1 = vehicles[i]
            vehicle2 = vehicles[j]

            if pygame.Rect(vehicle1.x, vehicle1.y, VEHICLE_WIDTH, VEHICLE_HEIGHT).colliderect(
                pygame.Rect(vehicle2.x, vehicle2.y, VEHICLE_WIDTH, VEHICLE_HEIGHT)
            ):
                vehicle1.color = RED
                vehicle1.crashed = True
                vehicle2.color = RED
                vehicle2.crashed = True

# Initialize lanes and vehicles
lanes = [lane for lane in range(HORIZONTAL_LANES + VERTICAL_LANES)]
vehicles = []
for lane in range(HORIZONTAL_LANES):
    vehicles.append(Vehicle(lane, "horizontal"))
for lane in range(HORIZONTAL_LANES, HORIZONTAL_LANES + VERTICAL_LANES):
    vehicles.append(Vehicle(lane, "vertical"))

# DDoS Attack class
class DDoSAttack:
    def __init__(self):
        self.active = False
        self.duration = 0

    def activate(self):
        self.active = True
        self.duration = DDOS_DURATION

    def deactivate(self):
        self.active = False

# Initialize DDoS attack
ddos_attack = DDoSAttack()

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Simulate DDoS attack
    if not ddos_attack.active and random.random() < DDOS_ATTACK_FREQUENCY:
        vehicle = random.choice(vehicles)
        vehicle.color = RED
        vehicle.crashed = True
        ddos_attack.activate()

    if ddos_attack.active:
        ddos_attack.duration -= 1
        if ddos_attack.duration <= 0:
            ddos_attack.deactivate()

    # Check for collisions
    check_collisions(vehicles)

    # Move and draw vehicles
    for vehicle in vehicles:
        vehicle.move()
        vehicle.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
