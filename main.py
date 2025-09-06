import pyautogui
import keyboard
import threading
import time

pyautogui.PAUSE = 0.1  # thời gian nghỉ giữa các thao tác
running = False        # trạng thái bật/tắt
thread = None          # thread chạy auto

def auto_click():
    global running
    while running:
        # Tìm hình tròn
        circle = pyautogui.locateCenterOnScreen(r"E:\0. Study_code\0. CodeLanguage\0. PythonTraining\4. ClickForLicense\circle.png", confidence=0.8)
        if circle:
            print("Tìm thấy hình tròn:", circle)
            pyautogui.click(circle)
            time.sleep(0.1)

            # Tìm nút Tiếp
            next_btn = pyautogui.locateCenterOnScreen(r"E:\0. Study_code\0. CodeLanguage\0. PythonTraining\4. ClickForLicense\tieptuc.png", confidence=0.8)
            if next_btn:
                print("Tìm thấy nút Tiếp:", next_btn)
                pyautogui.click(next_btn)
                time.sleep(0.1)
        else:
            print("Chưa thấy hình tròn...")
            time.sleep(1)

def toggle_running():
    global running, thread
    running = not running
    if running:
        print("Auto click BẬT")
        # Tạo thread chạy auto_click
        thread = threading.Thread(target=auto_click, daemon=True)
        thread.start()
    else:
        print("Auto click TẮT")

print("Nhấn F8 để BẬT/TẮT auto click. Nhấn ESC để thoát.")

# Lắng nghe phím nóng
keyboard.add_hotkey("f8", toggle_running)
keyboard.wait("esc")  # nhấn ESC để thoát
print("Thoát chương trình.")