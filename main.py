import wrap, object_physics

wrap.world.create_world(1900, 500)
wrap.world.set_back_color(45, 81, 253)
id=wrap.sprite.add("mario-scenery", 100, 480, "block")
mario = object_physics.create_physics("mario-1-small", 100, 200, "stand", 3)
lue = object_physics.create_physics("mario-2-small", 100, 0, "stand", 0)


@wrap.always
def run_phisics():
    object_physics.power_gravity(mario,wrap.sprite.get_top(id))
    object_physics.power_gravity(lue,wrap.sprite.get_top(mario["ID"]))
