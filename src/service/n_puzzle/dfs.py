import copy

# In list ra để debug thôi :v (bỏ cũng đc) vì mù cn nên k biết xài debug tun
def print_list(my_list):
    if my_list is None:
        print("List is None!")
        return  
    for i in my_list:
        for j in i:
            print(j)
        
        print("|")
# Hàm này kiểm tra có phải goal state hay không
def is_goal_state(state, goal):
    if(len(state) == 2):
        return state == [
            [1, 2],
            [0, 3]
        ] or state == [
            [0, 1],
            [2, 3]
        ] or state == [
            [1, 0],
            [2, 3]
        ] or state == [
            [1, 2],
            [3, 0]
        ]

    return state == goal

# Hàm này để lấy trạng thái tiếp theo (lên, xuống, trái, phải) của số 0, trả về None nếu không tìm thấy
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

class dfs:
    maxdepth:int
    visited:set = set()
    solution:list = []
    maxdepth:int
    goal:list
    found:bool

    def __init__(self, queue, goal, maxdepth):
        self.maxdepth = maxdepth
        self.visited.add(tuple(tuple(row) for row in queue[-1]))
        self.goal = goal
        self.found = False

        self.run(queue, 0)

    def run(self, queue, depth):
        if(depth == self.maxdepth):
            return None
        
        if(is_goal_state(queue[-1], self.goal)):
            self.solution.append(copy.deepcopy(queue))
            print(f"Tim thay solution trong ", len(self.solution[-1]), " buoc")
            print_list(self.solution[-1])
            self.found = True
            return None
        
        if(self.found):
            return None
        
        # print_list(queue)

        left = get_possible_moves(queue[-1], "to_left")
        if(left is not None and not self.found):
            left_tuple = tuple(tuple(row) for row in left)
            if(left_tuple not in self.visited):
                queue.append(left)
                self.visited.add(left_tuple)
                self.run(queue, depth+1)
                self.visited.remove(left_tuple)
                queue.pop()

        right = get_possible_moves(queue[-1], "to_right")
        if(right is not None and not self.found):
            right_tuple = tuple(tuple(row) for row in right)
            if(right_tuple not in self.visited):
                queue.append(right)
                self.visited.add(right_tuple)
                self.run(queue, depth+1)
                self.visited.remove(right_tuple)
                queue.pop()

        up = get_possible_moves(queue[-1], "to_up")
        if(up is not None and not self.found):
            up_tuple = tuple(tuple(row) for row in up)
            if(up_tuple not in self.visited):
                queue.append(up)
                self.visited.add(up_tuple)
                self.run(queue, depth+1)
                self.visited.remove(up_tuple)
                queue.pop()

        down = get_possible_moves(queue[-1], "to_down")
        if(down is not None and not self.found):
            down_tuple = tuple(tuple(row) for row in down)
            if(down_tuple not in self.visited):
                queue.append(down)
                self.visited.add(down_tuple)
                self.run(queue, depth+1)
                self.visited.remove(down_tuple)
                queue.pop()

        return None

    def public_get_solution(self):
        return self.solution

# Hàm chính của file này, mấy cái trên là hàm phụ thôi
def solve_n_puzzle(state, goal, max_depth=50):
    queue:list = [state]

    newClass = dfs(queue, goal, max_depth)

    output = newClass.public_get_solution()

    newClass = None

    return output
    