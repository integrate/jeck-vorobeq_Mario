import random

import wrap


def create_physics(sprite, x, y, costum, speed):
    marIo = wrap.sprite.add(sprite, x, y, costum)
    a = {"ID": marIo, "speed": speed}

    return a


def power_gravity(b, landing):
    wrap.sprite.move(b["ID"], 0, b["speed"])
    b["speed"] += 1
    bottom = wrap.sprite.get_bottom(b["ID"])
    # если y ОБЪЕКТА 480 или больше то телепорт. на 480

    if bottom >= landing:
        wrap.sprite.move_bottom_to(b["ID"],landing)

def jump(b):
    b["speed"]=-8