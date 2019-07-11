if __name__ != '__main__':
    from os import name,system
    系统=name
def 信息(版本):
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
    if 系统=="nt":
        print(system("ver"))
        print("您的系统是Windows。")
    if 系统=="posix":
        print(system("uname -a"))
        print("您的系统是UNIX或兼容于UNIX的系统（如Linux、Mac OS X、BSD等等）。")