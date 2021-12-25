import random

import wrap


def create_physics(sprite,x,y,costum,speed):
    marIo=wrap.sprite.add(sprite,x,y,costum)
    a={"ID":marIo,"speed":speed}

    return a


def power_gravity(b,y,x):
    landing=480
    wrap.sprite.move(b["ID"],0, b["speed"])
    b["speed"]+=1
    #если y марио 480 или больше то телепорт. на 480

    if y >= 480:
        wrap.sprite.move_to(b["ID"],x,480)