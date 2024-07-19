def on_item_interacted():
    startpos = player.position()
    blocks.replace(EMERALD_BLOCK, GRASS, positions.add(startpos, pos(-15, -20, -15)), positions.add(startpos, pos(15, 0, 15)))
    blocks.replace(IRON_BLOCK, STONE, positions.add(startpos, pos(-15, -20, -15)), positions.add(startpos, pos(15, 0, 15)))
    blocks.replace(GOLD_BLOCK, DIRT, positions.add(startpos, pos(-15, -20, -15)), positions.add(startpos, pos(15, 0, 15)))
    blocks.replace(GOLD_BLOCK, SAND, positions.add(startpos, pos(-15, -20, -15)), positions.add(startpos, pos(15, 0, 15)))
    blocks.replace(LAPIS_LAZULI_BLOCK, WATER, positions.add(startpos, pos(-15, -20, -15)), positions.add(startpos, pos(15, 0, 15)))
player.on_item_interacted(NETHERITE_SHOVEL, on_item_interacted)

