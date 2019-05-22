# Python超级Shell
import os
import webbrowser
系统=os.name
版本="滚动"
print("欢迎使用Python 超级Shell",版本,"版本！")
print("此项目已经改名，原名为Python Linux终端。")
def 天气():
    if 系统=="posix":
        print(os.system("curl wttr.in"))
def 计算器():
    while 1:
        选项=int(input("请输入您要的选项（1）加法计算，（2）减法计算，（3）乘法计算，（4）除法计算，（5）退出："))
        if 选项==5:
            break
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
    print("输入“系统”看系统信息。")
    print("输入“计算”计算算式。")
    print("输入“项目”打开项目网址。")
    print("输入“关于”查看关于信息。")
    if 系统=="posix":
        print("输入“天气”查看当前天气（为英文）。")
    print("从项目文件夹里下载的版本均为滚动版本，发行里为正式版本。")
    print("为了稳定，建议从发行版里下载。")
def 切换目录(目录):
    os.chdir(目录)
def 系统信息():
    if 系统=="nt":
        print(os.system("ver"))
        print("您的系统是Windows。")
    if 系统=="posix":
        print(os.system("uname -a"))
        print("您的系统是UNIX或UNIX LIKE。")
def 项目():
    webbrowser.open("https://gitee.com/laomocode/python_super_shell")
print("下面是系统信息：")
系统信息()
while 1:
    输入=input("终端：")
    if 输入=="帮助":
        帮助()
        continue
    elif 输入=="天气":
        天气()
        continue
    elif 输入=="退出":
        break
    elif 输入=="系统":
        系统信息()
        continue
    elif 输入=="关于":
        print("您现在用的是",版本,"版本。")
        print("项目网址：https://gitee.com/laomocode/python_super_shell")
        continue
    elif 输入=="计算器":
        计算器()
    elif 输入=="项目":
        项目()
        continue
    elif 输入=="切换目录":
        输入的目录=input("请输入您要切换的目录：")
        切换目录(输入的目录)
        continue
    输出=os.system(输入)
    print(输出)