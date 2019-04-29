# Python终端
import os
import time
系统=os.name
次数=0
def 天气():
    if 系统=="posix":
        print(os.system("curl wttr.in"))
def 帮助():
    print("帮助：")
    print("输入“退出”来退出终端。")
    print("输入“次数”显示输入次数。")
    print("输入“系统”查看系统信息。")
    if 系统=="posix":
        print("输入“天气”查看当前天气（为英文）。")
def 系统信息(形式):
    if 系统=="nt":
        print(os.system("ver"))
        if 形式=="普通":
            print("你的系统是Windows。")
    if 系统=="posix":
        print(os.system("uname -a"))
        if 形式=="普通":
            print("你的系统是UNIX或UNIX LIKE。")
        print(系统)
print(系统信息("启动输出"))
while 1:
    输入=input("终端：")
    次数=次数+1
    if 输入=="帮助":
        帮助()
        continue
    elif 输入=="天气":
        天气()
        continue
    elif 输入=="退出":
        break
    elif 输入=="次数":
        print("次数：",次数,"次")
        continue
    elif 输入=="系统":
        print(系统信息("普通"))
        continue
    输出=os.system(输入)
    print(输出)
print("你输入了：",次数,"次")