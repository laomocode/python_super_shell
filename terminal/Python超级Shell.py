#!/usr/bin/env python3
# Python超级Shell
import os
import webbrowser
import random
import pygame
import time
系统=os.name
版本="滚动"
工作目录=os.getcwd()
print("欢迎使用Python 超级Shell",版本,"版本！")
print("此项目已经改名，原名为Python Linux终端。")
print("输入“帮助”来查看帮助。")
def 切换工作目录():
    os.chdir(工作目录)
    os.chdir("terminal")
def 音乐(音频,秒数):
    文件=open(音频,mode='r')
    pygame.init()
    pygame.mixer.init()
    播放=pygame.mixer.music.load(文件)
    pygame.mixer.music.play()
    time.sleep(秒数)
    pygame.mixer.music.stop()
    文件.close()
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
#def aipc():
    #切换工作目录()
    #文件=open("AIPC.mp3",mode='r')
    #pygame.init()
    #pygame.mixer.init()
    #播放=pygame.mixer.music.load(文件)
    #pygame.mixer.music.play()
    #print("好消息！好消息！")
    #time.sleep(1)
    #print("笔记本电脑又要降价了。")
    #time.sleep(2)
    #print("AIPC,以1699元的价格劲爆出击。")
    #time.sleep(3)
    #print("你没听错，就是1699元。")
    #time.sleep(3)
    #print("每家一台电脑已经不稀奇，每人一个笔记本的时代来临了！")
    #time.sleep(4)
    # 13秒
    #print("老板在用、白领在用、小学生再用、老人也在用。")
    #time,sleep(4)
    #print("办公室、咖啡馆、大街小巷，到处都是AIPC的身影。")
    #time.sleep(3)
    #print("在北京、在上海、在广州，引发抢购热潮。")
    #time.sleep(4)
    #print("AIPC超低价格，超强性能（原台词为“功能”，但广告的画面中为“性能“，由于现代计算机的功能是靠软件来的，可以随时扩展和删除。因此”功能“不准确，转而用画面中的”性能“）、超酷外形，仅售1699元。心动不如行动，赶紧拿起电话抢购吧！")
    #ime.sleep(8)
    # 32秒
    #print("老板：”你在看我这台电脑，发了8000块钱，平时用的功能连八分之一都到不了（结论是看任务管理器的CPU占用率来看的，大写的服），等于说，我花了8000块钱，其中有7000块钱我都用不到。")
    #time.sleep(10)
    #print("股民：“这电脑啊，能够上网、看图片、看股票、打印文件就够用了。呦，这股票还涨起来了！”")
    #time.sleep(8)
    #print("老板：”办公软件都有，你看，多轻巧时尚（原广告画面不为“轻巧”，而是“小巧”，但说的是“轻巧”）。“")
    # 52秒
    #time.sleep(8)
    #print("主妇：“这么小，但是你看有3个USB接口，外加一个读卡器插槽。可以同时连接3个U盘（你不感觉触控板难用吗？）外加读数码相机里面的照片，简直太厉害了！")
    #time.sleep(11)
    #print("能聊天、发邮件、高速上网、看电影，我都会用！")
    #time.sleep(4)
    #print("AIPC的CPU，由三星最新研发。")
    #time.sleep(3)
    # 1分10秒
    #print("你看，同样运行一个3D游戏，台式机很快就死机了（话说以现在Windows NT内核的稳定性，配置就算差也不会四级呀（Mac OS X和Linux虽说也可以玩游戏，但您觉得有人会用这些玩意玩？）！），而我们AIPC却一直都很流畅。你看，子弹的火焰都看的一清二楚（话说三星的处理器只提供ARM处理器，主流的电脑游戏都不支持）。用这样的电脑玩游戏，那才叫爽！")
    #time.sleep(12)
    #print("不仅如此，他的内存三星原装。内存越高级，画面的解析力越强（你逗我玩吗？）。")
    #time.sleep(5)
    #print("这是最新的美国大片（这是美国大片吗？）。停，放大放大再放大。哈哈，天鹅（原为”海鸥“，但画面展示出来的是天鹅，因而改为”天鹅“）的每一根羽毛都看的清清楚楚。")
    #time.sleep(7)
    #print("让我们用对比一下普通的电视机再看一遍。没有拖尾、没有停顿。这样的画面，只有三星原装内存才能做得到。这样的电影看起来才叫爽！(大写的”服“）")
    # 1分43秒
    #time.slepp(9)
    #print("有了AIPC，你再也不用为购买价格昂贵的CD、DVD而烦恼了。更不用为找不到那部非常想看的电影而翻箱倒柜了。")
    #time.sleep(9)
    #print("有了AIPC笔记本电脑，可以享受百万首MP3等网络歌曲（1.其他电脑也可以办到的、2.您不怕侵权吗？）有了他，你可以随时收听周杰伦的歌曲，也可以珍藏蔡依林的美妙音乐，还可以珍藏雪村的所有歌曲。有了它，你还可以在线观赏好莱坞大片（1.其他电脑也行啊！2.这样干在法律上是属于侵权了。），在线观看几十万部网络高清电影。或者是浪漫的爱情故事篇，也或者是令人毛骨悚然的恐怖大片。")
    # 2分14秒
    #time.sleep(22)
    #print("AIPC还内置了MSN等聊天软件（MSN不是凉透了吗？），他可以随时随地的进行网上聊天（其他电脑不行吗？），最多可以同时和50个人聊天（其他电脑不行吗？）。它可能是世界上最（不）优良的笔记本电脑，它可以让你立刻变得无比迷人、无比浪漫。")
    #time.sleep(14)
    #print("无线上网，随时冲浪。你才是时尚达人、美酒佳人，音乐电影，那才是数字生活（把“数”念做“晓”）。")
    # 2分34秒
    #time.sleep(6)
    #print("AIPC超低价格，超强性能（原台词为“功能”，但广告的画面中为“性能“，由于现代计算机的功能是靠软件来的，可以随时扩展和删除。因此”功能“不准确，转而用画面中的”性能“）、超酷外形，仅售1699元。心动不如行动，赶紧拿起电话抢购吧！")
    #time.sleep(9)
    #print("接下来我们AIPC极限挑战的时间了。")
    #time.sleep(4)
    # 2分47秒
    #print("我们挑战的第一关是——它的性能到底怎么样呢？")
    #time,sleep(3)
    #print("AIPC笔记本电脑")
    #pygame.mixer.music.stop()
    #文件.close()
    # 这段代码将会在未来一段时间处于冻结状态，未来等一些新功能解决了再干。
def 王司徒():
    切换工作目录()
    文件=open("王司徒.mp3",mode='r')
    pygame.init()
    pygame.mixer.init()
    播放=pygame.mixer.music.load(文件)
    pygame.mixer.music.play()
    time.sleep(52)
    print("王朗：”来者可是诸葛孔明。“")
    time.sleep(4)
    print("诸葛亮：”正是。“")
    time.sleep(2)
    print("王朗：”久闻公之大名，今日有幸相会。”")
    time.sleep(10)
    print("王朗：“公既知天命，识时务，为何要兴无名之师，犯我疆界？”")
    time.sleep(10)
    print("诸葛亮：“我奉诏讨贼，何谓之无名？“")
    time.sleep(8)
    print("王朗：“天数有变，神器更易，而归有德之人，此乃自然之理。”")
    # 1分35秒=95秒
    time.sleep(9)
    print("诸葛亮：“曹贼篡汉，霸占中原，何称有德之人？")
    # 1分43秒
    time.sleep(8)
    print("王朗：”自桓帝、灵帝以来，黄巾猖獗，天下纷争，社稷有累卵之危，生灵有倒悬之急。“")
    time.sleep(13)
    print("王朗：”我太祖武皇帝，扫清六合，席卷八荒，万姓倾心，四方仰德；此非以权势取之，实乃天命所归也！“")
    # 2分12秒
    time.sleep(16)
    print("王朗：”我世祖文皇帝，神文圣武，继承大统，应天和人，法尧善舜，处中国以治万邦，这岂非天心人意乎？“")
    time.sleep(20)
    print("王朗：”今公蕴大才，抱大器自比管仲、乐毅，何乃强要逆天理，背人情而行事？“")
    time.sleep(10)
    print("王朗：”岂不闻古人云：’顺天者昌，逆天者亡’？今我大魏带甲百万，良将千员。“")
    # 2分53秒
    time.sleep(11)
    print("王朗：”谅尔等腐草之荧光，如何比得上天空之皓月？“")
    time.sleep(7)
    print("王朗：”你若倒戈卸甲，以礼来降，仍不失封侯之位，国安民乐，岂不美哉？“")
    time.sleep(17)
    # 3分17秒
    print("诸葛亮：“我原以为你身为汉朝老臣，来到阵前，面对两军将士。”")
    time.sleep(7)
    print("诸葛亮：“必有高论，面向到竟说出如此粗鄙之语！”")
    # 3分33秒
    time.sleep(9)
    print("诸葛亮：“我有一言，请诸位静听：’昔日桓帝、灵帝之时，汉统衰落，宦官酿祸，国外岁凶，四方扰攘。黄巾之后，董卓、李傕、郭汜等接踵而起。劫持汉帝，残暴生灵，因之，庙堂之上，朽木为官，殿陛之间禽兽食禄！以至狼心狗行之辈汹汹当朝，奴颜婢膝之徒，纷纷秉政，以致使社稷变为丘墟，苍生饱受涂炭之苦！至此国难之际，王司徒又有何作为？王司徒之生平，我素有所知，你世居东海之滨，初举孝廉入仕，理当匡君辅国，安汉兴刘，何期反助逆贼，同模篡位！罪恶深重，天地不容！‘”")
    time.sleep(80)
    # 4分53秒
    print("王朗：“你……诸葛村夫，你……敢……”")
    time.sleep(4)
    print("诸葛亮：“住口!“")
    time.sleep(1)
    print("诸葛亮：”无耻老贼，岂不知天下之人，皆愿生啖你肉，安敢在此饶舌！”")
    # 5分08秒
    time.sleep(10)
    print("诸葛亮：“今幸天意不绝炎汉，昭烈皇帝于西川，继承大统，我今奉嗣君之旨，兴师讨贼，你既为谄谀之臣，只可潜身缩首，苟图衣食，怎敢在我军面前妄称天数！”")
    # 5分27秒
    time.sleep(19)
    print("诸葛亮：“皓首匹夫，苍髯老贼！”")
    time.sleep(2)
    print("诸葛亮：“你即将命归九泉之下，届时有何面目去见汉朝二十四代先帝！”")
    time.sleep(11)
    print("诸葛亮：“二臣贼子，你枉活七十有六，一生未立寸功，只会摇唇鼓舌！助曹为虐！”")
    # 5分48秒
    time.sleep(8)
    print("诸葛亮：”一条断脊之犬，还敢在我军阵前狺狺狂吠。“")
    time.sleep(6)
    print("诸葛亮：”我从未见过有如此厚颜无耻之人！”")
    time.sleep(6)
    print("王朗：当场去世。")
    time.sleep(26)
    pygame.mixer.music.stop()
    文件.close()
def 金坷垃():
    切换工作目录()
    print("即将播放金坷垃广告……")
    音乐("金坷垃.mp3",98)
def 真香():
    切换工作目录()
    文件=open("真香.mp3",mode='r')
    pygame.init()
    pygame.mixer.init()
    播放=pygame.mixer.music.load(文件)
    pygame.mixer.music.play()
    print("我王境泽就是饿死。")
    time.sleep(2)
    print("死外面从这儿跳下去！")
    time.sleep(2)
    print("也不会吃一点东西！")
    time.sleep(2)
    print("啊，真香诶！")
    time.sleep(2)
    pygame.mixer.music.stop()
    文件.close()
def 随机数():
    最小数=int(input("请输入随机数的最小数："))
    最大数=int(input("请输入随机数的最大数："))
    print("您得到的随机数是：",random.randint(最小数,最大数))
def 今天吃什么():
    吃的东西=["火锅","饺子","麦当劳","肯德基","小龙虾","鸡","鸭","鹅"]
    while 1:
        print("今天吃：",吃的东西[random.randint(0,len(吃的东西)-1)])
        重复=input("还想继续吗？（输入“确定”继续，按回车退出）:")
        if 重复=="确定":
            continue
        else:
            break
def 天气():
    if 系统=="posix":
        print(os.system("curl wttr.in"))
def 计算器():
    while 1:
        选项=int(input("请输入您要的选项（1）加法计算，（2）减法计算，（3）乘法计算，（4）除法计算，（5）退出："))
        if 选项==5:
            break
        else:
            continue
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
    print("输入“工具箱”启动工具箱。")
    print("输入“计算器”计算算式。")
    print("输入“关于”查看关于信息。")
    print("输入“音乐”来听些东西。")
    print("从项目文件夹里下载的版本均为滚动版本，发行里为正式版本。")
    print("为了稳定，建议从发行版里下载。")
def 音乐聚合():
    while 1:
        #输入=int(input("您需要听什么？（1）金坷垃、（2）真香、（3）王司徒气死、（4）AIPC、（5）退出："))
        输入=int(input("您需要听什么？（1）金坷垃、（2）真香、（3）王司徒气死、（4）退出："))
        if 输入==1:
            金坷垃()
        elif 输入==2:
            真香()
        elif 输入==3:
            王司徒()
        #elif 输入==4:
            #aipc()
        #elif 输入==5:
            #break
        elif 输入==4:
            break
        else:
            continue
def 系统信息():
    if 系统=="nt":
        print(os.system("ver"))
        print("您的系统是Windows。")
    if 系统=="posix":
        print(os.system("uname -a"))
        print("您的系统是UNIX或兼容于UNIX的系统（如Linux、Mac OS X、BSD等等）。")
def 工具箱():
    while 1:
        if 系统=="posix":
            输入=int(input("您要使用工具箱那个功能？（1）今天吃什么、（2）搜索、（3）随机数、（4）天气、（5）退出："))
        if 系统=="nt":
            输入=int(input("您要使用工具箱那个功能？（1）今天吃什么、（2）搜索、（3）随机数、（4）退出："))
        if 输入==1:
            今天吃什么()
        if 输入==2:
            搜索()
        if 输入==3:
            随机数()
        if 系统=="posix" and 输入==4:
            天气()
        if 系统=="posix" and 输入==5:
            break
        if 系统=="nt" and 输入==4:
            break
        else:
            continue
print("下面是系统信息：")
系统信息()
while 1:
    输入=input("终端：")
    if 输入.find("cd")!=-1:
        目录=输入[3:]
        if 目录=="":
            continue
        else:
            os.chdir(目录)
            continue
    elif 输入=="帮助":
        帮助()
        continue
    elif 输入=="工具箱":
        工具箱()
        continue
    elif 输入=="音乐":
        音乐聚合()
        continue
    elif 输入=="退出":
        break
    elif 输入=="关于":
        print("您现在用的是",版本,"版本。")
        print("项目网址：https://gitee.com/laomocode/python_super_shell")
        网页=input("是否打开项目网页？（回车不打开网页，输入“打开”打开项目网页）：")
        if 网页=="打开":
            webbrowser.open("https://gitee.com/laomocode/python_super_shell")
        print("以下是系统信息：")
        系统信息()
        continue
    elif 输入=="计算器":
        计算器()
        continue
    print(os.system(输入))