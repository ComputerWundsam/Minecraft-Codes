pi = 3.14159265359
radius = 20
width = 1

def on_on_chat():
    startpos = player.position()
    c = 0
    for j in range(20): 
        for i in range(2*radius*pi):
            x1 = Math.sin(i/radius)*radius
            z1 = Math.cos(i/radius)*radius
            x2 = Math.sin(pi+i/radius)*radius
            z2 = Math.cos(pi+i/radius)*radius
            blocks.fill(RED_CONCRETE, positions.add(startpos, pos(x1-width, c-width, z1-width)), 
                positions.add(startpos, pos(x1+width, c+width, z1+width)), FillOperation.REPLACE) 
            blocks.fill(LIGHT_BLUE_CONCRETE, positions.add(startpos, pos(x2-width, c-width, z2-width)),
                positions.add(startpos, pos(x2+width, c+width, z2+width)), FillOperation.REPLACE)
            blocks.fill(LIME_CONCRETE, positions.add(startpos, pos(z2-width, c-width, x1-width)),
                positions.add(startpos, pos(z2+width, c+width, x1+width)), FillOperation.REPLACE)
            blocks.fill(YELLOW_CONCRETE, positions.add(startpos, pos(z1-width, c-width, x2-width)),
                positions.add(startpos, pos(z1+width, c+width, x2+width)), FillOperation.REPLACE)
            if i%3 == 0:
                c += 1
player.on_chat("run", on_on_chat)
