def 随机数():
    from random import randint
    最小数=int(input("请输入随机数的最小数："))
    最大数=int(input("请输入随机数的最大数："))
    print("您得到的随机数是：",randint(最小数,最大数))
def 今天吃什么():
    from random import randint
    吃的东西=["火锅","饺子","麦当劳","肯德基","小龙虾","鸡","鸭","鹅"]
    while 1:
        print("今天吃：",吃的东西[randint(0,len(吃的东西)-1)])
        重复=input("还想继续吗？（输入“确定”继续，按回车退出）:")
        if 重复=="确定":
            continue
        else:
            break