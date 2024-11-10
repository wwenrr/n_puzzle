import requests
import time

url = 'https://www.tikifreeship.cc/index/user/login.html'

# Dữ liệu cần gửi (thường là username và password hoặc bất kỳ thông tin nào khác)
data = {
    'username': 'your_username',  # Thay 'your_username' bằng username của bạn
    'password': 'your_password'   # Thay 'your_password' bằng password của bạn
}

with requests.Session() as session:
    while True:
        try:
            response = session.post(url, data=data)  
            print("Response Code:", response.status_code)
            
            # In ra nội dung của phản hồi (nếu cần)
            # print(response.text)  # Cẩn thận với việc in quá nhiều nội dung

            # Thêm một khoảng thời gian chờ giữa các lần gửi request

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            break  # Nếu có lỗi, thoát khỏi vòng lặp
