import pygame


class Window:

    def __init__(self, win_height, win_width):
        """Method of initialization class Window; win_height - height of screen, win_width - width of screen"""
        self.win_height = win_height
        self.win_width = win_width
        self.win = pygame.display.set_mode((win_width, win_height))

    def draw(self):
        """Method of drawing background"""
        a = pygame.image.load("bg2.png")
        self.win.blit(a, (0, 0))

    def gameover(self):
        """Method of drawing "Game Over" when game end"""
        f = pygame.image.load("go8.png")
        self.win.blit(f, (100, 50))

    def score(self, q):
        """Method of drawing score"""
        self.q = q
        font_1 = pygame.font.SysFont('Courier New', 50)
        this_sentence = font_1.render('Score :', True, (0, 0, 0))
        self.win.blit(this_sentence, (5, 5))
        font_2 = pygame.font.SysFont('Courier New', 50)
        this_sentence = font_2.render(str(self.q), True, (0, 0, 0))
        self.win.blit(this_sentence, (130, 5))
