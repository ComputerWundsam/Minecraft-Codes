c = 10
startpos: Position = None
radius = 10
blockheight = 8
radius = 20

def on_on_chat():
    global startpos, c
    startpos = player.position()
    setheight = startpos.get_value(Axis.Y)
    player.say(startpos.get_value(Axis.Y))
    while setheight > -65 + blockheight:
        blocks.fill(AIR,
            positions.add(startpos,
                pos(Math.sin(c / radius) * radius - blockheight,
                    0 - blockheight - c,
                    Math.cos(c / radius) * radius - blockheight)),
            positions.add(startpos,
                pos(Math.sin(c / radius) * radius + blockheight,
                    blockheight - c,
                    Math.cos(c / radius) * radius + blockheight)),
            FillOperation.REPLACE)
        setheight += 0 - 1
        c += 1
player.on_chat("run", on_on_chat)
