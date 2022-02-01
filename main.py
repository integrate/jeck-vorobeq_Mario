import wrap, object_physics, mario as mario_mod, dracon

wrap.world.create_world(1900, 500)
wrap.world.set_back_color(45, 81, 253)
id = wrap.sprite.add("mario-scenery", 100, 380, "block")
mario = object_physics.create_physics("mario-1-small", 100, 200, "stand", -8)
lue = object_physics.create_physics("mario-enemies", 100, 0, "dragon_stand1", 0)


@wrap.always
def run_phisics():
    object_physics.power_gravity(mario, mario_mod, wrap.sprite.get_top(id))
    object_physics.power_gravity(lue, dracon, wrap.sprite.get_top(id))


@wrap.on_key_down(wrap.K_w)
def jump():
    object_physics.jump(mario, wrap.sprite.get_top(id))
    mario_mod.costum_jump(mario)


@wrap.on_key_down(wrap.K_UP)
def jump():
    object_physics.jump(lue, wrap.sprite.get_top(id))
    dracon.costum_jump(lue)


@wrap.on_key_always(wrap.K_a)
def move():
    object_physics.move_left(mario)
    mario_mod.povorot_left(mario)


@wrap.on_key_always(wrap.K_d)
def move():
    object_physics.move_right(mario)
    mario_mod.povorot_right(mario)

@wrap.on_key_always(wrap.K_LEFT)
def move():
    object_physics.move_left(lue)
    dracon.povorot_left(lue)

@wrap.on_key_always(wrap.K_RIGHT)
def move():
    object_physics.move_right(lue)
    dracon.povorot_right(lue)