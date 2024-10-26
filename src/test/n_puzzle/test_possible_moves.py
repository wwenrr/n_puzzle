from src.service.n_puzzle.dfs import get_possible_moves

def test_possible_moves():
    list1:list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    assert get_possible_moves(list1, "to_left") == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]

    assert get_possible_moves(list1, "to_right") == None

    assert get_possible_moves(list1, "to_up") == [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
    ]

    assert get_possible_moves(list1, "to_down") == None
    
    list2: list = [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
    ]
    assert get_possible_moves(list2, "to_left") == [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    list4x4: list = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 0, 12],
        [13, 14, 15, 11]
    ]

    assert get_possible_moves(list4x4, "to_left") == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 0, 10, 12],
        [13, 14, 15, 11]
    ]

    assert get_possible_moves(list4x4, "to_right") == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 12, 0],
        [13, 14, 15, 11]
    ]

    assert get_possible_moves(list4x4, "to_up") == [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 7, 12],
        [13, 14, 15, 11]
    ]

    assert get_possible_moves(list4x4, "to_down") == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 15, 12],
        [13, 14, 0, 11]
    ]

    list4x4_out: list = [
        [0, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 11]
    ]
    assert get_possible_moves(list4x4_out, "to_up") == None

    