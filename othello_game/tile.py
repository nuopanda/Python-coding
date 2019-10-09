class Tile:
    def __init__(self, col, row):
        """constructor of Tile object"""
        self.col = col
        self.row = row
        self.current_state = "BACKGROUND"  # default state is "BACKGROUND"
        self.SPACING = 100
        self.DISTANCE = 50
        self.RADIUS = 90

    def display(self):
        """draw ellipse on processing"""
        if self.current_state == "PLAYER":
            stroke(0, 0, 0)
            fill(0, 0, 0)
            ellipse(self.col * self.SPACING + self.DISTANCE, self.row *
                    self.SPACING + self.DISTANCE, self.RADIUS, self.RADIUS)
        elif self.current_state == "AI":
            stroke(0, 0, 0)
            fill(255, 255, 255)
            ellipse(self.col * self.SPACING + self.DISTANCE, self.row *
                    self.SPACING + self.DISTANCE, self.RADIUS, self.RADIUS)
        else:
            noStroke()
            fill(0, 128, 0)
            ellipse(self.col * self.SPACING + self.DISTANCE, self.row *
                    self.SPACING + self.DISTANCE, self.RADIUS, self.RADIUS)

    def change_state(self, tile_state):
        """given the new tile_state, change it to the current_state of tile"""
        self.current_state = tile_state
