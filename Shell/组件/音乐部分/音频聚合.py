# 音频聚合
if __name__ != '__main__':
    from os import name
    from sys import path
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
            金坷垃输入=int(input("您需要听金坷垃的哪些音乐？（1）不能撒、（2）发达国家、（3）老外打架、（4）农民之声、（5）探索与发现、（6）专家："))
            if 金坷垃输入==1:
                不能撒()
            if 金坷垃输入==2:
                发达国家()
            if 金坷垃输入==3:
                老外打架()
            if 金坷垃输入==4:
                农民之声()
            if 金坷垃输入==5:
                探索与发现()
            if 金坷垃输入==6:
                专家()
        elif 输入==2:
            歌词输入=int(input("你需要开启歌词功能吗？（1）是、（2）否"))
            if 歌词输入==1:
                真香("歌词")
            else:
                真香("")
        elif 输入==3:
            歌词输入=int(input("你需要开启歌词功能吗？（1）是、（2）否"))
            if 歌词输入==1:
                王司徒("歌词")
            else:
                王司徒("")
        elif 输入==4:
            歌词输入=int(input("你需要开启歌词功能吗？（1）是、（2）否"))
            if 歌词输入==1:
                aipc("歌词")
            else:
                aipc("")
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
