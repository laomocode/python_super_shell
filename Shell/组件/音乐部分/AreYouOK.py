if __name__ != '__main__':
    import sys
    import os
    系统=os.name
    if 系统=="posix":
        sys.path.append(sys.path[0]+"/组件/音乐部分")
    elif 系统=="nt":
        sys.path.append(sys.path[0]+"\组件\音乐部分")
    from 音乐基础部分 import *
def AreYouOK():
    print("雷猴王来了！")
    音乐("Are You OK.mp3",132)