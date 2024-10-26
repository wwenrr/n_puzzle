from src.service.n_puzzle.main import generate_goal_state

def test_3x3():
    assert generate_goal_state([
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ]) == 11

    assert generate_goal_state([
        [2, 3, 8],
        [1, 6, 4],
        [7, 0, 5]
    ]) == 10

    assert generate_goal_state([
        [3, 6, 5],
        [2, 1, 4],
        [0, 7, 8]
    ]) == 10

    assert generate_goal_state([
        [3, 6, 5],
        [2, 1, 4],
        [0, 7, 8]
    ]) == 10

    assert generate_goal_state([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]) == 36

    assert generate_goal_state([
        [1, 3, 2],
        [5, 4, 6],
        [7, 8, 0]
    ]) == 2 

    assert generate_goal_state([
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ]) == 9

    assert generate_goal_state([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]) == 0

    assert generate_goal_state([
        [1, 3, 2],
        [5, 4, 6],
        [7, 8, 0]
    ]) == 2

    assert generate_goal_state([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]) == 0

    assert generate_goal_state([
        [1, 0, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]) == 0

    assert generate_goal_state([
        [1, 2, 0],
        [3, 4, 5],
        [6, 7, 8]
    ]) == 0

    assert generate_goal_state([
        [1, 3, 0],
        [2, 4, 5],
        [6, 7, 8]
    ]) == 1

    assert generate_goal_state([
        [2, 1, 0],
        [3, 4, 5],
        [6, 7, 8]
    ]) == 1
