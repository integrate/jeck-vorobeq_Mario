import wrap


def costum_jump(b):
    wrap.sprite.set_costume(b["ID"],"dragon_throw2")

def costum_stand(b):
    wrap.sprite.set_costume(b["ID"],"dragon_stand1")


def povorot_left(b):
    wrap.sprite.set_reverse_x(b["ID"], False)

def povorot_right(b):
    wrap.sprite.set_reverse_x(b["ID"], True)

def beg(r):
    one = wrap.sprite.get_costume(r["ID"])
    if one == "dragon_stand1":
        wrap.sprite.set_costume(r["ID"], "dragon_stand2")
    if one == "dragon_stand2":
        wrap.sprite.set_costume(r["ID"], "dragon_stand1")