import wrap


def create_physics(sprite,x,y,costum):
    marIo=wrap.sprite.add(sprite,x,y,costum)
    mario={"ID":marIo}

    return mario


def power_gravity(mario):
    wrap.sprite.move(mario["ID"],0,1)