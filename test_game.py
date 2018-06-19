import pytest
from . import game


def setup_clean_board(start_point: tuple = (0, 0), board_size: int = 4, default_element: str = game.EMPTY) -> list:
    board = [[default_element for _ in range(board_size)] for _ in range(board_size)]
    x, y = start_point
    board[x][y] = game.BLACK
    return board



BOARD_SAMPLE = [
    ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'],
    ['EMPTY', 'BLACK', 'EMPTY', 'EMPTY'],
    ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'],
    ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'],
]

BOARD_VISUAL_POINTS = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(1, 0), (1, 1), (1, 2), (1, 3)],
    [(2, 0), (2, 1), (2, 2), (2, 3)],
    [(3, 0), (3, 1), (3, 2), (3, 3)],
]



def test_has_move_returns_true_when_has_possible_move():
    board = setup_clean_board()
    assert game.has_move(board, 1, 1)


def test_has_move_returns_false_when_dosent_has_a_possible_move():
    board = setup_clean_board(default_element=game.BLACK)
    assert not game.has_move(board, 0, 0)


def test_get_adjacents_from_point_returns_list_of_adjacents_point():
    board = setup_clean_board(start_point=(1, 1))
    expected = [
        (0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]
    board[1][1] = game.BLACK
    assert game.get_adjacents(board, 1, 1) == expected


def mock_call(start_point: tuple = (0, 0), point_to_get: tuple = (1, 1)):
    return game.get_adjacents(
        setup_clean_board(start_point=start_point),
        point_to_get[0],
        point_to_get[1]
    )


@pytest.mark.parametrize(
    'value,expected', [
        (mock_call(point_to_get=(0, 0)), [(0, 1), (1, 0), (1, 1)]),
        (mock_call(
            point_to_get=(0, 1),
            start_point=(0, 1)
        ), [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]),
        (mock_call(
            point_to_get=(3, 0),
            start_point=(3, 0)
        ), [(2, 0), (2, 1), (3, 1)]),
        (mock_call(
            point_to_get=(0, 3),
            start_point=(0, 3)
        ), [(0, 2), (1, 2), (1, 3)]),
        (mock_call(
            point_to_get=(3, 3),
            start_point=(3, 3)
        ), [(2, 2), (2, 3), (3, 2)]),

    ]
)
def test_get_adjacents_from_point_returns_list_of_adjacents_point_edge_cases(value, expected):
    assert value == expected

