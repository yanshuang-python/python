from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains
import time
import keyboard  #监听键盘

import pyautogui
from selenium.webdriver.common.by import By

# C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=9527 --user-data-dir=“F:\selenium\AutomationProfile”
# https://rosettalab.top/annotation
# 链接实例
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
browser = webdriver.Chrome(options=options)


# Rectangular_box1 = browser.find_element_by_css_selector('#root > div > main > div > div > div > div.flex-1.overflow-x-scroll > div > div.relative.flex.flex-1.overflow-hidden > div.main-stage > div.relative.h-full.w-full > div.image-annotation.absolute.overflow-visible > svg:nth-child(3) > polygon.activated.shape.selected-shadow')
# print(Rectangular_box)
# location = Rectangular_box.location
# size = Rectangular_box.size
# w, h = size['width'], size['height']
# # print(location)
# time.sleep(3)
# print(size['x'])

# more_w = Rectangular_box1.size.get('width') #“更多”元素的x坐标
# more_h = Rectangular_box1.size.get('height') #“更多”元素的y坐标
# print(more_y,more_x)
# print(more_h,more_w)
# ActionChains(browser).drag_and_drop_by_offset(source=Rectangular_box, xoffset=500, yoffset=570)
# action.drag_and_drop_by_offset(Rectangular_box, more_x2+20, more_y2-20)
# ActionChains.move_to_element(Rectangular_box)
# pyautogui.moveTo(more_x, more_y, duration=1)

# def test(browser):
#     print('111')
# 检测矩形框是否打开并拖拽矩形框
Rectangular_box = browser.find_element_by_css_selector(
    '#root > div > main > div > div > div > div.flex-1.overflow-x-scroll > div > div.relative.flex.flex-1.overflow-hidden > div.main-stage > div.relative.h-full.w-full > div.image-annotation.absolute.overflow-visible > svg:nth-child(3) > rect:nth-child(22)')
# Rectangular_box2 = browser.find_element_by_css_selector(
#     '#root > div > main > div > div > div > div.flex-1.overflow-x-scroll > div > div.relative.flex.flex-1.overflow-hidden > div.main-stage > div.relative.h-full.w-full > div.image-annotation.absolute.overflow-visible > svg:nth-child(3) > rect:nth-child(18)')
# more_x = Rectangular_box.location.get('x')  # “更多”元素的x坐标
# more_y = Rectangular_box.location.get('y')  # “更多”元素的y坐标
# more_x2 = Rectangular_box.location.get('x')  # “更多”元素的x坐标
# more_y2 = Rectangular_box.location.get('y')  # “更多”元素的y坐标
action = ActionChains(browser)
action.click_and_hold(Rectangular_box)
action.perform()





# keyboard.add_hotkey('b', test, args=(browser,))
