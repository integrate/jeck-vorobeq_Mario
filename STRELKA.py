import wrap
strelka=wrap.sprite.add("img_1",350,430,"img_1")
def ykaz_strelk(b):

    top_mar = wrap.sprite.get_top(b["ID"])
    x_mar = wrap.sprite.get_x(b["ID"])
    wrap.sprite.move_bottom_to(strelka, top_mar)
    wrap.sprite.move_centerx_to(strelka, x_mar)


