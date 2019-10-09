from game_manager import GameManager
import re
import time

WIDTH = 800
HEIGHT = 800
SPACING = 100
game_manager = GameManager(WIDTH, HEIGHT, SPACING)
show_dialog = False


def setup():
    """set up the board"""
    size(WIDTH, HEIGHT)
    background(0, 128, 0)
    game_manager.board.board_display()
    game_manager.draw_current_board()
    game_manager.is_player_turn = True
    print("player's turn")


def draw():
    """draw the current board or input play's name if wins"""
    global show_dialog
    if show_dialog is True:
        name_input = input('enter your name')
        if name_input:
            write_score_txt(name_input)
            noLoop()
    else:
        if game_manager.is_any_move_available() is True:
            game_manager.draw_current_board()
        if game_manager.is_game_ended():
            game_manager.draw_current_board()
            game_manager.display_game_ending()
            show_dialog = True


def mousePressed():
    """if mousePressed, play's move"""
    if game_manager.is_player_turn is False:
        return
    if mousePressed:
        x = mouseX
        y = mouseY
        col = x//SPACING
        row = y//SPACING
        if game_manager.is_valid_tile_to_place(col, row, "PLAYER") is False:
            return
    game_manager.player_move(col, row)
    # At the very last line, flip the flag for is_player_turn.
    game_manager.is_player_turn = False
    game_manager.draw_current_board()
    return


def input(self, message=''):
    """set up the input dialog"""
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def write_score_txt(name_input):
    """Given player's name, add the name and the score into txt,
    sort the list according to the score"""
    name_score = []
    name_score.append(name_input)
    name_score.append(str(game_manager.black_score))
    content_add = ' '.join(name_score)+'\n'
    f = open('scores.txt', 'r+')
    count = 0
    max_score = 0
    lines_content = []
    while True:
        current_line = f.readline()
        lines_content.append(current_line)
        count += 1
        if not current_line:  # no line any more
            f.readline()
            f.write(content_add)
            f.close()
            break
        else:
            score_list = re.findall(r'\s+([0-9]+$)', current_line)
            score = int(score_list[0])
            # use the following code if want to sort by score
            # if score < game_manager.black_score:
            #     f.seek(0)
            #     contents = f.readlines()
            #     f.close()
            #     contents.insert(count-1, content_add)
            #     f = open('scores.txt', 'w+')
            #     contents = "".join(contents)
            #     f.write(contents)
            #     f.close()
            #     break
            max_score = max(max_score, score)
    if max_score < game_manager.black_score:
        lines_content.insert(0, content_add)
        f = open('scores.txt', 'w+')
        contents = "".join(lines_content)
        f.write(contents)
        f.close()
