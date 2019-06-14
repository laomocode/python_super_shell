if __name__ != '__main__':
    import os
    系统=os.name
def 天气():
    if 系统=="posix":
        print(os.system("curl wttr.in"))