selectmobs = [HORSE, POLAR_BEAR, DONKEY, CHICKEN, CAT, OCELOT, WOLF, SHEEP, FOX, PANDA, VILLAGER]

def on_on_chat(width):
    startpos = player.position()
    for i in range(4):
        blocks.place(IRON_BLOCK, positions.add(startpos, pos(width * (i//2), -1, width*(i%2))))
        blocks.place(RAIL, positions.add(startpos, pos(width * (i//2), 0, width*(i%2))))
    for i in range(width-1):
        placerails(positions.add(startpos, pos(0, 0, i+1)))
        placerails(positions.add(startpos, pos(width, 0, width-i-1)))
        placerails(positions.add(startpos, pos(width-i-1, 0, width)))
        placerails(positions.add(startpos, pos(i+1, 0, 0)))
    makeramp(startpos)

def placerails(selectpos):
    blocks.place(REDSTONE_BLOCK, positions.add(selectpos, pos(0, -1, 0)))
    blocks.place(POWERED_RAIL, selectpos)

def makeramp(startpos):
    agent.teleport(positions.add(startpos, pos(0, 4, 0)), EAST)
    agent.set_item(IRON_BLOCK, 4, 1)
    agent.set_item(RAIL, 4, 2)
    for i in range(5):
        for j in range(2):
            agent.set_slot(j+1)
            agent.place(FORWARD)
            if (j == 0):
                agent.move(UP, 1)
            else:
                agent.move(BACK, 1)
    agent.move(FORWARD, 3)
    while True:
        mobs.spawn(84, agent.get_position())
        loops.pause(500)
        mobs.spawn(selectmobs[randint(0, selectmobs.length-1)], positions.add(startpos, pos(5, 0, 0)))
        loops.pause(500)

player.on_chat("run", on_on_chat)
