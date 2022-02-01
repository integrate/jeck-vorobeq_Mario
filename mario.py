import wrap


def costum_jump(b):
    wrap.sprite.set_costume(b["ID"], "jump")


def costum_stand(b):
    wrap.sprite.set_costume(b["ID"], "stand")


def povorot_left(b):
    wrap.sprite.set_reverse_x(b["ID"], True)

def povorot_right(b):
    wrap.sprite.set_reverse_x(b["ID"], False)
