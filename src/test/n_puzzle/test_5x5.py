from src.service.n_puzzle.main import generate_goal_sum

def test_5x5():
    assert generate_goal_sum([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]) == 0

    assert generate_goal_sum([
        [5, 1, 2, 3, 4],
        [6, 7, 8, 9, 0],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]) == 4

    assert generate_goal_sum([
        [1, 2, 3, 4, 5],
        [0, 7, 8, 9, 6],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]) == 3

    assert generate_goal_sum([
        [5, 4, 3, 2, 1],
        [10, 9, 8, 7, 6],
        [15, 14, 13, 12, 11],
        [20, 19, 18, 17, 16],
        [0, 0, 0, 0, 0]
    ]) == 40

    assert generate_goal_sum([
        [1, 2, 3, 0, 5],
        [6, 7, 8, 4, 9],
        [11, 12, 13, 14, 10],
        [16, 17, 18, 19, 15],
        [21, 22, 23, 24, 25]
    ]) == 12