iwidth = 30
saplings = [BIRCH_SAPLING, CHERRY_SAPLING, JUNGLE_SAPLING, OAK_SAPLING]
flowers = [OXEYE_DAISY, POPPY, BLUE_ORCHID, ALLIUM, AZURE_BLUET, RED_TULIP, PINK_TULIP, CORNFLOWER, LILY_OF_THE_VALLEY]

def on_on_chat():
    startpos = player.position().to_world()
    left = 1
    right = 1
    counter = 0
    while left < iwidth and right < iwidth:
        blocks.fill(GRASS, positions.add(startpos, pos(left, -1, counter) ),  positions.add(startpos, pos(-right, 0, counter)), FillOperation.REPLACE)
        if((left + right) > 5):
            plantflowers(startpos, counter, left, right)
        counter += 1
        left += randint(0, 2)
        right += randint(0, 2)
        if(left > iwidth/2):
            left -= randint(0, 2)
        if(right > iwidth/2):
            right -= randint(0, 2)
    while left > -right:
        blocks.fill(GRASS, positions.add(startpos, pos(left, -2, counter) ),  positions.add(startpos, pos(-right, 0, counter)), FillOperation.REPLACE)
        if((left + right) > 5):
            plantflowers(startpos, counter, left, right)
        left -= randint(0, 2)
        right -= randint(0, 2)
        counter += 1

def plantflowers(startpos, counter, left, right):
    for i in range(5):
        blocks.fill(GRASS, positions.add(startpos, pos(left-(left*i/5), -2-i, counter) ),  positions.add(startpos, pos(-right+(right*i/5), -2-i, counter)), FillOperation.REPLACE)
    blocks.place(saplings[randint(0, saplings.length-1)], positions.add(startpos, pos(randint(left, -right), 1, counter)))
    for j in range(randint(1, (left+right)/10)):
        blocks.place(flowers[randint(0, flowers.length-1)], positions.add(startpos, pos(randint(left, -right), 1, counter)))
    if(randint(0, 20) > 19):
        waterpos = randint(left-2, -right+4)
        blocks.fill(WATER, positions.add(startpos, pos(waterpos, -1, counter-2)),  positions.add(startpos, pos(waterpos+2, 0, counter)))
player.on_chat("run", on_on_chat)


