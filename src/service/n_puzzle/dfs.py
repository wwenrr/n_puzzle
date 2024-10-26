import copy

def print_list(my_list):
    if my_list is None:
        print("List is None!")
        return  
    for i in my_list:
        print(i)

def is_goal_state(state, goal):
    return state == goal

def get_possible_moves(state:list, moving_rule:str):
    zero_pos:tuple = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]  # Tìm vị trí của '0'

    directions = {
        "to_up": (-1, 0),    # Đi lên
        "to_down": (1, 0),   # Đi xuống
        "to_left": (0, -1),  # Qua trái
        "to_right": (0, 1)   # Qua phải
    }
    
    after_zero_pos:tuple = tuple( map (sum, zip(zero_pos, directions[moving_rule]) ) )
    
    SIZE:int = len(state)
    if(
        (after_zero_pos[0] < SIZE and after_zero_pos[1] < SIZE)
        and
        (after_zero_pos[0] >= 0 and after_zero_pos[1] >= 0)
    ): 
        (x_1, y_1) = zero_pos
        (x_2, y_2) = after_zero_pos

        new_list = copy.deepcopy(state)
        new_list[x_1][y_1], new_list[x_2][y_2] = new_list[x_2][y_2], new_list[x_1][y_1]
        
        return new_list
    
    return None

def solve_n_puzzle(state, goal):
    solution_path:list = []
    queue:list = [state]
    visited = set()

    moving:list = [
        "to_up",
        "to_down",
        "to_left",
        "to_right"
    ]

    for i in range(25):
        if(len(queue) == 0): break

        last_element:list = queue[-1]
        visited.add(tuple(map(tuple, last_element)))

        for moving_rule in moving:
            next_move:list = get_possible_moves(last_element, moving_rule)

            if next_move is not None:  
                next_move_tuple = tuple(map(tuple, next_move))  

                if next_move == goal:
                    solution_path.append(copy.deepcopy(queue))
                    solution_path[-1].append(next_move)

                    print("goal:", queue)
                    break

                if next_move_tuple not in visited:  
                    queue.append(next_move)
                    visited.add(tuple(map(tuple, next_move_tuple)))
                    break
                else:
                    print(next_move, "visited")
                
        if(queue[-1] == last_element): queue.pop()

        # break

    print("queue: ")
    if(len(queue)):
        for i in queue:
            print_list(i)
            print("\n")
    else:
        print(solution_path)
    