import random

def print_list(list):
    for i in list:
        print(i)

def generate_initial_state(k : int):
    rows = k
    numbers = list(range(k * k))
    random.shuffle(numbers)
    
    initial_state = [numbers[i * k:(i + 1) * k] for i in range(k)]
    return initial_state

def generate_goal_state(list:list):    
    flattened_list = [num for row in list for num in row if num != 0]
    len_of_list = len(flattened_list)

    sum:int = 0
    for i in range(len_of_list):
        for j in range(i + 1, len_of_list):
            if flattened_list[j] < flattened_list[i] and flattened_list[j] != 0:
                sum += 1

    return sum
        


list = generate_initial_state(3)
print_list(list)
print(generate_goal_state(list))