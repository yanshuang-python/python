# 当前目录下所有文件夹下的文件名(不带后缀)写入对应txt文件(以文件夹命名)中

from os import walk


def file_name(gen):
    for root, dirs, files in walk(gen):
        print(files)
        return files


file = open('超级无敌集成版' + '.txt', 'w')
file.close()

gen = input("请拉入目标文件夹:") + "\\"
print(gen)
i2 = file_name(gen)

for i in i2:
    with open('{gen}{yan}'.format(yan=i, gen=gen), 'r') as f:
        u = f.read()
    with open(f'{gen}超级无敌集成版.txt', 'a') as p:
        p.write(u + "\n" + "\n")
