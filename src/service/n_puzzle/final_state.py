def form_A(my_list:list):
    size:int = len(my_list)
    matrix = []
    current_number = 1
    for i in range(size):
        row = []
        for j in range(size):
            if current_number == size * size:  # Kiểm tra nếu là số cuối cùng
                row.append(0)  # Gán số 0 cho phần tử cuối cùng
            else:
                row.append(current_number)
            current_number += 1
        matrix.append(row)
    return matrix