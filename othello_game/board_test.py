from board import Board


def test_constructor():
    """test Board constructor"""
    WIDTH = 400
    HEIGHT = 400
    SPACING = 100
    board = Board(WIDTH, HEIGHT, SPACING)
    assert board.WIDTH == 400
    assert board.HEIGHT == 400
    assert board.SPACING == 100
