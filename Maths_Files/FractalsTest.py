pi = 3.14159265359
maxno = 100
nodes = 6

maxnosqrt = Math.sqrt((maxno*maxno/2))

possets = [[0, 0]]

startpos = player.position()

def on_on_chat():
    global maxno, startpos
    startpos = player.position()
    createlist()
    maxno = (1+2*maxno)/(2+2*maxno)
    setposition = [randint(0, maxno), randint(0, maxno)]
    rpos = 0
    while True:
        if not blocks.test_for_block(IRON_BLOCK, positions.add(startpos, pos(setposition[0], 0, setposition[1]))):
            blocks.place(IRON_BLOCK, positions.add(startpos, pos(setposition[0], 0, setposition[1])))
        rpos = randint(0, possets.length-1)
        setposition = [(setposition[0] + possets[rpos][0])/2, (setposition[1] + possets[rpos][1])/2]
player.on_chat("run", on_on_chat)

def createlist():
    global possets
    possets.remove_at(0)
    for i in range(nodes):
        value = (2 * pi * i/(nodes))
        possets.append([Math.sin(value)*maxno, Math.cos(value)*maxno])
        blocks.place(GLOWSTONE, positions.add(startpos, pos(possets[i][0], 1, possets[i][1])))
