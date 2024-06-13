fibonacci = [1, 1, 2, 3, 5, 8, 13]
startpos = pos(0, 0, 0)
woodblock = PLANKS_ACACIA
mastblock = PLANKS_DARK_OAK
fenceblock = ACACIA_FENCE
sailblock = WOOL
counter = 0

def on_on_chat():
    global startpos, counter
    counter = 0
    startpos = player.position()
    blocks.fill(woodblock, positions.add(startpos, pos(-4, 3, 0)), positions.add(startpos, pos(-1, 3, 0)))
    blocks.place(woodblock, positions.add(startpos, pos(-1, 2, 0)))
    for i in range(fibonacci.length):
        for j in range(fibonacci[i]):
            makehull(i)
        blocks.place(fenceblock, positions.add(startpos, pos(-fibonacci[i], 4, -i+1)))
        blocks.place(fenceblock, positions.add(startpos, pos(-fibonacci[i], 4, i-1)))
    for i in range(2):
        for j in range(fibonacci[fibonacci.length - i - 2]):
            makehull(fibonacci.length - i - 2)
        blocks.place(fenceblock, positions.add(startpos, pos(-fibonacci[fibonacci.length - i - 2]-1, 4, -(fibonacci.length - i - 2))))
        blocks.place(fenceblock, positions.add(startpos, pos(-fibonacci[fibonacci.length - i - 2]-1, 4, fibonacci.length - i - 2)))
    blocks.fill(fenceblock, positions.add(startpos, pos(-1, 4, fibonacci.length - i - 2)), 
                            positions.add(startpos, pos(-1, 4, -(fibonacci.length - i - 2))))
    while counter > 0:
        makesail(positions.add(startpos, pos(-counter, 0, 0)))
        counter -= 15


def makehull(posvalue):
    global startpos, counter
    shapes.circle(woodblock, startpos, posvalue, Axis.X, ShapeOperation.REPLACE)
    blocks.fill(AIR, positions.add(startpos, pos(0, 1, -posvalue)), positions.add(startpos, pos(0, posvalue, posvalue)))
    blocks.fill(woodblock, positions.add(startpos, pos(0, 1, -posvalue)), positions.add(startpos, pos(0, 3, posvalue)))
    blocks.place(fenceblock, positions.add(startpos, pos(0, 4, -posvalue)))
    blocks.place(fenceblock, positions.add(startpos, pos(0, 4, posvalue)))
    
    
    startpos = positions.add(startpos, pos(1, 0, 0))
    counter += 1 

def makesail(setpos):
    blocks.fill(mastblock, setpos, positions.add(setpos, pos(0, 20, 0)))
    blocks.fill(mastblock, positions.add(setpos, pos(-1, 20, -fibonacci[fibonacci.length-1])), positions.add(setpos, pos(-1, 20, fibonacci[fibonacci.length-1])))
    blocks.fill(mastblock, positions.add(setpos, pos(-1, 8, -fibonacci[fibonacci.length-1])), positions.add(setpos, pos(-1, 8, fibonacci[fibonacci.length-1])))
    blocks.fill(sailblock, positions.add(setpos, pos(-2, 9, -fibonacci[fibonacci.length-1])), positions.add(setpos, pos(-2, 11, fibonacci[fibonacci.length-1])))
    blocks.fill(sailblock, positions.add(setpos, pos(-3, 12, -fibonacci[fibonacci.length-1])), positions.add(setpos, pos(-3, 16, fibonacci[fibonacci.length-1])))
    blocks.fill(sailblock, positions.add(setpos, pos(-2, 17, -fibonacci[fibonacci.length-1])), positions.add(setpos, pos(-2, 19, fibonacci[fibonacci.length-1])))

player.on_chat("run", on_on_chat)


def on_travelled_walk():
    blocks.fill(AIR, pos(-10, 0, -10), pos(10, 20, 10))
#player.on_travelled(FLY, on_travelled_walk)
