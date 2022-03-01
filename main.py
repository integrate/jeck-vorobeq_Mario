import wrap, object_physics, mario as mario_mod, dracon

wrap.world.create_world(1900, 500)
wrap.world.set_back_color(45, 81, 253)
id = wrap.sprite.add("mario-scenery", 100, 380, "block")
cloud_platform = wrap.sprite.add("mario-items", 500, 200, "cloud_platform")
cloud_platform2 = wrap.sprite.add("mario-items", 600, 300, "cloud_platform")
cloud_platform3 = wrap.sprite.add("mario-items", 400, 100, "cloud_platform")
mario = object_physics.create_physics("mario-1-small", mario_mod, 550, 200, "stand", -8,200)
#lue = object_physics.create_physics("mario-enemies", dracon, 100, 0, "dragon_stand1", 0,wrap.sprite.get_top(id))
lue = object_physics.create_physics("mario-enemies", dracon, 100, 0, "dragon_stand1", 0,300)
grounds_list=[cloud_platform ,cloud_platform2,cloud_platform3]

@wrap.always
def run_phisics():
    object_physics.power_gravity(mario)
    mario["landing"] = look_earth()
    object_physics.power_gravity(lue)


@wrap.on_key_down(wrap.K_w)
def jump():
    object_physics.jump(mario)


@wrap.on_key_down(wrap.K_UP)
def jump():
    object_physics.jump(lue)


@wrap.on_key_always(wrap.K_a)
def move():
    object_physics.move_left(mario)
    mario["landing"]=look_earth()


@wrap.on_key_always(wrap.K_d)
def move():
    object_physics.move_right(mario)
    mario["landing"]=look_earth()


def look_earth():
    gl=list(grounds_list)
    for a in gl:

        left_mario=wrap.sprite.get_left(mario["ID"])
        right_plat=wrap.sprite.get_right(a)
        if right_plat < left_mario:
            #wrap.sprite.remove(a)
            gl.remove(a)

    for a in gl:
        right_mario = wrap.sprite.get_right(mario["ID"])
        left_plat = wrap.sprite.get_left(a)
        if left_plat > right_mario:
            #wrap.sprite.remove(a)
            gl.remove(a)

    for a in gl:
        bottom_plat = wrap.sprite.get_bottom(a)
        top_mario = wrap.sprite.get_top(mario["ID"])
        if  bottom_plat < top_mario:
            #wrap.sprite.remove(a)
            gl.remove(a)

    if len(gl)>0:
        max=wrap.sprite.get_top(gl[0])
        for a in gl:
            top=wrap.sprite.get_top(a)
            if max < top:
                max = top

    else:
        max=500
    print(max)

    return max
# хотели Далее: переписать условие удаления островов, которые выше

@wrap.on_key_always(wrap.K_LEFT)
def move():
    object_physics.move_left(lue)


@wrap.on_key_always(wrap.K_RIGHT)
def move():
    object_physics.move_right(lue)
