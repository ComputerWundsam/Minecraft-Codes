depth = 10
radius = 26
pi = 3.14159265359
startpos = pos(0, 0, 0)
pathwidth = 4
lights = [OCHRE_FROGLIGHT, VERDANT_FROGLIGHT, PEARLESCENT_FROGLIGHT]

def on_on_chat():
    global startpos
    startpos = player.position()
    createsidewalls()
    createfloor()
    for i in range(2):
        createlavawell(positions.add(startpos, pos(radius/2 - radius*i, 0, depth/2)))
    createcenterpath()
    createlights()
    savestructure()

def createfloor():
    for i in range((radius+depth)/5):
        for j in range(depth/2+1):
            blocks.fill(BLOCK_OF_QUARTZ, positions.add(startpos, pos(radius+depth-(5*i) - j, -1, depth/2 + j)), positions.add(startpos, pos(radius+depth - (5*i) - j -1, -1, depth/2 + j)), FillOperation.REPLACE)
            blocks.fill(BLOCK_OF_QUARTZ, positions.add(startpos, pos(radius+depth-(5*i) - j, -1, depth/2 - j)), positions.add(startpos, pos(radius+depth - (5*i) - j -1, -1, depth/2 - j)), FillOperation.REPLACE)
            blocks.fill(BLOCK_OF_QUARTZ, positions.add(startpos, pos(-radius-depth + (5*i) + j, -1, depth/2 + j)), positions.add(startpos, pos(-radius-depth + (5*i) + j + 1, -1, depth/2 + j)), FillOperation.REPLACE)
            blocks.fill(BLOCK_OF_QUARTZ, positions.add(startpos, pos(-radius-depth + (5*i) + j, -1, depth/2 - j)), positions.add(startpos, pos(-radius-depth + (5*i) + j + 1, -1, depth/2 - j)), FillOperation.REPLACE)
    createcenterpath()

def createcenterpath():
    blocks.fill(AMETHYST_BLOCK, positions.add(startpos,pos(-pathwidth, -1, 0)), positions.add(startpos,pos(pathwidth, -1, depth)), FillOperation.REPLACE)
    for i in range(2):
        blocks.fill(PURPUR_SLAB, positions.add(startpos,pos(-pathwidth + 2*pathwidth*i, 0, 0)), positions.add(startpos,pos(-pathwidth + 2*pathwidth*i, 0, depth)), FillOperation.REPLACE)

def createlavawell(setpos):
    blocks.fill(PILLAR_QUARTZ_BLOCK, positions.add(setpos, pos(-2, 0, -2)), positions.add(setpos, pos(2, 0, 2)), FillOperation.REPLACE)
    blocks.fill(LAVA, positions.add(setpos, pos(-1, 0, -1)), positions.add(setpos, pos(1, 0, 1)), FillOperation.REPLACE)


def createlights():
    qradius = radius/4
    for i in range(3):
        for j in range(2):
            blocks.fill(BLACKSTONE_WALL, positions.add(startpos, pos(( - qradius - qradius*i)*(-1 + 2*j), radius/2, depth/2)), positions.add(startpos, pos((-qradius - qradius*i) *(-1 + 2*j), radius+1, depth/2)), FillOperation.REPLACE)
            createhanginglight(positions.add(startpos, pos(( - qradius - qradius*i)*(-1 + 2*j), radius/2, depth/2)))



def createsidewalls():
    player.execute("fill " + positions.add(startpos, pos(-radius-2, -1, 0)) + " " + positions.add(startpos, pos(radius+2, radius+2, depth)) + " deepslate_bricks")
    blocks.fill(AIR, positions.add(startpos, pos(-radius-1, 0, 0)), positions.add(startpos, pos(radius+1, radius+1, depth)))
    blocks.fill(NETHER_BRICK_FENCE, positions.add(startpos, pos(-radius-1, 0, 0)), positions.add(startpos,pos(radius+1, radius+1, 0)), FillOperation.REPLACE)
    for i in range(radius*pi/2):
        blocks.fill(AIR, positions.add(startpos, pos(Math.cos(i/radius)*radius, Math.sin(i/radius)*radius, 0)), positions.add(startpos, pos(-Math.cos(i/radius)*radius, Math.sin(i/radius)*radius, 0)), FillOperation.REPLACE)



def createhanginglight(setpos):
    blocks.place(GLOWSTONE, setpos)
    blocks.place(blocks.block_with_data(IRON_TRAPDOOR, 7), positions.add(setpos, pos(0, -1, 0)))
    blocks.place(blocks.block_with_data(IRON_TRAPDOOR, 12), positions.add(setpos, pos(1, 0, 0)))
    blocks.place(blocks.block_with_data(IRON_TRAPDOOR, 13), positions.add(setpos, pos(-1, 0, 0)))
    blocks.place(blocks.block_with_data(IRON_TRAPDOOR, 14), positions.add(setpos, pos(0, 0, 1)))
    blocks.place(blocks.block_with_data(IRON_TRAPDOOR, 15), positions.add(setpos, pos(0, 0, -1)))


def savestructure():
    blocks.save_structure("arch", positions.add(startpos, pos(-radius-2, -1, 0)), positions.add(startpos, pos(radius+2, radius+2, depth)))

player.on_chat("run", on_on_chat)

def on_chat():
    startpos = player.position()
    for i in range(100):
        blocks.load_structure("arch", positions.add(startpos, pos(-radius-2, 0, depth*i)))
        for j in range(2):
            createrune(positions.add(startpos, pos(-radius-2, (j%2)*(radius)/2+2, depth/2-3 + depth*i)), randint(0, runes.length-1))
            createrune(positions.add(startpos, pos(radius+2, (j%2)*(radius)/2+2, depth/2-3 + depth*i)), randint(0, runes.length-1))
player.on_chat("jump", on_chat)

def createrune(setpos, rune):
    setlight = lights[randint(0, lights.length-1)]
    for i in range(runes[rune].length):
        blocks.place(OCHRE_FROGLIGHT, positions.add(setpos, pos(0, runes[rune][i][1], runes[rune][i][0])))
runes=[     #a
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 8], [2, 7], [3, 6],  [1, 11], [2, 10], [3, 9], [4, 10], [5, 11]],
            #b
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 11], [2, 10], [3, 9], [3, 8], [2, 7], [1, 6], [1, 5], [2, 4], [3, 3], [3, 2], [2, 1], [1, 0]],
            #c
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 7], [2, 7], [3, 6], [4, 6], [5, 5], [5, 4],[5, 3],[5, 2],[5, 1],[5, 0]],
            #d
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [1, 4], [2, 5], [4, 7], [5, 8], [6, 9], [6, 8], [6, 7], [6, 6], [6, 5], [6, 4], [6, 3]],
            #e
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 10], [2, 9], [3, 10], [4, 0],[4, 1], [4, 2], [4, 3], [4, 4], [4, 5],[4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11]],
            #f
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 6], [2, 7], [3, 8], [4, 9], [5, 10], [6, 11], [1, 9], [2, 10], [3, 11]],
            #g
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11],[1, 8], [2, 7], [3, 6], [1, 4], [2, 5]],
            #h
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 10], [2, 9], [3, 8], [1, 3], [2, 2], [3, 1], [4, 0],[4, 1], [4, 2], [4, 3], [4, 4], [4, 5],[4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11]],
            #i
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11]],
            #j
            [[2, 0],[2, 1], [2, 2], [2, 3], [2, 4], [2, 5],[2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [1, 9], [0, 8], [-1, 7], [1, 4], [0, 5], [-1, 6], [3, 9], [4, 8], [5, 7], [3, 4], [4, 5], [5, 6]],
            #k
            [[2, 0],[2, 1], [2, 2], [2, 3], [2, 4], [2, 5],[2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [1, 2], [0, 1], [-1, 0], [3, 2], [4, 1], [5, 0]],
            #l
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 11], [2, 10], [3, 9], [4, 8]],
            #m 
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 10], [2, 9], [1, 8], [3, 8], [3, 10], [4, 0],[4, 1], [4, 2], [4, 3], [4, 4], [4, 5],[4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11]],
            #n
            [[2, 0],[2, 1], [2, 2], [2, 3], [2, 4], [2, 5],[2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [0, 8], [1, 7], [3, 5], [4, 4]],
            #o
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 8], [2, 7], [3, 6], [4, 7], [5, 8], [1, 11], [2, 10], [3, 9], [4, 10], [5, 11]],
            #p
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 1], [2, 2], [3, 3], [4, 2], [5, 1], [1, 11], [2, 10], [3, 9], [4, 10], [5, 11]],
            #q 
            [[2, 0],[2, 1], [2, 2], [2, 3], [2, 4], [2, 5],[2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [1, 0], [0, 1], [-1, 0], [3, 11], [4, 10], [5, 11]],
            #r
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 11], [2, 10], [3, 9], [3, 8], [2, 7], [1, 6], [1, 5], [2, 4], [3, 3]],
            #s
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1,6], [2, 7], [3, 8], [4, 9], [4, 0],[4, 1], [4, 2], [4, 3], [4, 4], [4, 5],[4, 6], [4, 7], [4, 8]],
            #t 
            [[2, 0],[2, 1], [2, 2], [2, 3], [2, 4], [2, 5],[2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [1, 10], [0, 9], [-1, 8], [3, 10], [4, 9], [5, 8]],
            #u
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 11], [2, 10], [3, 9], [4, 0],[4, 1], [4, 2], [4, 3], [4, 4], [4, 5],[4, 6], [4, 7], [4, 8]],
            #v
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 1], [2, 2], [3, 3], [4, 4], [4, 5],[4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11]],
            #w 
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 11], [2, 10], [3, 9], [3, 8], [2, 7], [1, 6]],
            #x
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 6], [2, 5], [3, 4], [1, 7], [2, 8], [3, 9]],
            #y
            [[0, 0],[0, 1], [0, 2], [0, 3], [0, 4], [0, 5],[0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [1, 11], [2, 10], [3, 9], [4, 3], [4, 4], [4, 5],[4, 6], [4, 7], [4, 8], [2, 3]],
            #z
            [[2, 0],[2, 1], [2, 2], [2, 3], [2, 4], [2, 5],[2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [1, 8], [0, 9], [-1, 10], [3, 8], [4, 9], [5, 10]],

]

def on_chat2():
    global startpos
    startpos = positions.add(player.position(), pos(0, 0, 0))
    createrune(startpos, 5)
player.on_chat("test", on_chat2)
