animals = [PARROT, BAT, BEE, CHICKEN, ALLAY]

def on_on_chat():
    while True:
        mobs.spawn(animals[randint(0, animals.length-1)], pos_camera(randint(-1, 1), randint(-3, 3), 5))
player.on_chat("run", on_on_chat)
