if __name__ != '__main__':
    import pygame
    import sys
    import time
    import os
def 王司徒():
    os.chdir(sys.path[0])
    os.chdir("音乐")
    文件=open("王司徒.mp3",mode='r')
    pygame.init()
    pygame.mixer.init()
    播放=pygame.mixer.music.load(文件)
    pygame.mixer.music.play()
    time.sleep(52)
    print("王朗：“来者可是诸葛孔明。”")
    time.sleep(4)
    print("诸葛亮：“正是。”")
    time.sleep(2)
    print("王朗：“久闻公之大名，今日有幸相会。”")
    time.sleep(10)
    print("王朗：“公既知天命，识时务，为何要兴无名之师，犯我疆界？”")
    time.sleep(10)
    print("诸葛亮：“我奉诏讨贼，何谓之无名？”")
    time.sleep(8)
    print("王朗：“天数有变，神器更易，而归有德之人，此乃自然之理。”")
    # 1分35秒=95秒
    time.sleep(9)
    print("诸葛亮：“曹贼篡汉，霸占中原，何称有德之人？”")
    # 1分43秒
    time.sleep(8)
    print("王朗：“自桓帝、灵帝以来，黄巾猖獗，天下纷争，社稷有累卵之危，生灵有倒悬之急。”")
    time.sleep(13)
    print("王朗：“我太祖武皇帝，扫清六合，席卷八荒，万姓倾心，四方仰德；此非以权势取之，实乃天命所归也！”")
    # 2分12秒
    time.sleep(16)
    print("王朗：“我世祖文皇帝，神文圣武，继承大统，应天和人，法尧善舜，处中国以治万邦，这岂非天心人意乎？”")
    time.sleep(20)
    print("王朗：“今公蕴大才，抱大器自比管仲、乐毅，何乃强要逆天理，背人情而行事？”")
    time.sleep(10)
    print("王朗：“岂不闻古人云：‘顺天者昌，逆天者亡’？今我大魏带甲百万，良将千员。”")
    # 2分53秒
    time.sleep(11)
    print("王朗：“谅尔等腐草之荧光，如何比得上天空之皓月？”")
    time.sleep(7)
    print("王朗：“你若倒戈卸甲，以礼来降，仍不失封侯之位，国安民乐，岂不美哉？”")
    time.sleep(17)
    # 3分17秒
    print("诸葛亮：“我原以为你身为汉朝老臣，来到阵前，面对两军将士。”")
    time.sleep(7)
    print("诸葛亮：“必有高论，没想到竟说出如此粗鄙之语！”")
    # 3分33秒
    time.sleep(9)
    print("诸葛亮：“我有一言，请诸位静听：’昔日桓帝、灵帝之时，汉统衰落，宦官酿祸，国外岁凶，四方扰攘。黄巾之后，董卓、李傕、郭汜等接踵而起。劫持汉帝，残暴生灵，因之，庙堂之上，朽木为官，殿陛之间禽兽食禄！以至狼心狗行之辈汹汹当朝，奴颜婢膝之徒，纷纷秉政，以致使社稷变为丘墟，苍生饱受涂炭之苦！至此国难之际，王司徒又有何作为？王司徒之生平，我素有所知，你世居东海之滨，初举孝廉入仕，理当匡君辅国，安汉兴刘，何期反助逆贼，同模篡位！罪恶深重，天地不容！’”")
    time.sleep(80)
    # 4分53秒
    print("王朗：“你……诸葛村夫，你……敢……”")
    time.sleep(4)
    print("诸葛亮：“住口!”")
    time.sleep(1)
    print("诸葛亮：“无耻老贼，岂不知天下之人，皆愿生啖你肉，安敢在此饶舌！”")
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
    print("诸葛亮：“一条断脊之犬，还敢在我军阵前狺狺狂吠。”")
    time.sleep(6)
    print("诸葛亮：“我从未见过有如此厚颜无耻之人！”") 
    time.sleep(6)
    print("王朗：当场去世。")
    time.sleep(26)
    pygame.mixer.music.stop()
    pygame.quit()
    文件.close()