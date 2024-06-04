blocksets = [RED_GLAZED_TERRACOTTA, BLUE_GLAZED_TERRACOTTA, LIME_GLAZED_TERRACOTTA, PINK_GLAZED_TERRACOTTA, YELLOW_GLAZED_TERRACOTTA, ORANGE_GLAZED_TERRACOTTA, 
        MAGENTA_GLAZED_TERRACOTTA, GREEN_GLAZED_TERRACOTTA, LIGHT_BLUE_GLAZED_TERRACOTTA, PURPLE_GLAZED_TERRACOTTA]

def on_on_chat():
    startpos = player.position()
    counter = 0
    while (startpos.get_value(Axis.Y) < 320):
        for i in range(blocksets.length):
            blocks.place(blocksets[(i+startpos.get_value(Axis.Y))%blocksets.length], positions.add(startpos, pos(i, 0, 0)))
            blocks.place(blocksets[(i+startpos.get_value(Axis.Y))%blocksets.length], positions.add(startpos, pos(blocksets.length, 0, i)))
            blocks.place(blocksets[(i+startpos.get_value(Axis.Y))%blocksets.length], positions.add(startpos, pos(blocksets.length-i, 0, blocksets.length)))
            blocks.place(blocksets[(i+startpos.get_value(Axis.Y))%blocksets.length], positions.add(startpos, pos(0, 0, blocksets.length-i)))
        startpos = positions.add(startpos, pos(0, 1, 0))
player.on_chat("run", on_on_chat)
