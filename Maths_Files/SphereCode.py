radius = 40
pi = 3.14159265359
c = 12


def on_on_chat():
    startpos = player.position()
    for i in range(4*c):
        for j in range(pi*radius/2 +1):
            diff = Math.cos(j/(2*radius))
            value = (2*pi*i)/(c) 
            blocks.fill(IRON_BLOCK, positions.add(startpos, pos( Math.sin(value)*j * diff - 1, Math.cos(j/radius)*radius, Math.cos(value)*j  * diff - 1)), positions.add(startpos, pos(Math.sin(value)*j * diff + 1, Math.cos(j/radius)*radius, Math.cos(value)*j  * diff + 1)))
            blocks.fill(IRON_BLOCK, positions.add(startpos, pos(Math.sin(value)*j  * diff - 1, -Math.cos(j/radius)*radius, Math.cos(value)*j * diff - 1)), positions.add(startpos, pos(Math.sin(value)*j * diff + 1, -Math.cos(j/radius)*radius, Math.cos(value)*j  * diff + 1)))
player.on_chat("run", on_on_chat)
