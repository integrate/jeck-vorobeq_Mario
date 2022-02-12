import random

import wrap


def create_physics(sprite,mod, x, y, costum, speed):
    marIo = wrap.sprite.add(sprite, x, y, costum)
    a = {"ID": marIo,"MOD":mod, "speed": speed}

    return a


def power_gravity(b, landing):
    wrap.sprite.move(b["ID"], 0, b["speed"])
    bottom = wrap.sprite.get_bottom(b["ID"])
    if bottom < landing:
        b["speed"] += 1

    # если y ОБЪЕКТА 480 или больше то телепорт. на 480

    if bottom > landing:
        b["speed"] = 0
        wrap.sprite.move_bottom_to(b["ID"],landing)
        b["MOD"].costum_stand(b)


def jump(b,landing):
    y_landing=wrap.sprite.get_bottom(b["ID"])
    b["MOD"].costum_jump(b)
    if y_landing ==landing:
        b["speed"] = -20

def move_left(b):
    wrap.sprite.move(b["ID"],-5,0)

def move_right(b):
    wrap.sprite.move(b["ID"],5,0)


