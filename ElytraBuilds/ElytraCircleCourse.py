radius = 6
pi = 3.14159265359
ringdistance = 50
ringoffset = 3
randblocks = [DIAMOND_BLOCK, REDSTONE_BLOCK, LAPIS_LAZULI_BLOCK, EMERALD_BLOCK, GOLD_BLOCK, IRON_BLOCK]

def on_on_chat():
    startpos = player.position()
    while True:
        setblock = randblocks[randint(0, randblocks.length-1)]
        for i in range(2*radius*pi):
            blocks.place(setblock, positions.add(startpos, pos(0, Math.sin(i/radius)*radius, Math.cos(i/radius)*radius)))
        startpos = positions.add(startpos, pos(ringdistance, randint(-ringoffset, ringoffset), randint (-ringoffset, ringoffset)))
player.on_chat("run", on_on_chat)
