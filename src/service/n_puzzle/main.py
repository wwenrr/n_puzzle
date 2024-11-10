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
    if(len(my_list) == 2):
        return [
            [
                [1, 2],
                [0, 3]
            ],
            [
                [0, 1],
                [2, 3]
            ]
        ] 

    mod:int = generate_goal_sum(my_list)
    return final_state.form_A(len(my_list))

size = 3

# print("Initial State:")
# # my_list = generate_initial_state(size)
# my_list = [
#     [1, 2],
#     [0, 3]
# ]
# print_list(my_list)

# print("goal: ")
# print_list(generate_final_state(my_list))
# print("----------------")


# if(dfs.solve_n_puzzle(my_list, generate_final_state(my_list))):
#     print("Solution found")
# else:
#     print("Dont found solution")

parser = argparse.ArgumentParser()

parser.add_argument('--max-depth', type=int, help='Chiều sâu tối đa của thuật toán', required=True)
parser.add_argument('--size', type=int, help='Kích thước ma trận', required=True)

args = parser.parse_args()

print("Nhap kich thuoc ma tran <n>, chuong trinh se tu dong tao ma tran ngau nhien:")
try:
    size = args.size
    my_list = generate_initial_state(size)

    print(f"Tao ma tran ngau nhien: ")
    print_list(my_list)

    print(f"Tinh toan trang thai dich:")
    goal = generate_final_state(my_list)
    print_list(goal)

    print(f"\nNhap chieu sau toi da cua thuat toan: (Khuyen khich nhap tu n^2 < input < 2*n^2)")
    print(f"Luu y nhap so nho co the khong tim thay solution, nguoc lai co the doi rat lau!")

    max_depth = args.max_depth

    print(f"\nBat dau tim cac ket qua kha thi...")

    solution = dfs.solve_n_puzzle(my_list, generate_final_state(my_list), max_depth)

    if(solution):
        print(f"\nTim thay", len(solution), " ket qua")
    else:
        print(f"\nKhong tim thay solution")

    os.system('cls')
except ValueError:
    print("Thua!")


