def form_A(size:int):
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

def form_B(n):
    # Khởi tạo ma trận n x n với tất cả các phần tử bằng 0
    matrix = [[0] * n for _ in range(n)]
    
    # Các biến để theo dõi các giới hạn của ma trận
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1  # Giá trị bắt đầu để điền vào ma trận
    
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
                matrix[i][left] = num
                num += 1
            left += 1  # Di chuyển giới hạn bên trái sang phải
            
    
    return replace_max_with_zero(matrix)

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
