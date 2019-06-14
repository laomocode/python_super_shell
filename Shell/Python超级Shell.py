#!/usr/bin/env python3
# Python超级Shell
import os
import webbrowser
import random
import time
import sys
系统=os.name
if 系统=="posix":
    sys.path.append(sys.path[0]+"/组件/音乐部分")
    sys.path.append(sys.path[0]+"/组件")
elif 系统=="nt":
    sys.path.append(sys.path[0]+"\组件\音乐部分")
    sys.path.append(sys.path[0]+"\组件")
from 音频聚合 import *
版本="滚动"
print(" ____        _   _                   ____                        ")
print("|  _ \ _   _| |_| |__   ___  _ __   / ___| _   _ _ __   ___ _ __ ")
print("| |_) | | | | __| '_ \ / _ \| '_ \  \___ \| | | | '_ \ / _ \ '__|")
print("|  __/| |_| | |_| | | | (_) | | | |  ___) | |_| | |_) |  __/ |   ")
print("|_|    \__, |\__|_| |_|\___/|_| |_| |____/ \__,_| .__/ \___|_|   ")
print("       |___/                                    |_|              ")
print(" ____  _          _ _                                            ")
print("/ ___|| |__   ___| | |                                           ")
print("\___ \| '_ \ / _ \ | |                                           ")
print(" ___) | | | |  __/ | |                                           ")
print("|____/|_| |_|\___|_|_|                                           ")
print("欢迎使用Python 超级Shell",版本,"版本！")
print("此软件使用GPL v3开源协议，请进入软件仓库里的License文件或许可证协议文件查看详情。")
print("此项目已经改名，原名为Python Linux终端。")
print("输入“帮助”来查看帮助。")
def 民国和公元转换(年份,转换模式):
    if 转换模式=="公元纪年":
        民国年份=1912+年份-1
        if 年份==1:
            print("民国元年是公元",民国年份,"年。")
        else:
            print("民国",年份,"是公元",民国年份,"年。")
    elif 转换模式=="民国纪年":
        公元年份=年份-1912
        if 公元年份==0:
            print("公元",年份,"是民国元年。")
        else:
            print("公元",年份,"是民国",年份-1912,"年。")
    else:
        print("错误。")
def 下载视频(网址):
    print(os.system("you-get "+网址))
def AreYouOK():
    print("雷猴王来了！")
    音乐("Are You OK.mp3",132)
def 念诗之王():
    print("赵本山正在为你念诗……")
    音乐("念诗之王.mp3",146)
def 搜索():
    搜索引擎=int(input("输入您想要的搜索引擎：（1）百度、（2）360搜索、（3）谷歌、（4）搜狗、（5）秘迹："))
    搜索内容=input("请输入您要搜索的内容：")
    if 搜索引擎==1:
        webbrowser.open("https://www.baidu.com/s?wd="+搜索内容)
    elif 搜索引擎==2:
        webbrowser.open("https://www.so.com/s?q="+搜索内容)
    elif 搜索引擎==3:
        webbrowser.open("https://www.google.com/search?q="+搜索内容)
    elif 搜索引擎==4:
        webbrowser.open("https://www.sogou.com/web?query="+搜索内容)
    elif 搜索引擎==5:
        webbrowser.open("https://mijisou.com/search?q="+搜索内容)
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
    print("输入“音频”来听些东西。")
    print("从项目文件夹里下载的版本均为滚动版本，发行里为正式版本。")
    print("为了稳定，建议从发行版里下载。")
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
            输入=int(input("您要使用工具箱那个功能？（1）今天吃什么、（2）搜索、（3）随机数、（4）天气、(5)下载视频、（6）民国和公元纪年转换、（7）退出："))
        if 系统=="nt":
            输入=int(input("您要使用工具箱那个功能？（1）今天吃什么、（2）搜索、（3）随机数、（4）下载视频、（5）民国和公元纪年转换、（6）退出："))
        if 输入==1:
            今天吃什么()
        if 输入==2:
            搜索()
        if 输入==3:
            随机数()
        if 输入==5 and 系统=="posix" or 输入==4 and 系统=="nt":
            视频网址=input("请输入您要下载的视频网址：")
            下载视频(视频网址)
        if 系统=="posix" and 输入==4:
            天气()
        if 系统=="posix" and 输入==6 or 系统=="nt" and 输入==5:
            输入=int(input("请输入您要民国转公元纪年还是公元转民国纪年，（1）民国转公元纪年、（2）公元转民国纪年："))
            转换年份=int(input("请输入您要转换的年份："))
            if 输入==1:
                民国和公元转换(转换年份,"公元纪年")
            if 输入==2:
                民国和公元转换(转换年份,"民国纪年")
        if 系统=="posix" and 输入==7 or 系统=="nt" and 输入==6:
            break
        else:
            continue
print("下面是系统信息：")
系统信息()
while 1:
    输入=input("Shell：")
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
    elif 输入=="音频":
        音频聚合()
        continue
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