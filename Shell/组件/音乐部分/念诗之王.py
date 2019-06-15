if __name__ != '__main__':
    from sys import path
    from os import name
    系统=name
    if 系统=="posix":
        path.append(sys.path[0]+"/组件/音乐部分")
    elif 系统=="nt":
        path.append(sys.path[0]+"\组件\音乐部分")
    from 音乐基础部分 import *
def 念诗之王():
    print("赵本山正在为你念诗……")
    音乐("念诗之王.mp3",146)