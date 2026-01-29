import os
import time

def create_large_file(filename, size_in_gb):
    # Kích thước mỗi lần ghi (10MB để tối ưu tốc độ ghi đĩa)
    chunk_size = 10 * 1024 * 1024 
    
    # Nội dung giả lập: Lặp lại dòng chữ này
    # Dùng ký tự đơn giản để giảm tải CPU khi generate
    text_chunk = "Day la mot dong code vo nghia dung de test heavy file.\n" * (chunk_size // 55)
    
    # Tính toán số lần cần lặp
    target_bytes = size_in_gb * 1024 * 1024 * 1024
    iterations = target_bytes // len(text_chunk)

    print(f"--- Đang bắt đầu tạo file '{filename}' với kích thước {size_in_gb}GB ---")
    print("Vui lòng đợi, tốc độ phụ thuộc vào ổ cứng của bạn...")
    
    start_time = time.time()
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for i in range(iterations + 1):
                f.write(text_chunk)
                
                # Hiển thị tiến độ mỗi 100 lần lặp
                if i % 50 == 0:
                    print(f"Đã ghi: {i * len(text_chunk) / (1024**3):.2f} GB")
                    
        end_time = time.time()
        print(f"\n--- Hoàn tất! ---")
        print(f"File '{filename}' đã được tạo.")
        print(f"Thời gian thực hiện: {end_time - start_time:.2f} giây")
        print(f"CẢNH BÁO: Đừng cố mở file này bằng Notepad++ trừ khi bạn muốn treo máy!")
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# --- CẤU HÌNH ---
# Tên file muốn tạo (đuôi .py hay .txt đều được, Notepad++ xử lý như nhau)
FILE_NAME = "sieunang.py" 
# Kích thước file (GB). 5GB là quá đủ để đánh bại Notepad++
SIZE_GB = 5 

if __name__ == "__main__":
    create_large_file(FILE_NAME, SIZE_GB)