if __name__ != '__main__':
    import sys
    import os
    系统=os.name
    if 系统=="posix":
        sys.path.append(sys.path[0]+"/组件/工具箱")
    elif 系统=="nt":
        sys.path.append(sys.path[0]+"\组件\工具箱")
    from 天气 import *
    from 搜索 import *
    from 民国和公元转换 import *
    from 计算器 import *
    from 随机数 import *
def 工具箱():
    while 1:
        if 系统=="posix":
            输入=int(input("您要使用工具箱那个功能？（1）今天吃什么、（2）搜索、（3）随机数、（4）天气、（5）民国和公元纪年转换、（6）退出："))
        if 系统=="nt":
            输入=int(input("您要使用工具箱那个功能？（1）今天吃什么、（2）搜索、（3）随机数、（4）民国和公元纪年转换、（5）退出："))
        if 输入==1:
            今天吃什么()
        if 输入==2:
            搜索()
        if 输入==3:
            随机数()
        if 系统=="posix" and 输入==4:
            天气()
        if 系统=="posix" and 输入==5 or 系统=="nt" and 输入==4:
            输入=int(input("请输入您要民国转公元纪年还是公元转民国纪年，（1）民国转公元纪年、（2）公元转民国纪年："))
            转换年份=int(input("请输入您要转换的年份："))
            if 输入==1:
                民国和公元转换(转换年份,"公元纪年")
            if 输入==2:
                民国和公元转换(转换年份,"民国纪年")
        if 系统=="posix" and 输入==6 or 系统=="nt" and 输入==5:
            break
        else:
            continue