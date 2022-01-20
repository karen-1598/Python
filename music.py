import pygame
import time
import json
import os

path=r"(insert here the path of mp3 files folder)"
os.chdir(path)
pygame.mixer.init()
for file in os.listdir():
    if file.endswith(".mp3"):
        soundobj=pygame.mixer.Sound(file)
        c=''
        data=''
        soundobj.play()
        c=input("press n if noisy or c if clean ")
        soundobj.stop()
        time.sleep(1)
        data={
            "name":file,
            "label":c
        }
        with open('newfile.json','a')as f:
            json.dump(data,f)

