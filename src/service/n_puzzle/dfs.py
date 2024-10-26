import copy

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

def solve_n_puzzle(state, goal, visited=None):
    if visited is None:
        visited = set()  # Khởi tạo tập hợp đã duyệt

    state_tuple = tuple(tuple(row) for row in state)  # Chuyển đổi thành tuple để sử dụng làm khóa
    if state_tuple in visited:
        return False  # Trả về False nếu trạng thái đã được duyệt

    visited.add(state_tuple)  # Đánh dấu trạng thái là đã duyệt

    if state == goal:
        print("Found solution!")
        return True  # Trả về True nếu đạt được trạng thái mục tiêu

    # Duyệt các hướng di chuyển
    for direction in ["to_up", "to_down", "to_left", "to_right"]:
        new_state = get_possible_moves(state, direction)
        if new_state is not None:  # Nếu có trạng thái hợp lệ
            if solve_n_puzzle(new_state, goal, visited):
                return True  # Nếu tìm được giải pháp, trả về True

    return False