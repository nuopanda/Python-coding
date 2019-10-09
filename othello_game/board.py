class Board:
    def __init__(self, WIDTH, HEIGHT, SPACING):
        """constructor of Board object"""
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING

    def board_display(self):
        """draw lines of board"""
        # draw the horizontal line
        strokeWeight(2)
        for i in range(1, self.HEIGHT//self.SPACING + 1):
            line(0, self.SPACING*i, self.WIDTH, self.SPACING*i)
        # draw the vertical line
        for i in range(1, self.WIDTH//self.SPACING + 1):
            line(self.SPACING*i, 0, self.SPACING*i, self.HEIGHT)
