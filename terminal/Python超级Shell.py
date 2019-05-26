#!/usr/bin/env python3
# Python超级Shell
import os
import webbrowser
import random
import pygame
import time
系统=os.name
版本="滚动"
工作目录=os.getcwd()
print("欢迎使用Python 超级Shell",版本,"版本！")
print("此项目已经改名，原名为Python Linux终端。")
print("输入“帮助”来查看帮助。")
def 切换工作目录():
    os.chdir(工作目录)
    os.chdir("terminal")
def 音乐(音频,秒数):
    文件=open(音频,mode='r')
    pygame.init()
    pygame.mixer.init()
    播放=pygame.mixer.music.load(文件)
    pygame.mixer.music.play()
    time.sleep(秒数)
    pygame.mixer.music.stop()
    文件.close()
def aipc():
    切换工作目录()
    print("即将播放AIPC广告……")
    音乐("AIPC.mp3",492)
def 王司徒():
    切换工作目录()
    print("王司徒即将气死……")
    音乐("王司徒.mp3",386)
def 金坷垃():
    切换工作目录()
    print("即将播放金坷垃广告……")
    音乐("金坷垃.mp3",98)
def 真香():
    切换工作目录()
    print("真香！")
    音乐("真香.mp3",8)
def 随机数():
    最小数=int(input("请输入随机数的最小数："))
    最大数=int(input("请输入随机数的最大数："))
    print("您得到的随机数是：",random.randint(最小数,最大数))
def 今天吃什么():
    吃的东西=["火锅","饺子","麦当劳","肯德基","小龙虾","鸡","鸭","鹅"]
    while 1:
        print("今天吃：",吃的东西[random.randint(0,len(吃的东西)-1)])
        重复=input("还想继续吗？（输入“确定”继续，按回车退出）:")
        if 重复=="确定":
            continue
        else:
            break
def 天气():
    if 系统=="posix":
        print(os.system("curl wttr.in"))
def 计算器():
    while 1:
        选项=int(input("请输入您要的选项（1）加法计算，（2）减法计算，（3）乘法计算，（4）除法计算，（5）退出："))
        if 选项==5:
            break
        else:
            continue
        因数1=int(input("请输入第一个因数："))
        因数2=int(input("请输入第二个因数："))
        if 选项==1:
            结果=因数1+因数2
        elif 选项==2:
            结果=因数1-因数2
        elif 选项==3:
            结果=因数1*因数2
        elif 选项==4:
            结果=因数1/因数2
        else:
            print("您输入的内容不正确。")
        print(结果)
def 帮助():
    print("帮助：")
    print("输入“退出”退出终端。")
    print("输入“工具箱”启动工具箱。")
    print("输入“计算器”计算算式。")
    print("输入“关于”查看关于信息。")
    print("输入“音乐”来听些东西。")
    print("从项目文件夹里下载的版本均为滚动版本，发行里为正式版本。")
    print("为了稳定，建议从发行版里下载。")
def 音乐聚合():
    while 1:
        输入=int(input("您需要听什么？（1）金坷垃、（2）真香、（3）王司徒气死、（4）AIPC、（5）退出："))
        if 输入==1:
            金坷垃()
        elif 输入==2:
            真香()
        elif 输入==3:
            王司徒()
        elif 输入==4:
            aipc()
        elif 输入==5:
            break
        else:
            continue
def 系统信息():
    if 系统=="nt":
        print(os.system("ver"))
        print("您的系统是Windows。")
    if 系统=="posix":
        print(os.system("uname -a"))
        print("您的系统是UNIX或兼容于UNIX的系统（如Linux、Mac OS X、BSD等等）。")
def 工具箱():
    while 1:
        if 系统=="posix":
            输入=int(input("您要使用工具箱那个功能？（1）今天吃什么、（2）随机数、（3）天气、（4）退出："))
        if 系统=="nt":
            输入=int(input("您要使用工具箱那个功能？（1）今天吃什么、（2）随机数、（3）退出："))
        if 输入==1:
            今天吃什么()
        if 输入==2:
            随机数()
        if 系统=="posix" and 输入==3:
            天气()
        if 系统=="posix" and 输入==4:
            break
        if 系统=="nt" and 输入==3:
            break
        else:
            continue
print("下面是系统信息：")
系统信息()
while 1:
    输入=input("终端：")
    if 输入.find("cd")!=-1:
        目录=输入[3:]
        if 目录=="":
            continue
        else:
            os.chdir(目录)
            continue
    elif 输入=="帮助":
        帮助()
        continue
    elif 输入=="工具箱":
        工具箱()
        continue
    elif 输入=="音乐":
        音乐聚合()
    elif 输入=="退出":
        break
    elif 输入=="关于":
        print("您现在用的是",版本,"版本。")
        print("项目网址：https://gitee.com/laomocode/python_super_shell")
        网页=input("是否打开项目网页？（回车不打开网页，输入“打开”打开项目网页）：")
        if 网页=="打开":
            webbrowser.open("https://gitee.com/laomocode/python_super_shell")
        print("以下是系统信息：")
        系统信息()
        continue
    elif 输入=="计算器":
        计算器()
        continue
    print(os.system(输入))