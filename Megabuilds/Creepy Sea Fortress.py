stoneblock = STONE_BRICKS
radius = 60
size = 5
startpos = pos(0, 0, 0)
pi = 3.14159265359

def on_on_chat():
    global radius, startpos
    startpos = player.position()
    loops.pause(5000)
    for i in range(radius*2*pi):
        blocks.fill(stoneblock, positions.add(startpos, pos(radius*Math.sin(i/(radius)) -size, 5, radius*Math.cos(i/(radius))-size)), 
            positions.add(startpos, pos(radius*Math.sin(i/(radius))+size, -10, radius*Math.cos(i/(radius))+size)))
    createbordertower(positions.add(startpos, pos(0, 0, radius)))
    createbordertower(positions.add(startpos, pos(0, 0, -radius)))
    createbordertower(positions.add(startpos, pos(-radius, 0, 0)))
    createbordertower(positions.add(startpos, pos(radius, 0, 0)))
    createcentraltower()
    createlightning()
    
def createcentraltower():
    for i in range(radius/size):
        if i%2 == 0:
            setblock = REDSTONE_BLOCK
        else:
            setblock = BLOCK_OF_NETHERITE
        shapes.circle(setblock, positions.add(startpos, pos(0, i+6, 0)), radius-size*i, Axis.Y, ShapeOperation.REPLACE)


def createbordertowers():
    global startpos
    for i in range(size*2+1):
        blocks.fill(BLOCK_OF_NETHERITE, positions.add(startpos, pos(-radius - (2*size - i), -10+10*i,  - (2*size - i))), positions.add(startpos, pos(-radius +  (2*size - i), 10*i, (2*size - i))), FillOperation.REPLACE)    
        blocks.fill(BLOCK_OF_NETHERITE, positions.add(startpos, pos(radius - (2*size - i), -10+10*i,  - (2*size - i))), positions.add(startpos,pos(radius +  (2*size - i), 10*i, (2*size - i))), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_NETHERITE, positions.add(startpos, pos(- (2*size - i), -10+10*i,  radius - (2*size - i))), positions.add(startpos,pos((2*size - i), 10*i,  radius + (2*size - i))), FillOperation.REPLACE)
        blocks.fill(BLOCK_OF_NETHERITE, positions.add(startpos, pos(- (2*size - i), -10+10*i,  -radius - (2*size - i))), positions.add(startpos,pos((2*size - i), 10*i,  -radius + (2*size - i))), FillOperation.REPLACE)

def createbordertower(setpos):
    for i in range(size*2+1):
        blocks.fill(BLOCK_OF_NETHERITE, positions.add(setpos, pos( - (2*size - i), -10+10*i,  - (2*size - i))), positions.add(setpos, pos((2*size - i), 10*i, (2*size - i))), FillOperation.REPLACE)
        if (i < size*2):
            for j in range(5):
                blocks.replace(GLASS, BLOCK_OF_NETHERITE, positions.add(setpos, pos( - (2*size - i- 1), -9+10*i+2*j,  - (2*size - i))), positions.add(setpos, pos((2*size - i - 1), -9+10*i++2*j,  (2*size - i))))
                blocks.replace(GLASS, BLOCK_OF_NETHERITE, positions.add(setpos, pos( - (2*size - i), -9+10*i+2*j,  - (2*size - i - 1))), positions.add(setpos, pos((2*size - i), -9+10*i++2*j,  (2*size - i - 1))))

def createlightning():
    while True:
        mobs.spawn(LIGHTNING_BOLT, positions.add(startpos, pos(-radius, 10*size*2+1,  0)))
        mobs.spawn(LIGHTNING_BOLT, positions.add(startpos, pos(radius, 10*size*2+1,  0)))
        mobs.spawn(LIGHTNING_BOLT, positions.add(startpos, pos(0, 10*size*2+1,  radius)))
        mobs.spawn(LIGHTNING_BOLT, positions.add(startpos, pos(0, 10*size*2+1,  -radius)))
    

player.on_chat("run", on_on_chat)

def on_travelled_walk():
    blocks.replace(AIR, STONE_BRICKS, pos(-10, -10, -10), pos(10, 10, 10))
#player.on_travelled(FLY, on_travelled_walk)
