import pygame
from random import randint
from Filec2 import GreenColumn
from Filec2 import RedColumn
from Filec2 import BlueColumn
from Fileb1 import Bird
from Filew import Window


class Game():

    def __init__(self):
        """Method of initialization of class Game"""
        self.score = 0
        self.y = 100
        self.window = Window(500, 600)
        self.a = False
        self.c = False
        self.d = False
        self.p = 0
        self.run = True
        self.flag = True
        self.yloc1 = randint(250, 450)
        self.xloc1 = 600
        self.ysize1 = 500 - self.yloc1
        self.yloc2 = self.yloc1 - 100
        self.ysize2 = self.yloc2
        self.xloc2 = self.xloc1
        self.yloc3 = randint(250, 450)
        self.xloc3 = 400
        self.ysize3 = 500 - self.yloc3
        self.yloc4 = self.yloc3 - 150
        self.ysize4 = self.yloc4
        self.xloc4 = self.xloc3
        self.yloc5 = randint(250, 450)
        self.xloc5 = 200
        self.ysize5 = 500 - self.yloc5
        self.yloc6 = self.yloc5 - 50
        self.ysize6 = self.yloc6
        self.xloc6 = self.xloc5
        self.column1 = GreenColumn(self.window.win, self.yloc1, self.xloc1, self.ysize1)
        self.column2 = GreenColumn(self.window.win, 0, self.xloc2, self.ysize2)
        self.column3 = RedColumn(self.window.win, self.yloc3, self.xloc3, self.ysize3)
        self.column4 = RedColumn(self.window.win, 0, self.xloc4, self.ysize4)
        self.column5 = BlueColumn(self.window.win, self.yloc5, self.xloc5, self.ysize5)
        self.column6 = BlueColumn(self.window.win, 0, self.xloc6, self.ysize6)
        self.bird = Bird(self.window.win, self.y, self.column1.ysize)
        self.bird2 = Bird(self.window.win, self.y, self.column3.ysize)
        self.bird3 = Bird(self.window.win, self.y, self.column5.ysize)

    def init_1column(self):
        """Method of initialization of first column"""
        b = self.bird.get_y()
        self.yloc1 = randint(250, 450)
        self.xloc1 = 600
        self.ysize1 = 500 - self.yloc1
        self.yloc2 = self.yloc1 - 120
        self.ysize2 = self.yloc2
        self.xloc2 = self.xloc1
        self.column1 = GreenColumn(self.window.win, self.yloc1, self.xloc1, self.ysize1)
        self.column2 = GreenColumn(self.window.win, 0, self.xloc2, self.ysize2)
        self.bird = Bird(self.window.win, b, self.column1.ysize)

    def init_2column(self):
        """Method of initialization of second column"""
        b = self.bird2.get_y()
        self.yloc3 = randint(250, 450)
        self.xloc3 = 600
        self.ysize3 = 500 - self.yloc3
        self.yloc4 = self.yloc3 - 150
        self.ysize4 = self.yloc4
        self.xloc4 = self.xloc3
        self.column3 = RedColumn(self.window.win, self.yloc3, self.xloc3, self.ysize3)
        self.column4 = RedColumn(self.window.win, 0, self.xloc4, self.ysize4)
        self.bird2 = Bird(self.window.win, b, self.column3.ysize)

    def init_3column(self):
        """Method of initialization of third column"""
        b = self.bird3.get_y()
        self.yloc5 = randint(250, 450)
        self.xloc5 = 600
        self.ysize5 = 500 - self.yloc5
        self.yloc6 = self.yloc5 - 100
        self.ysize6 = self.yloc6
        self.xloc6 = self.xloc5
        self.column5 = BlueColumn(self.window.win, self.yloc5, self.xloc5, self.ysize5)
        self.column6 = BlueColumn(self.window.win, 0, self.xloc6, self.ysize6)
        self.bird3 = Bird(self.window.win, b, self.column5.ysize)

    def move_columns(self):
        """Method of moving all columns"""
        self.a = self.column1.move()
        self.column2.move()
        self.c = self.column3.move()
        self.column4.move()
        self.d = self.column5.move()
        self.column6.move()

    def shut_game(self):
        """Method of ending game when you close it"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def jump_birds(self):
        """Method of jumping all birds"""
        self.bird.jump()
        self.bird2.jump()
        self.bird3.jump()

    def crash_ground(self):
        """Method of checking if bird crash in ground and draw "Game over" if it is necessary"""
        self.flag = self.bird.ground()
        if not (self.flag):
            self.window.gameover()

    def draw(self):
        """Method of drawing all screen except third column"""
        self.window.draw()
        self.bird.draw()
        self.column3.draw()
        self.column4.draw()
        self.column1.draw()
        self.column2.draw()

    def draw_col56(self):
        """Method of drawing third column"""
        self.column5.draw()
        self.column6.draw()

    def crash_walls(self):
        """Method of checking if bird crash in first two columns and draw "Game over" if it is necessary"""
        if self.column1.xloc >= 50 and self.column1.xloc <= 141:
            self.flag = self.bird.crash()
            self.score += 1
            if not (self.flag):
                self.window.gameover()
        if self.column3.xloc >= 50 and self.column3.xloc <= 141:
            self.flag = self.bird2.crash()
            self.score += 1
            if not (self.flag):
                self.window.gameover()

    def crash_col56(self):
        """Method of checking if bird crash in third column and draw "Game over" if it is necessary"""
        if self.column5.xloc >= 50 and self.column5.xloc <= 141:
            self.flag = self.bird3.crash()
            self.score += 1
            if not (self.flag):
                self.window.gameover()

    def game_score(self):
        """Method of drawing score"""
        if self.flag:
            self.window.score(self.score // 10)

    def cycle(self):
        """Method which contain main cycle"""
        self.run = True
        while self.run:
            if self.a:
                self.init_1column()
            if self.c:
                self.init_2column()
            if self.d:
                self.init_3column()
            pygame.init()
            pygame.time.delay(100)
            if self.flag:
                self.move_columns()
            self.shut_game()
            if not (self.run):
                break
            if self.flag:
                self.jump_birds()
            self.crash_ground()
            self.draw()
            if self.p > 30:
                self.draw_col56()
                self.crash_col56()
            self.crash_walls()
            self.game_score()
            pygame.display.update()
            self.p = self.p + 1
        pygame.quit()
