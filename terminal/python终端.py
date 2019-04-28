# Python终端
import os
import time
次数=0
def 帮助():
    print("帮助：")
    print("输入“退出”来退出终端。")
    print("输入“次数”显示输入次数。")
    print("输入“系统”查看系统信息")
def 系统信息():
    系统=os.name
    if 系统=="nt":
        print(os.system("ver"))
        print("你的系统是Windows。")
    if 系统=="posix":
        print(os.system("uname -a"))
        print("你的系统是UNIX或UNIX LIKE。")
while 1:
    输入=input("终端：")
    次数=次数+1
    if 输入=="帮助":
        帮助()
        continue
    elif 输入=="退出":
        break
    elif 输入=="次数":
        print("次数：",次数,"次")
        continue
    elif 输入=="系统":
        print(系统信息())
        continue
    输出=os.system(输入)
    print(输出)
print("你输入了：",次数,"次")