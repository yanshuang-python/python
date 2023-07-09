from pynput import keyboard
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def on_activate():
    # 检测矩形框是否打开并拖拽矩形框
    Rectangular_box = browser.find_element_by_css_selector(
        '#root > div > main > div > div > div > div.flex-1.overflow-x-scroll > div > div.relative.flex.flex-1.overflow-hidden > div.main-stage > div.relative.h-full.w-full > div.image-annotation.absolute.overflow-visible > svg:nth-child(3) > rect:nth-child(42)')
    # Rectangular_box2 = browser.find_element_by_css_selector(
    #     '#root > div > main > div > div > div > div.flex-1.overflow-x-scroll > div > div.relative.flex.flex-1.overflow-hidden > div.main-stage > div.relative.h-full.w-full > div.image-annotation.absolute.overflow-visible > svg:nth-child(3) > rect:nth-child(18)')
    # more_x = Rectangular_box.location.get('x')  # “更多”元素的x坐标
    # more_y = Rectangular_box.location.get('y')  # “更多”元素的y坐标
    # more_x2 = Rectangular_box.location.get('x')  # “更多”元素的x坐标
    # more_y2 = Rectangular_box.location.get('y')  # “更多”元素的y坐标

    action = ActionChains(browser)
    action.click_and_hold(Rectangular_box)
    action.perform()

def for_canonical(f):
    return lambda k: f(l.canonical(k))


if __name__ == '__main__':
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    browser = webdriver.Chrome(options=options)


    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('b'),
        on_activate)
    with keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()