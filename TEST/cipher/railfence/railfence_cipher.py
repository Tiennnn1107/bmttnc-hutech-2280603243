class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        # Kiểm tra số lượng hàng hợp lệ
        if num_rails <= 1:
            return plain_text # Không mã hóa nếu chỉ có 1 hàng hoặc ít hơn

        # Tạo các "đường ray" rỗng
        rails = [[] for _ in range(num_rails)]
        
        rail_index = 0
        direction = 1  # 1: xuống, -1: lên

        # Điền các ký tự vào các đường ray
        for char in plain_text:
            rails[rail_index].append(char)
            
            # Thay đổi hướng khi chạm đến hàng đầu tiên hoặc hàng cuối cùng
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            
            # Cập nhật chỉ số đường ray (phải nằm ngoài khối if/elif)
            rail_index += direction
        
        # Nối các ký tự từ các đường ray để tạo ra văn bản đã mã hóa
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Kiểm tra số lượng hàng hợp lệ
        if num_rails <= 1:
            return cipher_text # Không giải mã nếu chỉ có 1 hàng hoặc ít hơn

        # Bước 1: Xác định độ dài của mỗi đường ray
        # rail_lengths sẽ lưu trữ số lượng ký tự trên mỗi đường ray
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1

        # Mô phỏng quá trình mã hóa để biết số lượng ký tự trên mỗi đường ray
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction # Cập nhật chỉ số đường ray

        # Bước 2: Chia văn bản mã hóa thành các đường ray dựa trên độ dài đã tính
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length])) # Chuyển thành list để có thể pop
            start += length

        # Bước 3: Đọc các ký tự từ các đường ray theo đường zigzag để tạo lại văn bản gốc
        plain_text_chars = [''] * len(cipher_text) # Mảng để lưu trữ ký tự giải mã
        rail_index = 0
        direction = 1
        
        # Chỉ số hiện tại trong plain_text_chars
        plain_text_char_index = 0 

        # Lặp qua từng vị trí trong văn bản gốc
        for _ in range(len(cipher_text)):
            # Lấy ký tự đầu tiên từ đường ray hiện tại và thêm vào văn bản gốc
            # Sử dụng pop(0) để loại bỏ ký tự đã lấy
            plain_text_chars[plain_text_char_index] = rails[rail_index].pop(0)
            plain_text_char_index += 1

            # Thay đổi hướng khi chạm đến hàng đầu tiên hoặc hàng cuối cùng
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            
            # Cập nhật chỉ số đường ray
            rail_index += direction
        
        # Nối các ký tự lại để tạo ra văn bản đã giải mã
        return ''.join(plain_text_chars)

