import os


def cjwj():
    try:
        os.mkdir('../重要文件')

    except:
        print('正在做准备工作1...')

    try:
        os.mkdir('../图片')

    except:
        print('正在做准备工作2...')
