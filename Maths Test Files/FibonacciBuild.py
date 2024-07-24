pi = 3.14159265359

radius = 1
firstno = 1
secondno = 1

c = 1

def on_on_chat():
    global radius, firstno, secondno
    startpos = player.position()
    for i in range(20):
        radius = firstno + secondno
        secondno = firstno
        firstno = radius
        cradius = radius*c
        for j in range(cradius*pi/2):
            blocks.place(GLOWSTONE, positions.add(startpos, pos(Math.sin((i*pi/2)+j/cradius)*cradius, 1, Math.cos((i*pi/2)+j/cradius)*cradius)))
            if(j % 50 == 0):
                player.teleport(positions.add(startpos, pos(Math.sin((i*pi/2)+j/cradius)*cradius, 5, Math.cos((i*pi/2)+j/cradius)*cradius)))
        if i % 2 == 0:
            if i % 4 == 0:
                startpos = positions.add(startpos, pos(-secondno*c, 0, 0))
            else:
                startpos = positions.add(startpos, pos(secondno*c, 0, 0))
        else:
            if i % 4 == 1:
                startpos = positions.add(startpos, pos(0, 0, secondno*c))
            else:
                startpos = positions.add(startpos, pos(0, 0, -secondno*c))
player.on_chat("run", on_on_chat)
