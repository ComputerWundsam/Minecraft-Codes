bsets = [EMERALD_ORE,OXIDIZED_COPPER,WEATHERED_COPPER,DARK_PRISMARINE,PRISMARINE,PRISMARINE,
LAPIS_ORE,EMERALD_BLOCK,CYAN_GLAZED_TERRACOTTA,BLUE_CONCRETE,LAPIS_LAZULI_BLOCK,LIGHT_BLUE_CONCRETE,LIGHT_BLUE_TERRACOTTA,
MUD_BRICKS,BROWN_TERRACOTTA,PRISMARINE,WARPED_PLANKS,BLUE_WOOL,WARPED_PLANKS,RED_MUSHROOM_BLOCK,REDSTONE_BLOCK]

def on_on_chat():
    startpos = positions.add(player.position(), pos(0, 60, 0))
    for i in range(400):
        blocks.fill(AIR, positions.add(startpos, pos(-200+i, -60, -200)), positions.add(startpos, pos(-200+i, 0, 200)))
        blocks.fill(BLOCK_OF_NETHERITE, positions.add(startpos, pos(-200+i, -120, -200)), positions.add(startpos, pos(-200+i, -120, 200)))
    for i in range(120):
        blocks.fill(AIR, positions.add(startpos, pos(-30, -i, -30)), positions.add(startpos, pos(30, -i, 30)))
    for i in range (xyzi.length):
        blocks.place(bsets[xyzi[i][3]], positions.add(startpos, pos(xyzi[i][0], xyzi[i][1], xyzi[i][2])))
player.on_chat("run", on_on_chat)
