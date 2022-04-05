import random

import wrap


def create_physics(sprite,mod, x, y, costum, speed,landing,ground):
    marIo = wrap.sprite.add(sprite, x, y, costum)
    a = {"ID": marIo,"MOD":mod, "speed": speed,"landing":landing,"GROUND":ground}

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
    look_earth(b)

def jump(b):
    y_landing=wrap.sprite.get_bottom(b["ID"])
    if y_landing ==b["landing"]:
        b["speed"] = -20
        b["MOD"].costum_jump(b)


def move_left(b):
    wrap.sprite.move(b["ID"],-5,0)
    b["MOD"].povorot_left(b)
    b["MOD"].beg(b)
    look_earth(b)


def move_right(b):
    wrap.sprite.move(b["ID"],5,0)
    b["MOD"].povorot_right(b)
    b["MOD"].beg(b)
    look_earth(b)

def look_earth(mario):
    gl = list(mario["GROUND"])
    if mario ["ID"] in gl:
        gl.remove(mario["ID"])
    for a in gl.copy():

        left_mario = wrap.sprite.get_left(mario["ID"])
        right_plat = wrap.sprite.get_right(a)
        if right_plat < left_mario:
            # wrap.sprite.remove(a)
            gl.remove(a)

    for a in gl.copy():
        right_mario = wrap.sprite.get_right(mario["ID"])
        left_plat = wrap.sprite.get_left(a)
        if left_plat > right_mario:
            # wrap.sprite.remove(a)
            gl.remove(a)

    for a in gl.copy():
        top_plat = wrap.sprite.get_top(a)
        bottom_mario = wrap.sprite.get_bottom(mario["ID"])
        if top_plat < bottom_mario:
            # wrap.sprite.remove(a)
            gl.remove(a)

    if len(gl) > 0:
        max = wrap.sprite.get_top(gl[0])
        for a in gl:
            top = wrap.sprite.get_top(a)
            if top< max:
                max = top

    else:
        max = 500

    mario["landing"] = max