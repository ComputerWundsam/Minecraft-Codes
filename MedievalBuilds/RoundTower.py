radius = 25
pi = 3.14159265359
height = 60
startpos = pos(0, 0, 0)
c = 48
stoneblock = STONE_BRICKS

def on_on_chat():
    global startpos
    startpos = player.position()
    flatten()
    for i in range(2*radius*pi):
        blocks.fill(stoneblock, positions.add(startpos, pos(Math.sin(i/radius) * radius - 1, 0, Math.cos(i/radius) * radius - 1)), 
                    positions.add(startpos, pos(Math.sin(i/radius) * radius +1, height, Math.cos(i/radius) * radius + 1)) , FillOperation.REPLACE)
        blocks.fill(stoneblock, startpos, positions.add(startpos, pos(Math.sin(i/radius) * radius, 0, Math.cos(i/radius) * radius)) , FillOperation.REPLACE)
    createroof()
    createwindows()
    creategate()

def flatten():
    tradius = radius+5
    for j in range(3):
        for i in range(2*tradius*pi):
            blocks.fill(AIR, positions.add(startpos, pos(0, 60-30*j, 0)), positions.add(startpos, pos(Math.sin(i/tradius) * tradius, 90-30*j, Math.cos(i/tradius) * tradius)))

def createroof():
    global height 
    height = height+1
    for j in range(3):
        tradius = radius + j +1
        for i in range(2*tradius*pi):
            blocks.fill(stoneblock, positions.add(startpos, pos(Math.sin(i/tradius) * tradius - 1, height+j, Math.cos(i/tradius) * tradius - 1)), positions.add(startpos, pos(Math.sin(i/tradius) * tradius +1, height+j, Math.cos(i/tradius) * tradius + 1)) , FillOperation.REPLACE)
    for i in range(2*tradius*pi):
        blocks.fill(stoneblock, positions.add(startpos, pos(0, height+j-1, 0)), positions.add(startpos, pos(Math.sin(i/tradius) * tradius, height+j-1, Math.cos(i/tradius) * tradius)) , FillOperation.REPLACE)
    cpart = 0
    cvalue = 0
    for i in range(pi*tradius*2):
        if(i >= cpart):
            cvalue += 1
            cpart += pi*tradius*2/c
        value = i/tradius
        player.say(cpart)
        if cvalue % 4 == 0:
            cheight = 4
        else:
            cheight = 0
        blocks.fill(stoneblock, positions.add(startpos, pos(Math.sin(value)*tradius - 1, height+j, Math.cos(value)*tradius - 1)), positions.add(startpos, pos(Math.sin(value)*tradius + 1, height+cheight+j, Math.cos(value)*tradius + 1)))

def createwindows():
    lowpos = height/3
    highpos = 2*height/3
    for i in range(2):
        blocks.replace(AIR, stoneblock, positions.add(startpos, pos(-radius - 1 + (2*radius*i+2), lowpos, -1)), positions.add(startpos, pos(-radius + 1 + (2*radius*i-2), highpos, 1)))
        blocks.replace(AIR, stoneblock, positions.add(startpos, pos(-1, lowpos, -radius - 1 + (2*radius*i+2))), positions.add(startpos, pos(1, highpos, -radius + 1 + (2*radius*i-2))))

def creategate():
    blocks.fill(STONE_BRICKS, positions.add(startpos, pos(radius-2, 0, -4)), positions.add(startpos, pos(radius+2, 3, 4)), FillOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(radius-2, 1, -3)), positions.add(startpos, pos(radius+2, 2, 3)), FillOperation.REPLACE)
    for i in range(3):
        blocks.fill(STONE_BRICKS, positions.add(startpos, pos(radius-2, 4+i, -4+i)), positions.add(startpos, pos(radius+2, 4+i, 4-i)), FillOperation.REPLACE)
        blocks.fill(AIR, positions.add(startpos, pos(radius-2, 2+i, -3+i)), positions.add(startpos, pos(radius+2, 2+i, 3-i)), FillOperation.REPLACE)

player.on_chat("run", on_on_chat)
player.on_chat("test", test)

def test():
    global startpos 
    startpos = player.position()
    createroof()
