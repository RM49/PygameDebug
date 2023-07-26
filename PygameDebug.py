import pygame

class Debug():
    def __init__(self, screen, colour, fontsize):
        pygame.init()
        self.screen = screen
        self.colour = colour
        self.fontsize = fontsize
        self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)
        self.debugs = []

    def Update(self, *args):
        y = 0
        for x in args:
            text = self.font.render(str(x[0]) + ": " + str(x[1]), True, self.colour)
            self.screen.blit(text, (0, y))
            y += self.fontsize
