if __name__ != '__main__':
    import webbrowser
def 搜索():
    搜索引擎=int(input("输入您想要的搜索引擎：（1）百度、（2）360搜索、（3）谷歌、（4）搜狗、（5）秘迹："))
    搜索内容=input("请输入您要搜索的内容：")
    if 搜索引擎==1:
        webbrowser.open("https://www.baidu.com/s?wd="+搜索内容)
    elif 搜索引擎==2:
        webbrowser.open("https://www.so.com/s?q="+搜索内容)
    elif 搜索引擎==3:
        webbrowser.open("https://www.google.com/search?q="+搜索内容)
    elif 搜索引擎==4:
        webbrowser.open("https://www.sogou.com/web?query="+搜索内容)
    elif 搜索引擎==5:
        webbrowser.open("https://mijisou.com/search?q="+搜索内容)