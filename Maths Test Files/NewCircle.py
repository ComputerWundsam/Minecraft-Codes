pi = 3.14159265359
radius = 50
startpos = pos(0, 0, 0)
circleblock = GOLD_BLOCK

def on_on_chat():
    global startpos
    startpos = player.position()
    for i in range(radius*2):
        blocks.fill(circleblock, positions.add(startpos, pos(-Math.sin(i/radius)*radius-1, 0, -Math.cos(i/radius)*radius-1)), 
            positions.add(startpos, pos(Math.sin(i/radius)*radius+1, 0, -Math.cos(i/radius)*radius+1)), FillOperation.REPLACE)
        blocks.fill(circleblock, positions.add(startpos, pos(-Math.sin(i/radius)*radius-1, 0, Math.cos(i/radius)*radius-1)),
                positions.add(startpos, pos(Math.sin(i/radius)*radius+1, 0, Math.cos(i/radius)*radius+1)), FillOperation.REPLACE)

player.on_chat("run", on_on_chat)


