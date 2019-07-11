if __name__ != '__main__':
    import pygame
    from sys import path
    from time import sleep
    from os import chdir
    from 音乐基础部分 import *
def 真香(歌词):
    切换工作目录(".")
    if 歌词=="歌词":
        文件=open("真香.mp3",mode='r')
        pygame.init()
        pygame.mixer.init()
        播放=pygame.mixer.music.load(文件)
        pygame.mixer.music.play()
        print("我王境泽就是饿死。")
        sleep(2)
        print("死外面从这儿跳下去！")
        sleep(2)
        print("也不会吃一点东西！")
        sleep(2)
        print("啊，真香诶！")
        sleep(2)
        pygame.mixer.music.stop()
        pygame.quit()
        文件.close()
    else:
        音乐("真香.mp3",8)