

def on_chat():
    startpos = player.position()
    for i in range(100):
        loops.pause(100)
        player.execute("fill " + positions.add(startpos, pos(-40, 2+2*i, -40)) + " " + 
            positions.add(startpos, pos(40, 4+2*i, 40)) + " chorus_flower replace chorus_flower")
player.on_chat("run", on_chat)
