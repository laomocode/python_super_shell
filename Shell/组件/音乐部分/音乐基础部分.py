# 音乐基础部分
if __name__ != '__main__':
    import pygame
    from sys import path
    from os import chdir
    from time import sleep
def 音乐(音频,秒数):
    pygame.init()
    pygame.mixer.init()
    chdir(path[0])
    chdir("音乐")
    文件=open(音频,mode='r')
    播放=pygame.mixer.music.load(文件)
    pygame.mixer.music.play()
    sleep(秒数)
    pygame.mixer.music.stop()
    pygame.quit()
    文件.close()