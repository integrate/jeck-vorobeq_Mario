import random

import wrap


def create_physics(sprite,x,y,costum):
    marIo=wrap.sprite.add(sprite,x,y,costum)
    a={"ID":marIo,"speed":random.randint(1,5)}

    return a


def power_gravity(b):
    wrap.sprite.move(b["ID"],0, bl["speed"])
