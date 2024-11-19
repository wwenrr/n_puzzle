def goal_state(size: int):
    # Create an empty matrix
    matrix = []
    
    # Variable 'current_number' is used to fill values from 1 to size*size
    current_number = 1
    
    # Loop through all the rows of the matrix
    for i in range(size):
        row = []  # Create a new row
        
        # Loop through all the columns in the current row
        for j in range(size):
            # Check if it's the last number in the matrix (0)
            if current_number == size * size:
                row.append(0)  # Assign 0 to the last position (empty space)
            else:
                # If it's not the last number, assign the next value
                row.append(current_number)
            
            # Increment the number to fill the next position
            current_number += 1
        
        # Add the row to the matrix
        matrix.append(row)

    # Return the filled matrix
    return matrix


# hàm phụ thôi :v
def replace_max_with_zero(matrix):
    max_value = float('-inf')  # Giá trị lớn nhất ban đầu
    max_position = (0, 0)  # Vị trí của phần tử lớn nhất

    # Duyệt qua từng phần tử trong ma trận
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Nếu tìm thấy phần tử lớn hơn, cập nhật giá trị lớn nhất và vị trí
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)

    # Thay thế phần tử lớn nhất bằng 0
    matrix[max_position[0]][max_position[1]] = 0
    
    return matrix
