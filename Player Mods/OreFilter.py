repblocks = ["grass", "stone", "dirt", "sand", "gravel", "deepslate", "tuff", "smooth_basalt"]
firstpos = pos(-10, -15, -10)
secpos = pos(10, 10, 10)

def destroyblocks():
    for i in range(repblocks.length):
        player.execute("/fill " + firstpos + secpos + " glass replace " + repblocks[i])
    player.execute("/fill " + pos(-9, 0, -9) + pos(9, 9, 9) + " air replace glass")

player.on_travelled(WALK, destroyblocks)
player.on_travelled(SPRINT, destroyblocks)
