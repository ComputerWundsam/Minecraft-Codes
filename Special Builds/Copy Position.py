startpos = pos(0, 0, 0)
endpos = pos(0, 0, 0)
def setstart():
    global startpos
    startpos = positions.add(player.position(), pos(0, -1, 0))
def setend():
    global endpos
    endpos = player.position()
def clone():    
    blocks.clone(startpos, endpos, pos(0, -1, 0), CloneMask.REPLACE, CloneMode.NORMAL)
player.on_chat("start", setstart)
player.on_chat("end", setend)
player.on_chat("clone", clone)
