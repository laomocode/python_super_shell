# 音乐基础部分
if __name__ != '__main__':
    import pygame
    import sys
    import os
    import time
def 音乐(音频,秒数):
    pygame.init()
    pygame.mixer.init()
    os.chdir(sys.path[0])
    os.chdir("音乐")
    文件=open(音频,mode='r')
    播放=pygame.mixer.music.load(文件)
    pygame.mixer.music.play()
    time.sleep(秒数)
    pygame.mixer.music.stop()
    pygame.quit()
    文件.close()