# 音频聚合
if __name__ != '__main__':
    from os import name
    from sys import path
    系统=name
    if 系统=="posix":
        path.append(path[0]+"/组件/音乐部分")
    elif 系统=="nt":
        path.append(path[0]+"\组件\音乐部分")
    from aipc import *
    from 王司徒 import *
    from 真香 import *
    from AreYouOK import *
    from 念诗之王 import *
    from 金坷垃 import *
def 音频聚合():
    while 1:
        输入=int(input("您需要听什么？（1）金坷垃、（2）真香、（3）王司徒气死、（4）AIPC、（5）Are You OK、（6）念诗之王、（7）退出："))
        #输入=int(input("您需要听什么？（1）金坷垃、（2）真香、（3）王司徒气死、（4）退出："))
        if 输入==1:
            金坷垃()
        elif 输入==2:
            真香()
        elif 输入==3:
            王司徒()
        elif 输入==4:
            aipc()
        elif 输入==5:
            AreYouOK()
        elif 输入==6:
            念诗之王()
        elif 输入==7:
            break
        #elif 输入==4:
            #break
        else:
            continue
