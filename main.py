import wrap, object_physics, mario as mario_mod, dracon
wrap.add_sprite_dir("img_1")
wrap.world.create_world(1350, 500)
wrap.world.set_back_image("img.png")
id = wrap.sprite.add("mario-scenery", 100, 380, "block")
cloud_platform = wrap.sprite.add("mario-items", 500, 200, "cloud_platform")
cloud_platform2 = wrap.sprite.add("mario-items", 600, 300, "cloud_platform")
cloud_platform3 = wrap.sprite.add("mario-items", 400, 100, "cloud_platform")
grounds_list=[cloud_platform ,cloud_platform2,cloud_platform3,id]
strelka=wrap.sprite.add("img_1",350,430,"img_1")
mario = object_physics.create_physics("mario-1-small", mario_mod, 400, 50, "stand", -8,200,grounds_list)
#lue = object_physics.create_physics("mario-enemies", dracon, 100, 0, "dragon_stand1", 0,wrap.sprite.get_top(id))
lue = object_physics.create_physics("mario-enemies", dracon, 100, 0, "dragon_stand1", 0,300,grounds_list)

@wrap.always
def run_phisics():
    object_physics.power_gravity(mario)
    top_mar=wrap.sprite.get_top(mario["ID"])
    x_mar = wrap.sprite.get_x(mario["ID"])
    wrap.sprite.move_bottom_to(strelka,top_mar)
    wrap.sprite.move_centerx_to(strelka,x_mar)
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



@wrap.on_key_always(wrap.K_d)
def move():
    object_physics.move_right(mario)

@wrap.on_key_always(wrap.K_LEFT)
def move():
    object_physics.move_left(lue)


@wrap.on_key_always(wrap.K_RIGHT)
def move():
    object_physics.move_right(lue)
