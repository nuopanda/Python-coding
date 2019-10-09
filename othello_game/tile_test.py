from tile import Tile


def test_constructor():
    """test Tile constructor"""
    tile = Tile(1, 1)
    assert tile.col == 1
    assert tile.row == 1
    assert tile.current_state == "BACKGROUND"
    assert tile.SPACING == 100
    assert tile.DISTANCE == 50
    assert tile.RADIUS == 90


def test_change_state():
    """test Tile change_state method"""
    tile = Tile(1, 1)
    tile.change_state("PLAYER")
    assert tile.current_state == "PLAYER"
