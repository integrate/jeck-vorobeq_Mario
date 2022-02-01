import wrap


def costum_jump(b):
    wrap.sprite.set_costume(b["ID"],"dragon_throw2")

def costum_stand(b):
    wrap.sprite.set_costume(b["ID"],"dragon_stand1")


def povorot_left(b):
    wrap.sprite.set_reverse_x(b["ID"], False)

def povorot_right(b):
    wrap.sprite.set_reverse_x(b["ID"], True)

