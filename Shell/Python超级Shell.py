#!/usr/bin/env python3
# Python超级Shell
from os import system,name,chdir
from sys import path
系统=name
if 系统=="posix":
    path.append(path[0]+"/组件/音乐部分")
    path.append(path[0]+"/组件")
    path.append(path[0]+"/组件/工具箱")
elif 系统=="nt":
    path.append(path[0]+"\组件\音乐部分")
    path.append(path[0]+"\组件")
    path.append(path[0]+"\组件\工具箱")
from 系统信息 import *
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
print("下面是系统信息：")
系统信息()
while 1:
    输入=input("Shell：")
    if 输入.find("cd")!=-1:
        目录=输入[3:]
        if 目录=="":
            continue
        else:
            chdir(目录)
            continue
    elif 输入=="帮助":
        from 帮助 import *
        帮助()
        continue
    elif 输入=="工具箱":
        from 工具箱 import 工具箱
        工具箱()
        continue
    elif 输入=="音频":
        from 音频聚合 import *
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
    print(system(输入))