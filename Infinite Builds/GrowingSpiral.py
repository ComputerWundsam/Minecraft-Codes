pi = 3.14159265359
xposadd = [-1, 0, 1, 0]
zposadd = [0, 1, 0, -1]

baseradius = 3


def on_on_chat():
    startpos = player.position()
    invertpos = player.position()
    count = 1
    radius = baseradius
    while True:
        for i in range(radius*pi/2 +1):
            v = count*pi/2

            blocks.fill(IRON_BLOCK, positions.add(startpos, pos(Math.sin(v+i/radius)*radius-baseradius/2, 0, Math.cos(v+i/radius)*radius-baseradius/2)), 
                                    positions.add(startpos, pos(Math.sin(v+i/radius)*radius+baseradius/2, 0, Math.cos(v+i/radius)*radius+baseradius/2)), FillOperation.REPLACE)

        startpos = positions.add(startpos, pos(xposadd[count%xposadd.length]*baseradius, 0, zposadd[count%zposadd.length]*baseradius))
        count += 1
        radius = baseradius*count


player.on_chat("run", on_on_chat)
