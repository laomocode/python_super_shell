if __name__ != '__main__':
    from sys import path
    from os import name
    系统=name
    if 系统=="posix":
        path.append(path[0]+"/组件/音乐部分")
    elif 系统=="nt":
        path.append(path[0]+"\组件\音乐部分")
    from 音乐基础部分 import *
def AreYouOK():
    print("雷猴王来了！")
    音乐("Are You OK.mp3",132)
