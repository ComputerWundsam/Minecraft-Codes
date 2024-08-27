blockheight = 12
radius = 18

def on_on_chat():
    startpos = player.position()
    setheight = startpos.get_value(Axis.Y)
    player.say(startpos.get_value(Axis.Y))
    c=0
    while c < 10000:
        blocks.fill(AIR, positions.add(startpos, pos(Math.sin(c/radius)*radius - blockheight, Math.cos(c/radius)*radius - blockheight,  c)),
                positions.add(startpos, pos(Math.sin(c/radius)*radius + blockheight, Math.cos(c/radius)*radius + blockheight, c )))
        c += 1
player.on_chat("run", on_on_chat)
