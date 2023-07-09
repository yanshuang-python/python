import keyboard  # 监听键盘
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains
import time
from pynput.mouse import Controller,Button

def test_a():
    print('aaa')


def test(browser):
    print('111')
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


if __name__ == '__main__':
    # options = Options()
    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    # browser = webdriver.Chrome(options=options)
    #
    # keyboard.add_hotkey('f1', test_a)
    # # 按f1输出aaa
    # keyboard.add_hotkey('b', test, args=('browser',))
    # # 按ctrl+alt输出b
    # keyboard.wait()
    # # wait里也可以设置按键，说明当按到该键时结束

    # 获取鼠标位置
    import pynput
    from pynput.mouse import Controller, Button

    mouse = Controller()
    mouseposition = mouse.position
    print("鼠标当前的位置是：{0}".format(mouseposition))

