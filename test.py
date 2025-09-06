import pyautogui
import keyboard
import threading
import time
import os # <-- Thay đổi đường dẫn
import sys

# Lấy đường dẫn thư mục hiện tại
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ghép đường dẫn đến file ảnh
circle_path = os.path.join(BASE_DIR, 'images', 'circle.png')
tieptuc_path = os.path.join(BASE_DIR, 'images', 'tieptuc.png')
ketthuc_path = os.path.join(BASE_DIR, 'images', 'ketthuc.png')
luyentatca_path = os.path.join(BASE_DIR, 'images', 'luyentatca.png')
end8h_path = os.path.join(BASE_DIR, 'images', 'end8h.png')

pyautogui.PAUSE = 0.1
running = False
thread = None

# Tránh crash hay hiện lỗi trên thanh
def safe_locate(image_path, confidence=0.8):
    try:
        return pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return None

def auto_click():
    global running
    while running:
        # 1. Tìm hình tròn
        circle = safe_locate(circle_path)
        end8h_panel = safe_locate(end8h_path)
        if circle:

#            print("Tìm thấy hình tròn:", circle)

            pyautogui.click(circle)
            time.sleep(0.1)

            # 1.1 Tìm nút Tiếp
            next_btn = safe_locate(tieptuc_path)
            if next_btn:

#                print("Tìm thấy nút Tiếp:", next_btn)

                pyautogui.click(next_btn)

            else:
                # 1.2 Nếu không thấy Tiếp thì thử tìm Kết thúc luyện thi
                # Kéo xuống nếu không thấy

                pyautogui.scroll(-100)
                if next_btn:
                    pyautogui.click(next_btn)
                    break
                else:
                    end_btn = safe_locate(ketthuc_path)
                    if end_btn == True and next_btn == False:
                        pyautogui.click(end_btn)
                #elif end_btn:
                #    print("Không thấy nút Tiếp → Nhấn Kết thúc luyện thi:", end_btn)
                #    pyautogui.click(end_btn)

        # Dừng chương trình khi hết giờ làm bài
        elif end8h_panel:
            running = False
            print("Bạn đã học đủ thời gian tối đa cho phép")
            os._exit(0)
        

        else:
            # 2. Nếu không thấy hình tròn, thử tìm nút Luyện tất cả
            all_btn = safe_locate(luyentatca_path)
            if all_btn:

#                print("Không thấy hình tròn → Nhấn Luyện tất cả:", all_btn)

                pyautogui.click(all_btn)
            else:
                print("Chưa thấy gì phù hợp...")

        time.sleep(0.2)

def toggle_running():
    global running, thread
    running = not running
    if running:
        print("Auto click BẬT")
        thread = threading.Thread(target=auto_click, daemon=True)
        thread.start()
    else:
        print("Auto click TẮT")

print("Nhấn F8 để BẬT/TẮT auto click. Nhấn ESC để thoát.")

keyboard.add_hotkey("f8", toggle_running)
keyboard.wait("esc")
print("Thoát chương trình.")
