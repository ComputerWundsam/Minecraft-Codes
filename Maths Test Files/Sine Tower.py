def on_on_chat():
    global startpos
    startpos = player.position()
    for k in range(50):
        blocks.place(GLASS,
            positions.add(startpos, pos(0 - k, Math.sin(2 * k / radius) * radius, 0)))
        blocks.place(GLASS,
            positions.add(startpos, pos(0 - k, Math.cos(2 * k / radius) * radius, 0)))
        blocks.place(GLASS,
            positions.add(startpos, pos(0 - k, Math.tan(2 * k / radius) * radius, 0)))
player.on_chat("jump", on_on_chat)

def on_chat2():
    global startpos
    startpos = player.position()
    shapes.sphere(GLASS, startpos, 25, ShapeOperation.OUTLINE)

def on_on_chat2():
    global startpos
    startpos = player.position()
    j = 0
    while j <= radius - 1:
        i = 0
        while i <= (radius - j) * 2 * pi - 1:
            blocks.place(GLASS,
                positions.add(startpos,
                    pos(Math.sin(i / (radius - j)) * (radius - j),
                        j,
                        Math.cos(i / (radius - j)) * (radius - j))))
            i += 1
        j += 1
player.on_chat("r", on_on_chat2)

startpos: Position = None
radius = 10
pi = 3.14159265359
