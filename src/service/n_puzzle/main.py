import random
from . import final_state
from . import dfs
import os
import sys
import argparse

sys.setrecursionlimit(1000000)
sys.stdout.reconfigure(encoding="utf-8")

def print_list(my_list):
    if my_list is None:
        print("List is None!")
        return  
    for i in my_list:
        print(i)

def generate_initial_state(k : int, size = 20):
    numbers = list(range(k * k))

    initial_state = final_state.goal_state(k)

    random_list = random.choices(range(0, 4), k=size)

    moving_rule = [
        "to_left",
        "to_right",
        "to_up",
        "to_down"
    ]

    for move in random_list:
        next_move = dfs.get_possible_moves(initial_state, moving_rule[move])
        if(next_move is not None):
            initial_state = next_move

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
    return final_state.goal_state(len(my_list))

parser = argparse.ArgumentParser()

parser.add_argument('--max-depth', type=int, help='Chiều sâu tối đa của thuật toán', required=True)
parser.add_argument('--size', type=int, help='Kích thước ma trận', required=True)
args = parser.parse_args()

try:
    max_depth = args.max_depth
    size = args.size
    print(f"Doc du lieu tu input:")
    print("max_depth=",max_depth,", size=",size)

    my_list = generate_initial_state(size, max_depth)

    print(f"Tao ma tran ngau nhien: ")
    print_list(my_list)

    print(f"Tinh toan trang thai dich:")
    goal = generate_final_state(my_list)
    print_list(goal)

    print(f"\nBat dau tim cac ket qua kha thi...")

    solution = dfs.solve_n_puzzle(my_list, generate_final_state(my_list), max_depth)

    if(solution):
        print(f"\nTim thay", len(solution), " ket qua")
    else:
        print(f"\nKhong tim thay solution")

except ValueError:
    print("Thua!")


