import pygame


class Column():

    def __init__(self, win, yloc, xloc, ysize):
        """Method of initialization basic class Column; win - screen, yloc - Y coordinate of left corner of column,
        xloc - X coordinate of left corner of column, ysize - height of column"""
        self.yloc = yloc
        self.xloc = xloc
        self.ysize = ysize
        self.win = win

    def move(self):
        self.xloc -= 10
        if self.xloc < 0:
            return True
        else:
            return False

    def draw(self):
        pass


class GreenColumn(Column):
    """Hereditary class which has green colour and medium width"""

    def __init__(self, win, yloc, xloc, ysize):
        """Method of initialization hereditary class GreenColumn; win - screen,
         yloc - Y coordinate of left corner of column,
         xloc - X coordinate of left corner of column, ysize - height of column"""
        Column.__init__(self, win, yloc, xloc, ysize)

    # def move(self):
    #     """Method of moving green column"""
    #     self.move()

    def draw(self):
        """Method of drawing green column"""
        pygame.draw.rect(self.win, (0, 255, 0), (self.xloc, self.yloc, 50, self.ysize))


class RedColumn(Column):
    """Hereditary class which has red colour and big width"""

    def __init__(self, win, yloc, xloc, ysize):
        """Method of initialization hereditary class RedColumn; win - screen,
         yloc - Y coordinate of left corner of column,
        xloc - X coordinate of left corner of column, ysize - height of column"""
        Column.__init__(self, win, yloc, xloc, ysize)

    #def move(self):
        #"""Method of moving red column"""

    def draw(self):
        """Method of drawing red column"""
        pygame.draw.rect(self.win, (255, 0, 0), (self.xloc, self.yloc, 75, self.ysize))


class BlueColumn(Column):
    """Hereditary class which has blue colour and small width"""

    def __init__(self, win, yloc, xloc, ysize):
        """Method of initialization hereditary class BlueColumn; win - screen,
        yloc - Y coordinate of left corner of column,
        xloc - X coordinate of left corner of column, ysize - height of column"""
        Column.__init__(self, win, yloc, xloc, ysize)

    # def move(self):
    #     """Method of moving blue column"""
    #     self.move()

    def draw(self):
        """Method of drawing blue column"""
        pygame.draw.rect(self.win, (0, 0, 255), (self.xloc, self.yloc, 25, self.ysize))
