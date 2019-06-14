if __name__ != '__main__':
    import os
    系统=os.name
def 系统信息():
    if 系统=="nt":
        print(os.system("ver"))
        print("您的系统是Windows。")
    if 系统=="posix":
        print(os.system("uname -a"))
        print("您的系统是UNIX或兼容于UNIX的系统（如Linux、Mac OS X、BSD等等）。")