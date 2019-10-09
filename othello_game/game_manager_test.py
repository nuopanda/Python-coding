from game_manager import GameManager


def test_constructor_build_tile_matrix():
    """test GameManager constructor and build_tile_matrix"""
    game_manager = GameManager(400, 600, 100)
    assert game_manager.WIDTH == 400
    assert game_manager.HEIGHT == 600
    assert game_manager.SPACING == 100
    assert len(game_manager.tile_grid) == 4
    assert len(game_manager.tile_grid[0]) == 6
    assert game_manager.tile_grid[1][2].current_state == "AI"
    assert game_manager.tile_grid[2][2].current_state == "PLAYER"
    assert game_manager.tile_grid[1][3].current_state == "PLAYER"
    assert game_manager.tile_grid[2][3].current_state == "AI"
    game_manager = GameManager(200, 200, 100)
    assert game_manager.WIDTH == 200
    assert game_manager.HEIGHT == 200
    assert game_manager.SPACING == 100
    assert len(game_manager.tile_grid) == 2
    assert len(game_manager.tile_grid[0]) == 2
    assert game_manager.tile_grid[0][0].current_state == "AI"
    assert game_manager.tile_grid[0][1].current_state == "PLAYER"
    assert game_manager.tile_grid[1][0].current_state == "PLAYER"
    assert game_manager.tile_grid[1][1].current_state == "AI"
    game_manager = GameManager(100, 200, 100)
    assert game_manager.tile_grid == []


def test_is_on_board():
    """test GameManager is_on_board method"""
    game_manager = GameManager(300, 200, 100)
    assert game_manager.is_on_board(3, 2) is False
    assert game_manager.is_on_board(1, 1) is True


def test_is_valid_tile_to_place():
    """test GameManager is_valid_tile_to_place method"""
    game_manager = GameManager(600, 600, 100)
    assert game_manager.is_valid_tile_to_place(1, 1, "AI") is False
    assert game_manager.tiles_to_flip == []
    assert game_manager.is_valid_tile_to_place(1, 2, "PLAYER") is True
    assert game_manager.tiles_to_flip == [[2, 2]]
    assert game_manager.is_valid_tile_to_place(2, 2, "PLAYER") is False


def test_get_all_valid_moves():
    """test GameManager get_all_valid_moves method"""
    game_manager = GameManager(400, 400, 100)
    game_manager.get_all_valid_moves("AI")
    assert game_manager.all_valid_moves == [[0, 2], [1, 3], [2, 0], [3, 1]]
    game_manager = GameManager(200, 200, 100)
    game_manager.get_all_valid_moves("PLAYER")
    assert game_manager.all_valid_moves == []


def test_get_max_count_move_AI():
    """test GameManager get_max_count_move_AI method"""
    game_manager = GameManager(400, 400, 100)
    game_manager.get_all_valid_moves("AI")
    col, row = game_manager.get_max_count_move_AI()
    assert col == 2
    assert row == 0
    game_manager = GameManager(600, 600, 100)
    game_manager.get_all_valid_moves("PLAYER")
    col, row = game_manager.get_max_count_move_AI()
    assert col == 1
    assert row == 2


def test_get_fake_tile_grid():
    """test GameManager get_fake_tile_grid method"""
    game_manager = GameManager(400, 400, 100)
    game_manager.get_fake_tile_grid()
    assert game_manager.fake_tile_grid[1][1].current_state == "AI"
    game_manager.tile_grid[1][3].change_state("PLAYER")
    game_manager.get_fake_tile_grid()
    assert game_manager.fake_tile_grid[1][3].current_state == "PLAYER"


def test_get_count():
    """test GameManager get_count method"""
    game_manager = GameManager(400, 400, 100)
    game_manager.tile_grid[1][3].change_state("PLAYER")
    game_manager.get_fake_tile_grid()
    game_manager.get_count()
    assert game_manager.black_count == 3
    assert game_manager.white_count == 2


def test_have_remaining_value_move():
    game_manager = GameManager(400, 400, 100)
    assert game_manager.have_remaining_value_move("AI") is True
    game_manager.tile_grid[2][0].change_state("PLAYER")
    game_manager.tile_grid[3][1].change_state("PLAYER")
    game_manager.tile_grid[0][2].change_state("PLAYER")
    game_manager.tile_grid[1][3].change_state("PLAYER")
    assert game_manager.have_remaining_value_move("AI") is False


def test_flip_tle():
    game_manager = GameManager(600, 600, 100)
    game_manager.is_valid_tile_to_place(1, 2, "PLAYER")
    game_manager.flip_tile("PLAYER")
    assert game_manager.tile_grid[2][2].current_state == "PLAYER"
    game_manager.flip_tile("AI")
    assert game_manager.tile_grid[0][0].current_state == "BACKGROUND"


def flip_tile(self, tile_state):
    """Given the state to flip, flip the tiles to that state"""
    for col, row in self.tiles_to_flip:
        self.tile_grid[col][row].change_state(tile_state)


def test_is_have_background_move():
    game_manager = GameManager(400, 400, 100)
    assert game_manager.is_have_background_move() is True
    game_manager = GameManager(200, 200, 100)
    assert game_manager.is_have_background_move() is False


def test_is_game_ended():
    """test GameManager is_game_ended method"""
    game_manager1 = GameManager(400, 400, 100)
    assert game_manager1.is_game_ended() is False
    game_manager2 = GameManager(200, 200, 100)
    assert game_manager2.is_game_ended() is True
    game_manager2.tile_grid[0][0].change_state("PLAYER")
    game_manager2.tile_grid[1][1].change_state("BACKGROUND")
    assert game_manager2.get_all_valid_moves("AI") is None
    assert game_manager2.tile_grid[1][1].current_state == "BACKGROUND"
    assert game_manager2.is_game_ended() is True


def test_is_any_move_available():
    game_manager = GameManager(400, 400, 100)
    assert game_manager.is_any_move_available() is True
    game_manager = GameManager(200, 200, 100)
    assert game_manager.is_any_move_available() is False


def test_player_move():
    game_manager = GameManager(400, 400, 100)
    game_manager.player_move(0, 1)
    assert game_manager.tile_grid[0][1].current_state == "PLAYER"
    assert game_manager.tile_grid[1][1].current_state == "PLAYER"


def test_ai_move():
    game_manager = GameManager(400, 400, 100)
    game_manager.ai_move()
    assert game_manager.tile_grid[2][0].current_state == "AI"
    assert game_manager.tile_grid[2][1].current_state == "AI"
    game_manager.tile_grid[3][1].change_state == "AI"
    assert game_manager.is_player_turn is True
