import time
import pyautogui

print("测试")

a = input("图片路径")
i = 1
while i < 9:
    print(pyautogui.locateOnScreen(a))
    time.sleep(1)
    i += 1
