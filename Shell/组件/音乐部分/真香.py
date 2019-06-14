if __name__ != '__main__':
    import pygame
    import sys
    import time
def 真香():
    os.chdir(sys.path[0])
    os.chdir("音乐")
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
    pygame.quit()
    文件.close()