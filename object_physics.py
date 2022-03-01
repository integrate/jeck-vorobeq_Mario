import random

import wrap


def create_physics(sprite,mod, x, y, costum, speed,landing):
    marIo = wrap.sprite.add(sprite, x, y, costum)
    a = {"ID": marIo,"MOD":mod, "speed": speed,"landing":landing}

    return a


def power_gravity(b):
    wrap.sprite.move(b["ID"], 0, b["speed"])
    bottom = wrap.sprite.get_bottom(b["ID"])
    if bottom < b["landing"]:
        b["speed"] += 1

    # если y ОБЪЕКТА 480 или больше то телепорт. на 480

    if bottom > b["landing"]:
        b["speed"] = 0
        wrap.sprite.move_bottom_to(b["ID"],b["landing"])
        b["MOD"].costum_stand(b)


def jump(b):
    y_landing=wrap.sprite.get_bottom(b["ID"])
    if y_landing ==b["landing"]:
        b["speed"] = -20
        b["MOD"].costum_jump(b)


def move_left(b):
    wrap.sprite.move(b["ID"],-5,0)
    b["MOD"].povorot_left(b)
    b["MOD"].beg(b)



def move_right(b):
    wrap.sprite.move(b["ID"],5,0)
    b["MOD"].povorot_right(b)
    b["MOD"].beg(b)

