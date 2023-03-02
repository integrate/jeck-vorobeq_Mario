import wrap, random

wrap.add_sprite_dir("img_1")
wrap.world.create_world(1350, 500)

import object_physics, mario as mario_mod, dracon, STRELKA

wrap.world.set_back_image("img.png")
seconds = 65
seconde = seconds - 1
schet_lue = 0
schet_mario = 0
rounds_lue = wrap.sprite.add_text(str(0), 1200, 50, text_color=[255, 255, 255], font_size=50)
rounds_mario = wrap.sprite.add_text(str(0), 100, 50, text_color=[255, 255, 255], font_size=50)
schet = wrap.sprite.add_text(str(seconde), 600, 450, text_color=[255, 255, 255], font_size=50)
id = wrap.sprite.add("mario-scenery", 100, 380, "block")
id1 = wrap.sprite.add("mario-scenery", 1100, 380, "block")
cloud_platform = wrap.sprite.add("mario-items", 500, 200, "cloud_platform")
cloud_platform2 = wrap.sprite.add("mario-items", 600, 300, "cloud_platform")
cloud_platform3 = wrap.sprite.add("mario-items", 400, 100, "cloud_platform")
cloud_platform4 = wrap.sprite.add("mario-items", 1000, 200, "cloud_platform")
cloud_platform5 = wrap.sprite.add("mario-items", 1200, 300, "cloud_platform")
cloud_platform6 = wrap.sprite.add("mario-items", 600, 100, "cloud_platform")
death = wrap.sprite.add("img_1", 100, 200, "img", False)
dragon = wrap.sprite.add("mario-enemies", 1200, 160, "dragon_stand1")
merio = wrap.sprite.add("mario-1-small", 100, 160, "stand")
grounds_list = [cloud_platform, cloud_platform2, cloud_platform3, id, id1, cloud_platform4, cloud_platform5,
                cloud_platform6]
mario = object_physics.create_physics("mario-1-small", mario_mod, 100, 370, "stand", -8, 200, grounds_list)
# lue = object_physics.create_physics("mario-enemies", dracon, 100, 0, "dragon_stand1", 0,wrap.sprite.get_top(id))
lue = object_physics.create_physics("mario-enemies", dracon, 1100, 370, "dragon_stand1", 0, 300, grounds_list)
vode = 2


def voda():
    if vode == 1:

        STRELKA.ykaz_strelk(mario)
    else:
        STRELKA.ykaz_strelk(lue)


@wrap.always(delay=10)
def run_phisics():
    object_physics.power_gravity(mario)

    object_physics.power_gravity(lue)
    voda()


@wrap.on_key_down(wrap.K_w)
def jump():
    object_physics.jump(mario)


@wrap.on_key_down(wrap.K_UP)
def jump():
    object_physics.jump(lue)


@wrap.on_key_always(wrap.K_a, delay=10)
def move():
    object_physics.move_left(mario)
    voda()


@wrap.on_key_always(wrap.K_d, delay=10)
def move():
    object_physics.move_right(mario)
    voda()


@wrap.on_key_always(wrap.K_LEFT, delay=10)
def move():
    object_physics.move_left(lue)
    voda()


@wrap.on_key_always(wrap.K_RIGHT, delay=10)
def move():
    object_physics.move_right(lue)
    voda()


@wrap.always
def pered_str():
    global vode, seconde
    collide_strelka = wrap.sprite.is_collide_sprite(lue["ID"], mario["ID"])
    if vode == 1 and collide_strelka == True:
        seconde = seconds
        vode = 2
        wrap.sprite.move_to(lue["ID"], 1100, -1600)
    elif collide_strelka == True:
        seconde = seconds
        vode = 1
        wrap.sprite.move_to(mario["ID"], 100, -1600)


def death_who():
    global schet_lue, schet_mario, seconde
    if schet_mario==3:
        wrap.sprite.add_text("mario win",675,250,font_size=200,text_color=[125,125,125],back_color=[12,12,12])
        exit()
    if schet_lue==3:
        wrap.sprite.add_text("dracon win",675,250,font_size=200,text_color=[125,125,125],back_color=[12,12,12])
        exit()
    if vode == 2 and seconde == 0:
        wrap.sprite.move_to(death, 1200, 100)
        wrap.sprite.show(death)
        schet_mario += 1
        wrap.sprite_text.set_text(rounds_mario, str(schet_mario))
    if vode == 1 and seconde == 0:
        wrap.sprite.move_to(death, 100, 100)
        wrap.sprite.show(death)

        schet_lue += 1
        wrap.sprite_text.set_text(rounds_lue, str(schet_lue))
    if seconde <= 0:
        wrap.sprite.move_to(mario["ID"], 100, 330)
        wrap.sprite.move_to(lue["ID"], 1100, 330)
        seconde = seconds



@wrap.always(1000)
def schetchik():
    global seconde, schet
    if seconde <= 0:
        return
    wrap.sprite.remove(schet)
    seconde = seconde - 1
    schet = wrap.sprite.add_text(str(seconde), 600, 450, text_color=[255, 255, 255], font_size=50)
    death_who()

import wrap_py
wrap_py.app.start()