import pygame


class Bird():

    def __init__(self, win, y, ysize):
        """Method of initialization class Bird; win - screen, y - Y coordinate of left corner of bird,
        ysize - height of column"""
        self.win = win
        self.y = y
        self.ysize = ysize

    def crash(self):
        """Method of checking if bird crash in column"""
        if self.y > 350 - self.ysize and self.y < 470 - self.ysize:
            return True
        else:
            return False

    def jump(self):
        """Method of jumping bird"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 30:
            self.y -= 30
        self.y += 10

    def ground(self):
        """Method of checking if bird crash in ground"""
        if self.y > 470:
            return False
        else:
            return True

    def get_y(self):
        """Method of getting Y coordinate of bird"""
        return self.y

    def draw(self):
        """Method of drawing bird"""
        z = pygame.image.load("bird.png")
        self.win.blit(z, (100, self.y))
