from src.service.n_puzzle.final_state import form_A
from src.service.n_puzzle.main        import generate_initial_state
from src.service.n_puzzle.main        import generate_goal_sum

def form_1(size:int):
    my_list = []
    for i in range(size-1):
        my_list.append(i)

    my_list.append(0)
    return my_list

def test_3x3():
    for i in range(100):
        my_list  = generate_initial_state(3)
        sum = generate_goal_sum(my_list)
        if(sum % 2 == 0): 
            assert form_A(my_list) == form_1(len(my_list))