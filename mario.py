import wrap


def costum_jump(b):
    wrap.sprite.set_costume(b["ID"], "jump")


def costum_stand(b):
    wrap.sprite.set_costume(b["ID"], "stand")


def povorot_left(b):
    wrap.sprite.set_reverse_x(b["ID"], True)

def povorot_right(b):
    wrap.sprite.set_reverse_x(b["ID"], False)

def beg(r):

    one=wrap.sprite.get_costume(r["ID"])
    if one == "stand":
        wrap.sprite.set_costume(r["ID"],"walk1")
    if one == "walk1":
        wrap.sprite.set_costume(r["ID"],"walk2")

    if one == "walk2":
        wrap.sprite.set_costume(r["ID"], "walk3")
        wrap.sprite.move(r["ID"],0,1)

    if one == "walk3":
        wrap.sprite.set_costume(r["ID"],"walk1")
        wrap.sprite.move(r["ID"], 0, -1)
