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

def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1  
    
    while top <= bottom and left <= right:
        # Di chuyển từ trái sang phải
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1  # Di chuyển giới hạn trên xuống
        
        # Di chuyển từ trên xuống dưới
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1  # Di chuyển giới hạn bên phải sang trái
        
        if top <= bottom:
            # Di chuyển từ phải sang trái
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Di chuyển giới hạn dưới lên
            
        if left <= right:
            # Di chuyển từ dưới lên trên
            for i in range(bottom, top - 1, -1):
                # Thay thế số 16 bằng số 0
                if num == 17:  # Chỉ thay số 16 bằng 0 khi đến lượt điền
                    matrix[i][left] = 0
                else:
                    matrix[i][left] = num
                num += 1
            left += 1  # Di chuyển giới hạn bên trái sang phải
            
    return matrix
