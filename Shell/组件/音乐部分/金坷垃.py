if __name__ != '__main__':
    from os import name
    from sys import path
    系统=name
    if 系统=="posix":
        path.append(sys.path[0]+"/组件/音乐部分")
    elif 系统=="nt":
        path.append(sys.path[0]+"\组件\音乐部分")
    from 音乐基础部分 import *
def 金坷垃():
    print("欢迎收听金坷垃广告。")
    音乐("金坷垃.mp3",98)