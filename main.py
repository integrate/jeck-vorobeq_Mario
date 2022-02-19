import wrap, object_physics, mario as mario_mod, dracon

wrap.world.create_world(1900, 500)
wrap.world.set_back_color(45, 81, 253)
id = wrap.sprite.add("mario-scenery", 100, 380, "block")
cloud_platform = wrap.sprite.add("mario-items", 500, 200, "cloud_platform")
cloud_platform2 = wrap.sprite.add("mario-items", 600, 300, "cloud_platform")
cloud_platform3 = wrap.sprite.add("mario-items", 400, 100, "cloud_platform")
mario = object_physics.create_physics("mario-1-small", mario_mod, 100, 200, "stand", -8)
lue = object_physics.create_physics("mario-enemies", dracon, 100, 0, "dragon_stand1", 0)
grounds_list=[cloud_platform ,cloud_platform2,cloud_platform3]

@wrap.always
def run_phisics():
    object_physics.power_gravity(mario, wrap.sprite.get_top(id))
    object_physics.power_gravity(lue, wrap.sprite.get_top(id))


@wrap.on_key_down(wrap.K_w)
def jump():
    object_physics.jump(mario, wrap.sprite.get_top(id))


@wrap.on_key_down(wrap.K_UP)
def jump():
    object_physics.jump(lue, wrap.sprite.get_top(id))


@wrap.on_key_always(wrap.K_a)
def move():
    object_physics.move_left(mario)
    look_earth()


@wrap.on_key_always(wrap.K_d)
def move():
    object_physics.move_right(mario)
    look_earth()


def look_earth():
    for a in grounds_list:
        wrap.sprite.remove(a)


@wrap.on_key_always(wrap.K_LEFT)
def move():
    object_physics.move_left(lue)


@wrap.on_key_always(wrap.K_RIGHT)
def move():
    object_physics.move_right(lue)
