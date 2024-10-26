import random
from . import final_state
from . import dfs

def print_list(my_list):
    if my_list is None:
        print("List is None!")
        return  
    for i in my_list:
        print(i)

def generate_initial_state(k : int):
    rows = k
    numbers = list(range(k * k))
    random.shuffle(numbers)
    
    initial_state = [numbers[i * k:(i + 1) * k] for i in range(k)]
    return initial_state

def generate_goal_sum(my_list:list):    
    flattened_list = [num for row in my_list for num in row if num != 0]
    len_of_list = len(flattened_list)

    sum:int = 0
    for i in range(len_of_list):
        for j in range(i + 1, len_of_list):
            if (flattened_list[j] < flattened_list[i]) and flattened_list[j] != 0:
                # print(flattened_list[i], flattened_list[j], sum)
                sum += 1

    return sum

def generate_final_state(my_list):
    mod:int = generate_goal_sum(my_list)
    if(mod % 2 == 0): 
        return final_state.form_A(len(my_list))
    else:
        return final_state.form_B(len(my_list))

size = 3

print("Initial State:")
my_list = generate_initial_state(size)

print_list(my_list)
print("\n")

if(dfs.solve_n_puzzle(my_list, generate_final_state(my_list))):
    print("Solution found")

# new_list = dfs.get_possible_moves(my_list, "to_up")

# print_list(new_list)

# print( tuple(map(sum, zip((3, 1), (2, 0)))) )

# size = 3

# print("Initial State:")
# my_list = generate_initial_state(size)
# print_list(my_list)

# print("\nGoal State:")
# goal    = generate_final_state(my_list)
# print_list(goal)

# solution = dfs.solve_n_puzzle(my_list, goal)

# if solution:
#     print("\nSolution found:")
#     print_list(solution)
# else:
#     print("No solution found.")
