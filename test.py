import pyautogui
import keyboard
import threading
import time

pyautogui.PAUSE = 0.1
running = False
thread = None

# Hàm an toàn tìm ảnh, không bị crash
def safe_locate(image_path, confidence=0.8):
    try:
        return pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return None

def auto_click():
    global running
    while running:
        # 1. Tìm hình tròn
        circle = safe_locate(r"E:\0. Study_code\0. CodeLanguage\0. PythonTraining\4. ClickForLicense\circle.png")
        if circle:
            print("Tìm thấy hình tròn:", circle)
            pyautogui.click(circle)
            time.sleep(0.1)

            # 1.1 Tìm nút Tiếp
            next_btn = safe_locate(r"E:\0. Study_code\0. CodeLanguage\0. PythonTraining\4. ClickForLicense\tieptuc.png")
            if next_btn:
                print("Tìm thấy nút Tiếp:", next_btn)
                pyautogui.click(next_btn)
            else:
                # 1.2 Nếu không thấy Tiếp thì thử tìm Kết thúc luyện thi
                end_btn = safe_locate(r"E:\0. Study_code\0. CodeLanguage\0. PythonTraining\4. ClickForLicense\ketthuc.png")
                if end_btn:
                    print("Không thấy nút Tiếp → Nhấn Kết thúc luyện thi:", end_btn)
                    pyautogui.click(end_btn)

        else:
            # 2. Nếu không thấy hình tròn, thử tìm nút Luyện tất cả
            all_btn = safe_locate(r"E:\0. Study_code\0. CodeLanguage\0. PythonTraining\4. ClickForLicense\luyentatca.png")
            if all_btn:
                print("Không thấy hình tròn → Nhấn Luyện tất cả:", all_btn)
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
