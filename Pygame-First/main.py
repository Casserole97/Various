import pygame, math

# game settings
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

COLOR_BLACK = 0, 0, 0
COLOR_WHITE = 255, 255, 255
COLOR_GREEN = 166, 206, 57
COLOR_BLUE = 57, 166, 206

GROUND_RECT = (0, 340, 640, 140)

isJump = False
jumpCount = 5

# classes
class Cords():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, amount):
        if isinstance(amount, Cords):
            self.x += amount.x
            self.y += amount.y
        else:
            self.x += amount
            self.y += amount

    def set_zero(self):
        self.x = 0
        self.y = 0

class Actor():
    def __init__(self, texture):
        self.position = Cords()
        self.velocity = Cords()
        self.texture = texture

    def get_bounds(self):
        return self.texture.get_rect().width, self.texture.get_rect().height

class Player(Actor):
        def control(self, speed=2, gravity=8):
            
            keys = pygame.key.get_pressed()

            midair = self.position.y < 340 - self.get_bounds()[1]

            global isJump
            global jumpCount
   
            ball.velocity.set_zero()

            if keys[pygame.K_a] and self.position.x > 0:
                self.position.x += self.velocity.x - speed
            if keys[pygame.K_d] and self.position.x < 640 - self.get_bounds()[0]:
                self.position.x += self.velocity.x + speed
                
            if not isJump:
                if midair:
                    self.position.y += gravity

                if keys[pygame.K_s] and self.position.y < 340 - self.get_bounds()[1]:
                    self.position.y += self.velocity.y + speed
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not midair:
                        isJump = True
                        
            else:
                if jumpCount >= -5:
                    self.position.y += self.velocity.y - (jumpCount * abs(jumpCount)) * 0.5
                    jumpCount -= 0.25
                    
                else:
                    jumpCount = 5
                    isJump = False
                            

# functions
def draw():
    screen.fill(COLOR_BLUE)
    screen.fill(COLOR_GREEN, GROUND_RECT)
    screen.blit(ball.texture, (ball.position.x, ball.position.y))
    pygame.display.flip()

# initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# textures
ballTexture = pygame.image.load('ball.png')
hudFont = pygame.font.SysFont('Press Start 2P', 16)

# game objects
ball = Player(ballTexture)

# loop control and timing
gameover = False
clock = pygame.time.Clock()

# gameloop
while not gameover:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    
    clock.tick(60)
    ball.control()
    draw()

pygame.quit()

