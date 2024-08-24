pi = 3.14159265359
radius = 20
iradius = 16
diff = (radius - iradius)/2

def on_on_chat():
    startpos = player.position()
    for i in range(diff*pi):
        outradius = (radius+ iradius)/2 + diff * Math.sin(i/diff)
        inradius = (radius + iradius)/2 - diff * Math.sin(i/diff)
        for j in range(2*outradius*pi):
            blocks.fill(RED_CONCRETE, positions.add(startpos, pos(Math.sin(j/outradius)*outradius -1, Math.sin(i/(radius*2))*(radius*2), Math.cos(j/outradius)*outradius-1)), 
            positions.add(startpos, pos(Math.sin(j/outradius)*outradius+1, Math.sin(i/(radius*2))*(radius*2), Math.cos(j/outradius)*outradius +1)))
        for j in range(2*inradius*pi):
            blocks.fill(RED_CONCRETE, positions.add(startpos, pos(Math.sin(j/inradius)*inradius-1, Math.sin(i/(radius*2))*(radius*2), Math.cos(j/inradius)*inradius-1)), 
            positions.add(startpos, pos(Math.sin(j/inradius)*inradius+1, Math.sin(i/(radius*2))*(radius*2), Math.cos(j/inradius)*inradius+1)))
player.on_chat("run", on_on_chat)
