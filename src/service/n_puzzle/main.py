import random
from . import final_state

def print_list(my_list):
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

def generate_final_state(my_list, mod):
    if(mod == 0): 
        my_list = final_state.form_A(my_list)

my_list = generate_initial_state(4)
print_list(my_list)

generate_goal_sum(my_list)
