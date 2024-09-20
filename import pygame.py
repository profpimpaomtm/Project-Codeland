import pygame
import math

# Constants
WIDTH, HEIGHT = 1080, 1080
BACKGROUND_COLOR = (255, 255, 255)
PENDULUM_COLOR_LEFT = (119, 151, 189)  # #7797bd
PENDULUM_COLOR_RIGHT = (30, 49, 72)    # #1e3148
FPS = 60
GRAVITY = 9.81

# Pendulum Class
class Pendulum:
    def __init__(self, origin, length, mass, angle, color):
        self.origin = origin
        self.length = length
        self.mass = mass
        self.angle = angle
        self.omega = 0  # Angular velocity
        self.color = color
        self.x = self.origin[0] + self.length * math.sin(self.angle)
        self.y = self.origin[1] + self.length * math.cos(self.angle)

    def update(self):
        # Calculate angular acceleration
        alpha = (-GRAVITY / self.length) * math.sin(self.angle)
        self.omega += alpha / FPS
        self.angle += self.omega / FPS
        self.x = self.origin[0] + self.length * math.sin(self.angle)
        self.y = self.origin[1] + self.length * math.cos(self.angle)

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.origin, (self.x, self.y), 2)
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.mass))

# Function to display the starter page
def starter_page():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pendulum Collision Simulation Starter Page')

    font = pygame.font.Font(None, 36)
    
    mass1 = 20
    mass2 = 20
    angle1 = math.pi / 4
    angle2 = -math.pi / 4
    
    while True:
        screen.fill(BACKGROUND_COLOR)

        # Display instructions
        instructions = [
            "Use LEFT/RIGHT arrows to adjust mass of Pendulum 1 (current: {})".format(mass1),
            "Use UP/DOWN arrows to adjust mass of Pendulum 2 (current: {})".format(mass2),
            "Press SPACE to start simulation."
        ]
        
        for i, text in enumerate(instructions):
            label = font.render(text, True, (0, 0, 0))
            screen.blit(label, (50, 50 + i * 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mass1 = max(1, mass1 - 1)  # Decrease mass1
                if event.key == pygame.K_RIGHT:
                    mass1 += 1  # Increase mass1
                if event.key == pygame.K_UP:
                    mass2 += 1  # Increase mass2
                if event.key == pygame.K_DOWN:
                    mass2 = max(1, mass2 - 1)  # Decrease mass2
                if event.key == pygame.K_SPACE:
                    return mass1, mass2, angle1, angle2  # Start simulation

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

# Main Function
def main():
    mass1, mass2, angle1, angle2 = starter_page()
    
    # Set up simulation
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pendulum Collision Simulation')
    clock = pygame.time.Clock()

    origin = (WIDTH // 2, HEIGHT // 4)  # Shared origin for both pendulums

    pendulum1 = Pendulum(origin, 300, mass1, angle1, PENDULUM_COLOR_LEFT)
    pendulum2 = Pendulum(origin, 300, mass2, angle2, PENDULUM_COLOR_RIGHT)

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return main()  # Return to the menu

        # Update pendulums
        pendulum1.update()
        pendulum2.update()

        # Collision detection (basic)
        distance = math.sqrt((pendulum1.x - pendulum2.x) ** 2 + (pendulum1.y - pendulum2.y) ** 2)
        if distance < (pendulum1.mass + pendulum2.mass):  # Simplified collision check
            # Handle collision response (exchange velocities)
            pendulum1.omega, pendulum2.omega = (
                pendulum2.omega * (pendulum2.mass / pendulum1.mass),
                pendulum1.omega * (pendulum1.mass / pendulum2.mass),
            )

        # Drawing
        screen.fill(BACKGROUND_COLOR)
        pendulum1.draw(screen)
        pendulum2.draw(screen)

        # Display message to return to menu
        font = pygame.font.Font(None, 36)
        label = font.render("Press esc to go back to main menu", True, (0, 0, 0))
        screen.blit(label, (WIDTH // 3, HEIGHT // 8))

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
