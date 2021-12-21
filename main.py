import wrap,object_physics

wrap.world.create_world(1900,500)
wrap.world.set_back_color(45,81,253)
wrap.sprite.add("mario-scenery",100,480,"block")
mario=object_physics.create_physics("mario-1-small", 100, 0, "stand",3)
lue=object_physics.create_physics("mario-2-small", 200, 0, "stand",0)

@wrap.always
def phisics():
    object_physics.power_gravity(lue)
    object_physics.power_gravity(mario)