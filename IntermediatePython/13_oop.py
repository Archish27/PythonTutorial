import pygame
import random

WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World!")
clock = pygame.time.Clock()

class Blob:

    #self is similar to this
    def __init__(self,color=RED):
        self.x = random.randrange(0,WIDTH) #WIDTH = 800
        self.y = random.randrange(0,HEIGHT) #HEIGHT = 600
        self.size = random.randrange(4,8)
        self.color=color

    def move(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x<0: self.x = 0
        elif self.x>WIDTH: self.x = WIDTH

        if self.y<0: self.y = 0
        elif self.y>HEIGHT: self.y = HEIGHT

    def draw_environment(blob):
        game_display.fill(WHITE)
        pygame.draw.circle(game_display,blob.color, [blob.x,blob.y],blob.size00)
        pygame.display.update()

    def main():
        red_blob = Blob(RED)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User Exited!")
                    pygame.quit()
                    quit()
            draw_environment(red_blob)
            clock.tick(60)

if __name__=="__init__":
    main()  
            









        





    
