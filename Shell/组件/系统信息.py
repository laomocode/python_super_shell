if __name__ != '__main__':
    from os import name,system
    系统=name
def 系统信息():
    if 系统=="nt":
        print(system("ver"))
        print("您的系统是Windows。")
    if 系统=="posix":
        print(system("uname -a"))
        print("您的系统是UNIX或兼容于UNIX的系统（如Linux、Mac OS X、BSD等等）。")