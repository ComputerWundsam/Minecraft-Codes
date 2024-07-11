combform = [0, 1, 2, 3, 3, 3, 2, 1, 0]

linesize = 6
counter = 0

def on_on_chat():
    startpos = player.position()
    honeycombbridge(startpos)
player.on_chat("run", on_on_chat)

def honeycombbridge(setpos):
    global counter
    while True:
        for j in range (linesize):
            for i in range(combform.length):
                blocks.place(HONEYCOMB_BLOCK, positions.add(setpos, pos(i, 0, combform[i]+j*6)))
                blocks.place(HONEYCOMB_BLOCK, positions.add(setpos, pos(i, 0, -combform[i]+j*6)))
                if(combform[i] > 0):
                    blocks.fill(HONEY_BLOCK, positions.add(setpos, pos(i, 0, combform[i]-1+j*6)), positions.add(setpos, pos(i, 0, -combform[i]+1+j*6)))
            mobs.spawn(BEE, positions.add(setpos, pos(-combform.length/2, 2, j*6)))
        counter += 1
        setpos = positions.add(setpos, pos(6, 0, 3 - (6*(counter%2))))

