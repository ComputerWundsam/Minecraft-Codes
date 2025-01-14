#Write "not" in Chat
def not_gate():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 5))
    blocks.fill(BLOCK_OF_NETHERITE, positions.add(setpos, pos(-1, 0, -4)), positions.add(setpos, pos(1, 0, 2)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, -3)), positions.add(setpos, pos(0, 1, 2)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(0, 1, -2)))
    negate(positions.add(setpos, pos(0, 1, 0)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 3)))
    blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(0, 1, -4)))
player.on_chat("not", not_gate)

#Write "or" in Chat
def or_gate():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 5))
    pos_or_gate(setpos)
    for i in range(2):
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -3)))
player.on_chat("or", or_gate)

#Write "nor" in Chat
def nor_gate():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 5))
    blocks.fill(MAGENTA_WOOL, positions.add(setpos, pos(-2, 0, -4)), positions.add(setpos, pos(2, 0, 6)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(REDSTONE, positions.add(setpos, pos(-1+2*i, 1, -2)), positions.add(setpos, pos(-1+2*i, 1, 0)), FillOperation.REPLACE)
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(-1+2*i, 1, -2)))
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -3)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 5)), positions.add(setpos, pos(0, 1, 0)), FillOperation.REPLACE)
    negate(positions.add(setpos, pos(0, 1, 3)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 6)))
player.on_chat("nor", nor_gate)

#Write "and" in Chat
def and_gate():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 5))
    pos_and_gate(setpos)
    for i in range(2):
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -4)))
player.on_chat("and", and_gate)

#Write "nand" in Chat
def nand_gate():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 5))
    blocks.fill(LAPIS_LAZULI_BLOCK, positions.add(setpos, pos(-2, 0, -4)), positions.add(setpos, pos(2, 0, 6)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 1, 0)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(REDSTONE, positions.add(setpos, pos(-1+2*i, 1, -2)), positions.add(setpos, pos(-1+2*i, 1, -1)), FillOperation.REPLACE)
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(-1+2*i, 1, -3)))
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -4)))
        blocks.place(REDSTONE_TORCH, positions.add(setpos, pos(-1+2*i, 2, 0)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 6)), positions.add(setpos, pos(0, 1, 1)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 1, 0)), FillOperation.REPLACE)
    blocks.place(REDSTONE, positions.add(setpos, pos(0, 2, 0)))
    blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(0, 1, 1)))
    negate(positions.add(setpos, pos(0, 1, 3)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 6)))
player.on_chat("nand", nand_gate)

#Write "xor" in Chat
def xor_gate():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 6))
    pos_xor_gate(setpos)
    for i in range(2):
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -5)))
player.on_chat("xor", xor_gate)

#Write "xnor" in Chat
def xnor_gate():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 6))
    blocks.fill(NETHER_BRICK, positions.add(setpos, pos(-2, 0, -5)), positions.add(setpos, pos(2, 0, 7)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 1, -2)), positions.add(setpos, pos(1, 1, 1)), FillOperation.REPLACE)
    for i in range(2):
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -5)))
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(-1+2*i, 1, -4)))
        blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(-1+2*i, 1, -1)))
        blocks.place(REDSTONE, positions.add(setpos, pos(-1+2*i, 2, 1)))
        blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(-1+2*i, 1, 2)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(-1, 1, -3)), positions.add(setpos, pos(1, 1, -3)), FillOperation.REPLACE)
    blocks.place(AIR, positions.add(setpos, pos(0, 1, -3)))
    blocks.fill(REDSTONE_TORCH, positions.add(setpos, pos(-1, 2, -2)), positions.add(setpos, pos(1, 2, -2)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 2, -2)), positions.add(setpos, pos(0, 2, -1)))
    blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(0, 1, 0)))
    blocks.replace(REDSTONE, IRON_BLOCK, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 1, 0)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 2)), positions.add(setpos, pos(0, 1, 6)))
    negate(positions.add(setpos, pos(0, 1, 3)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 7)))
player.on_chat("xnor", xnor_gate)

#Negate necessary for XNOR, NAND and NOR
def negate(setpos):
    blocks.place(IRON_BLOCK, positions.add(setpos, pos(0, 0, 0)))
    blocks.place(REDSTONE, positions.add(setpos, pos(0, 1, 0)))
    blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(0, 0, 1)))

def pos_xor_gate(setpos):
    blocks.fill(DIAMOND_BLOCK, positions.add(setpos, pos(-2, 0, -5)), positions.add(setpos, pos(2, 0, 3)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 1, -2)), positions.add(setpos, pos(1, 1, 1)), FillOperation.REPLACE)
    for i in range(2):
        blocks.place(REDSTONE, positions.add(setpos, pos(-1+2*i, 1, -5)))
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(-1+2*i, 1, -4)))
        blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(-1+2*i, 1, -1)))
        blocks.place(REDSTONE, positions.add(setpos, pos(-1+2*i, 2, 1)))
        blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(-1+2*i, 1, 2)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(-1, 1, -3)), positions.add(setpos, pos(1, 1, -3)), FillOperation.REPLACE)
    blocks.place(AIR, positions.add(setpos, pos(0, 1, -3)))
    blocks.fill(REDSTONE_TORCH, positions.add(setpos, pos(-1, 2, -2)), positions.add(setpos, pos(1, 2, -2)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 2, -2)), positions.add(setpos, pos(0, 2, -1)))
    blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(0, 1, 0)))
    blocks.replace(REDSTONE, IRON_BLOCK, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 1, 0)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 2)), positions.add(setpos, pos(0, 1, 3)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 4)))

def pos_and_gate(setpos):
    blocks.fill(GOLD_BLOCK, positions.add(setpos, pos(-2, 0, -4)), positions.add(setpos, pos(2, 0, 2)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 1, 0)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(REDSTONE, positions.add(setpos, pos(-1+2*i, 1, -4)), positions.add(setpos, pos(-1+2*i, 1, -1)), FillOperation.REPLACE)
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(-1+2*i, 1, -3)))
#        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -4)))
        blocks.place(REDSTONE_TORCH, positions.add(setpos, pos(-1+2*i, 2, 0)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 2)), positions.add(setpos, pos(0, 1, 1)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 1, 0)), FillOperation.REPLACE)
    blocks.place(REDSTONE, positions.add(setpos, pos(0, 2, 0)))
    blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(0, 1, 1)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 3)))

def pos_or_gate(setpos):
    blocks.fill(EMERALD_BLOCK, positions.add(setpos, pos(-2, 0, -4)), positions.add(setpos, pos(2, 0, 2)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(REDSTONE, positions.add(setpos, pos(-1+2*i, 1, -3)), positions.add(setpos, pos(-1+2*i, 1, 0)), FillOperation.REPLACE)
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(-1+2*i, 1, -2)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 2)), positions.add(setpos, pos(0, 1, 0)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(0, 1, 1)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 3)))

def halfadder():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 15))
    pos_halfadder(setpos)
    for i in range(2):
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -10)))

player.on_chat("halfadder", halfadder)

def createredstonepart(selectpos):
    blocks.place(IRON_BLOCK, selectpos)
    blocks.place(REDSTONE, positions.add(selectpos, pos(0, 1, 0)))

def pos_halfadder(setpos):
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(7, 0, -10)), positions.add(setpos, pos(-2, 0, 0)), FillOperation.REPLACE)
    pos_xor_gate(setpos)
    pos_and_gate(positions.add(setpos, pos_camera(5, 0, -1)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(4, 1, -5)), positions.add(setpos, pos(1, 1, -5)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(6, 1, -7)), positions.add(setpos, pos(-1, 1, -7)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(REDSTONE, positions.add(setpos, pos(6-7*i, 1, -5)), positions.add(setpos, pos(6-7*i, 1, -7-2*i)), FillOperation.REPLACE)
    for i in range(3):
        createredstonepart(positions.add(setpos, pos(1, 1+i%2, -6-i)))
    blocks.place(REDSTONE, positions.add(setpos, pos(1, 1, -9)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(7, 1, 1)), positions.add(setpos, pos(6, 1, 1)), FillOperation.REPLACE)
    redstonebridgesouth(positions.add(setpos, pos(8, 1, 1)), 11, 0)
    createredstonepart(positions.add(setpos, pos(9, 1, -10)))

def fulladder():
    setpos = player.position()
    setpos = positions.add(setpos, pos_camera(0, 0, 15))
    pos_fulladder(setpos)
    for i in range(2):
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -10)))


def pos_fulladder(setpos):
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(7, 0, -10)), positions.add(setpos, pos(-3, 0, 20)), FillOperation.REPLACE)
    pos_halfadder(setpos)
    pos_xor_gate(positions.add(setpos, pos(-1, 0, 9)))
    redstonebridgewest(positions.add(setpos, pos(4, 1, 3)), 7)
    redstonebridgesouth(positions.add(setpos, pos(-3, 1, 4)), 14, 2)
    redstonebridgesouth(positions.add(setpos, pos(6, 1, 11)), 10, 2)
    pos_and_gate(positions.add(setpos, pos(4, 0, 9)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(5, 1, 5)), positions.add(setpos, pos(5, 1, 3)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(3, 1, 4)), positions.add(setpos, pos(1, 1, 4)), FillOperation.REPLACE)
    pos_or_gate(positions.add(setpos, pos(5, 0, 15)))
    blocks.place(REDSTONE, positions.add(setpos, pos(7, 1, 15)))
    redstonebridgesouth(positions.add(setpos, pos(8, 1, 15)), 25, 0)
    createredstonepart(positions.add(setpos, pos(9, 1, -10)))
player.on_chat("fulladder", fulladder)

def redstonebridgesouth(setpos, size, direction):
    createredstonepart(setpos)
    createredstonepart(positions.add(setpos, pos(0, 0, -size)))
    blocks.fill(CONCRETE, positions.add(setpos, pos(0, 1, -1)), positions.add(setpos, pos(0, 1, -size+1)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 2, -1)), positions.add(setpos, pos(0, 2, -size+1)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(REPEATER, direction), positions.add(setpos, pos(0, 2, -size/2)))
    blocks.place(blocks.block_with_data(REPEATER, direction), positions.add(setpos, pos(0, 2, -size+2)))
    blocks.place(blocks.block_with_data(REPEATER, direction), positions.add(setpos, pos(0, 2, -2)))

def redstonebridgewest(setpos, size):
    createredstonepart(setpos)
    createredstonepart(positions.add(setpos, pos(-size, 0, 0)))
    blocks.fill(CONCRETE, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(-size+1, 1, 0)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(-1, 2, 0)), positions.add(setpos, pos(-size+1, 2, 0)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(REPEATER, 1), positions.add(setpos, pos(-size/2, 2, 0)))
    blocks.place(blocks.block_with_data(REPEATER, 1), positions.add(setpos, pos(-size/2, 2, 0)))
    blocks.place(blocks.block_with_data(REPEATER, 1), positions.add(setpos, pos(-size/2, 2, 0)))

def nbitadder(n):
    startpos = player.position()
    startpos = positions.add(startpos, pos(0, 0, 15))
    pos_halfadder(startpos)
    createhalfadderconnection(positions.add(startpos, pos(0, 0, 4)))
    for i in range(n-1):
        pos_fulladder(positions.add(startpos, pos(13+13*i, 0, 0)))
    for i in range(n):
        createadderconnections(positions.add(startpos, pos(13*i-1, 0, -2*i-12)), positions.add(startpos, pos(-3, 0, -2*i-12)), 2+2*i, i+1)
        createadderoutput(positions.add(startpos, pos(13*i, 0, 13)), positions.add(startpos, pos(-2, 0, 13)), 2*(n-i)+8, i+1)
player.on_chat("nbit", nbitadder)

def createadderconnections(setpos, firstpos, distance, count):
    blocks.fill(IRON_BLOCK, firstpos, positions.add(setpos, pos(0, 2, 0)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, setpos, positions.add(setpos, pos(2, 0, distance)), FillOperation.REPLACE)
    for i in range(2):
        blocks.place(REDSTONE, positions.add(setpos, pos(2*i, 1, 0)))
        blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1+2*i, 0)), positions.add(firstpos, pos(0, 1+2*i, 0)), FillOperation.REPLACE)
        blocks.fill(REDSTONE, positions.add(setpos, pos(0+2*i, 1, 1)), positions.add(setpos, pos(0+2*i, 1, distance)), FillOperation.REPLACE)
        blocks.place(REDSTONE, positions.add(firstpos, pos(0, 1+2*i, 0)))
        createswitch(positions.add(firstpos, pos(-1, 2*i, 0)))
        for j in range(count):
            blocks.place(blocks.block_with_data(REPEATER, 1), positions.add(firstpos, pos(13*j+1, 1+2*i, 0)))
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(0+2*i, 1, distance)))
        for j in range(distance/12-1):
            player.say(positions.add(setpos, pos(0+2*i, 1, 10*j+10)))
            blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(0+2*i, 1, 12*j+1)))
    createredstonepart(positions.add(setpos, pos(1, 1, 0)))

def createhalfadderconnection(setpos):
    blocks.fill(IRON_BLOCK, setpos, positions.add(setpos, pos(0, 0, 11)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 0)), positions.add(setpos, pos(0, 1, 11)), FillOperation.REPLACE)
    blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(0, 1, 2)))

def createswitch(setpos):
    blocks.place(REDSTONE_LAMP, setpos)
    blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(0, 1, 0)))

def createadderoutput(setpos, firstpos, distance, count):
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(0, 2, distance)), positions.add(setpos, pos(0, 2, 0)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 3, distance)), positions.add(setpos, pos(0, 3, 0)), FillOperation.REPLACE)
    createredstonepart(positions.add(setpos, pos(0, 1, -1)))
    createredstonepart(positions.add(setpos, pos(0, 1, distance+1)))
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(0, 0, distance+2)), positions.add(firstpos, pos(0, 0, distance+2)), FillOperation.REPLACE)
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, distance+2)), positions.add(firstpos, pos(0, 1, distance+2)), FillOperation.REPLACE)
    blocks.place(REDSTONE_LAMP, positions.add(firstpos, pos(-1, 0, distance+2)))
    for i in range(count):
        blocks.place(blocks.block_with_data(REPEATER, 3), positions.add(setpos, pos(-13*i-1, 1, distance+2)))
    for j in range(distance/12):
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(0, 3, 12*j+1)))


def on_chat(n):
    startpos = player.position()
    
    for i in range(n):
        createadderoutput(positions.add(startpos, pos(13*i, 0, (18+2*n))), positions.add(startpos, pos(-2, 0, (18+2*n))), 2*(n-i)+4, i+1)
player.on_chat("jump", on_chat)
