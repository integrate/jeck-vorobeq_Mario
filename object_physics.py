import random

import wrap


def create_physics(sprite,x,y,costum,speed):
    marIo=wrap.sprite.add(sprite,x,y,costum)
    a={"ID":marIo,"speed":speed}

    return a


def power_gravity(b):
    wrap.sprite.move(b["ID"],0, b["speed"])
    b["speed"]+=1