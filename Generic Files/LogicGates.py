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
    blocks.fill(EMERALD_BLOCK, positions.add(setpos, pos(-2, 0, -4)), positions.add(setpos, pos(2, 0, 2)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(REDSTONE, positions.add(setpos, pos(-1+2*i, 1, -2)), positions.add(setpos, pos(-1+2*i, 1, 0)), FillOperation.REPLACE)
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(-1+2*i, 1, -2)))
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -3)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 2)), positions.add(setpos, pos(0, 1, 0)), FillOperation.REPLACE)
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 3)))
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
    blocks.fill(GOLD_BLOCK, positions.add(setpos, pos(-2, 0, -4)), positions.add(setpos, pos(2, 0, 2)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 1, 0)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(REDSTONE, positions.add(setpos, pos(-1+2*i, 1, -2)), positions.add(setpos, pos(-1+2*i, 1, -1)), FillOperation.REPLACE)
        blocks.place(blocks.block_with_data(REPEATER, 2), positions.add(setpos, pos(-1+2*i, 1, -3)))
        blocks.place(blocks.block_with_data(LEVER, 5), positions.add(setpos, pos(-1+2*i, 1, -4)))
        blocks.place(REDSTONE_TORCH, positions.add(setpos, pos(-1+2*i, 2, 0)))
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 2)), positions.add(setpos, pos(0, 1, 1)), FillOperation.REPLACE)
    blocks.fill(IRON_BLOCK, positions.add(setpos, pos(-1, 1, 0)), positions.add(setpos, pos(1, 1, 0)), FillOperation.REPLACE)
    blocks.place(REDSTONE, positions.add(setpos, pos(0, 2, 0)))
    blocks.place(blocks.block_with_data(REDSTONE_TORCH, 3), positions.add(setpos, pos(0, 1, 1)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 3)))
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
    blocks.fill(DIAMOND_BLOCK, positions.add(setpos, pos(-2, 0, -5)), positions.add(setpos, pos(2, 0, 3)), FillOperation.REPLACE)
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
    blocks.fill(REDSTONE, positions.add(setpos, pos(0, 1, 2)), positions.add(setpos, pos(0, 1, 3)))
    blocks.place(REDSTONE_LAMP, positions.add(setpos, pos(0, 1, 4)))
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
