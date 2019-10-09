from board import Board
from tile import Tile
import time


class GameManager:
    def __init__(self, WIDTH, HEIGHT, SPACING):
        """constructor of GameManager object"""
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SPACING = SPACING
        self.board = Board(self.WIDTH, self.HEIGHT, self.SPACING)
        self.build_tile_matrix()
        self.black_count = 0
        self.white_count = 0
        self.black_score = 0
        self.white_score = 0
        # If true the player moves; otherwise the AI moves.
        self.is_player_turn = True

    def build_tile_matrix(self):
        """build the tile objects matrix, change first 4 tiles in middle"""
        self.tile_grid = []
        self.col_number = self.WIDTH//self.SPACING
        self.row_number = self.HEIGHT//self.SPACING
        if self.col_number < 2 or self.row_number < 2:
            return
        for i in range(self.col_number):
            self.tile_grid.append([Tile(i, j) for j in range(self.row_number)])
        # draw the initial four tiles
        # draw the two white tiles
        row_middle = (self.row_number-1)//2
        col_middle = (self.col_number-1)//2
        # use "AI" to represent white tiles
        self.tile_grid[col_middle][row_middle].change_state("AI")
        self.tile_grid[col_middle + 1][row_middle + 1].change_state("AI")
        # draw the two black tiles
        self.tile_grid[col_middle][row_middle+1].change_state("PLAYER")
        self.tile_grid[col_middle+1][row_middle].change_state("PLAYER")

    def draw_current_board(self):
        """draw the current board of tiles"""
        for col in range(self.col_number):
            for row in range(self.row_number):
                self.tile_grid[col][row].display()

    def is_on_board(self, col, row):
        """Given the col, row, check if it is on the board"""
        if (col < self.col_number and col >= 0 and
                row < self.row_number and row >= 0):
            return True
        else:
            return False

    def is_valid_tile_to_place(self, col, row, state):
        """given col and row, check if it is valid to change state of tiles"""
        if self.tile_grid[col][row].current_state != "BACKGROUND":
            return False
        if state == "PLAYER":
            oppose_state = "AI"
        elif state == "AI":
            oppose_state = "PLAYER"
        self.tiles_to_flip = []
        # check for 8 directions
        for col_dic, row_dic in [[0, 1], [0, -1], [-1, 0], [1, 0],
                                 [-1, 1], [1, -1], [1, 1], [-1, -1]]:
            count = 0
            tiles_cum = []
            curr_col = col
            curr_row = row
            curr_col += col_dic
            curr_row += row_dic
            if not self.is_on_board(curr_col, curr_row):
                continue
            while (self.tile_grid[curr_col][curr_row].current_state ==
                   oppose_state):
                tiles_cum.append([curr_col, curr_row])
                count += 1
                curr_col += col_dic
                curr_row += row_dic
                if not self.is_on_board(curr_col, curr_row):
                    break
            if not self.is_on_board(curr_col, curr_row):
                continue
            if self.tile_grid[curr_col][curr_row].current_state == state:
                if(count >= 1):
                    for cum in tiles_cum:
                        self.tiles_to_flip.append(cum)
                    continue
                else:
                    continue
        if len(self.tiles_to_flip) == 0:
            return False
        else:
            return True

    def get_all_valid_moves(self, state):
        """Given a state, get all the valid moves of the state"""
        # basically this method is for finding valid moves for AI
        # but can be modified to be used for other state
        self.all_valid_moves = []
        for col in range(self.col_number):
            for row in range(self.row_number):
                if self.is_valid_tile_to_place(col, row, state) is True:
                    self.all_valid_moves.append([col, row])

    def get_max_count_move_AI(self):
        """return the col, row of AI which can achieve the best score"""
        max_count = 0
        for col, row in self.all_valid_moves:
            self.get_fake_tile_grid()
            self.fake_tile_grid[col][row].change_state("AI")
            self.get_count()
            # two strategies for AI:
            # have the maximum count
            # if on the edge of the board, have priority
            if max_count < self.white_count:
                move_col = col
                move_row = row
                max_count = self.white_count
            elif max_count == self.white_count:
                if (col == 0 or row == 0 or
                        col == self.col_number or row == self.row_number):
                    move_col = col
                    move_row = row
        return move_col, move_row

    def get_fake_tile_grid(self):
        """generate a fake_tile_grid to mimic the current tile_grid"""
        self.fake_tile_grid = []
        for col in range(self.col_number):
            self.fake_tile_grid.append([Tile(col, row)
                                        for row in range(self.row_number)])
        for col in range(self.col_number):
            for row in range(self.row_number):
                self.fake_tile_grid[col][row].change_state(
                    self.tile_grid[col][row].current_state)

    def get_count(self):
        """score the fake_tile_grid"""
        self.white_count = 0
        self.black_count = 0
        for col in range(self.col_number):
            for row in range(self.row_number):
                if self.fake_tile_grid[col][row].current_state == "PLAYER":
                    self.black_count += 1
                elif self.fake_tile_grid[col][row].current_state == "AI":
                    self.white_count += 1

    def have_remaining_value_move(self, state):
        """Given the state, check if it has valid move"""
        # if the state has no all_valid_moves, then the opponent get the turn
        # otherwise wait for the mousekey
        self.get_all_valid_moves(state)
        if len(self.all_valid_moves) == 0 or self.all_valid_moves is None:
            return False
        else:
            return True

    def flip_tile(self, tile_state):
        """Given the state to flip, flip the tiles to that state"""
        for col, row in self.tiles_to_flip:
            self.tile_grid[col][row].change_state(tile_state)

    def is_have_background_move(self):
        """check if there is still empty place to place tiles"""
        for col in range(self.col_number):
            for row in range(self.row_number):
                if self.tile_grid[col][row].current_state == "BACKGROUND":
                    return True
                else:
                    continue
        return False

    def is_game_ended(self):
        """check if the game is ended"""
        if self.is_have_background_move() is True:
            if (self.have_remaining_value_move("AI") is False and
                    self.have_remaining_value_move("PLAYER") is False):
                return True
            else:
                return False
        elif self.is_have_background_move() is False:
            return True

    def display_game_ending(self):
        """display the ending message"""
        fill(255, 0, 0)
        textSize(30)
        self.white_score = 0
        self.black_score = 0
        for col in range(self.col_number):
            for row in range(self.row_number):
                if self.tile_grid[col][row].current_state == "AI":
                    self.white_score += 1
                elif self.tile_grid[col][row].current_state == "PLAYER":
                    self.black_score += 1
        if (self.black_score > self.white_score):
            ending = "YOU WIN!\nYou have " + \
                str(self.black_score)+" TILES!"
            text(ending, self.WIDTH/2 - 140, self.HEIGHT/2-20)
        elif (self.black_score < self.white_score):
            ending = "You lose.\nComputer has " + \
                str(self.white_score) + " TILES!"
            text(ending, self.WIDTH/2-140, self.HEIGHT/2-20)
        elif (self.black_score == self.white_score):
            ending = "      GAME OVER!\nThey all have " + \
                str(self.white_score) + " TILES!"
            text(ending, self.WIDTH/2 - 140, self.HEIGHT/2-20)

    def is_any_move_available(self):
        """check if it's ai's move"""
        if self.is_game_ended():
            return False
        if self.is_player_turn is False:
            self.ai_move()
        return not self.is_game_ended()

    def player_move(self, col, row):
        """given the col, row, do the player's move"""
        if self.is_game_ended():
            return
        if self.is_valid_tile_to_place(col, row, "PLAYER"):
            self.tile_grid[col][row].change_state("PLAYER")
            self.flip_tile("PLAYER")

    def ai_move(self):
        """do the ai's move"""
        # first : player move, then ai move (ai has remaining value move)
        # second: ai move, ai move (ai has remaining, player not has remaining)
        # third: player move, player move (ai not has remaining, player has)
        # four: game ended
        if self.is_game_ended() is True:
            return
        # if ai can make a move
        elif self.have_remaining_value_move("AI") is True:
            print("computer's turn")
            time.sleep(1)
            max_col, max_row = self.get_max_count_move_AI()
            if self.is_valid_tile_to_place(max_col, max_row, "AI"):
                self.tile_grid[max_col][max_row].change_state("AI")
                self.flip_tile("AI")
        # if ai cannot make a move
        elif self.have_remaining_value_move("AI") is False:
            if (self.is_game_ended is False and
                    self.have_remaining_value_move("PLAYER") is True):
                self.is_player_turn = True
                print("no valid move for computer")
                return
        # Check if player can make a move. If not, AI keeps moving.
        if self.is_game_ended():
            return
        elif self.have_remaining_value_move("PLAYER") is False:
            print("no valid move for player")
            self.ai_move()
        elif self.have_remaining_value_move("PLAYER") is True:
            time.sleep(3)
            print("player's turn")
            self.is_player_turn = True
