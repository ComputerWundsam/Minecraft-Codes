pi = 3.14159265359

radius = 1
firstno = 1
secondno = 1

c = 1 #this is the radius of the spiral
inv = 1 #change this to turn around the spiral

def on_on_chat():
    global radius, firstno, secondno
    startpos = player.position()
    r = randint(0, 3)
    for i in range(10):
        radius = firstno + secondno
        secondno = firstno
        firstno = radius
        cradius = radius*c
        for j in range(cradius*pi/2):
            blocks.place(GLOWSTONE, positions.add(startpos, pos(Math.sin((i*pi/2)+j/cradius)*cradius * inv, 0, Math.cos((i*pi/2)+j/cradius)*cradius)))
        if i  % 2 == 0:
            if i  % 4 == 0:
                startpos = positions.add(startpos, pos(-secondno*c* inv, 0, 0))
            else:
                startpos = positions.add(startpos, pos(secondno*c* inv, 0, 0))
        else:
            if i % 4 == 1:
                startpos = positions.add(startpos, pos(0, 0, secondno*c ))
            else:
                startpos = positions.add(startpos, pos(0, 0, -secondno*c))
player.on_chat("run", on_on_chat)
