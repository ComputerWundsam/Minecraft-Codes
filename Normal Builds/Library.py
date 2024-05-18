houseblock = BRICKS
roofblock = PLANKS_DARK_OAK
shelves = BOOKSHELF
lights = OCHRE_FROGLIGHT
floor = POLISHED_DIORITE
pillar = PILLAR_QUARTZ_BLOCK
window = GLASS
librarytext = [525, 557, 540, 561, 36]

def on_on_chat(width, height, depth):
    startpos = positions.add(player.position().to_world(), pos_camera(0, 0, 3))
    for i in range(width):
        blocks.fill(houseblock, positions.add(startpos, pos(-i, 0, 0)), positions.add(startpos, pos(-i, height+width-i, 0)))        
        blocks.fill(houseblock, positions.add(startpos, pos(i, 0, 0)), positions.add(startpos, pos(i, height+width-i, 0)))
        blocks.fill(houseblock, positions.add(startpos, pos(-i, 0, depth)), positions.add(startpos, pos(-i, height+width-i, depth)))
        blocks.fill(houseblock, positions.add(startpos, pos(i, 0, depth)), positions.add(startpos, pos(i, height+width-i, depth)))
    for i in range(width+1):
        blocks.fill(roofblock, positions.add(startpos, pos(-i, height+width+1-i, 0)), positions.add(startpos, pos(-i, height+width+2-i, depth)))
        blocks.fill(roofblock, positions.add(startpos, pos(i, height+width+1-i, 0)), positions.add(startpos, pos(i, height+width+2-i, depth)))
    blocks.fill(houseblock, positions.add(startpos, pos(width, 0, 0)), positions.add(startpos, pos(width, height, depth)))
    blocks.fill(houseblock, positions.add(startpos, pos(-width, 0, 0)), positions.add(startpos, pos(-width, height, depth)))
    for i in range(width/5):
        blocks.fill(pillar, positions.add(startpos, pos(-i*5, 0, 0)), positions.add(startpos, pos(-i*5, height+width-i*5, 0)))
        blocks.fill(pillar, positions.add(startpos, pos(i*5, 0, 0)), positions.add(startpos, pos(i*5, height+width-i*5, 0)))
        blocks.fill(pillar, positions.add(startpos, pos(-i*5, 0, depth)), positions.add(startpos, pos(-i*5, height+width-i*5, depth)))
        blocks.fill(pillar, positions.add(startpos, pos(i*5, 0, depth)), positions.add(startpos, pos(i*5, height+width-i*5, depth)))
    for i in range(4):
        blocks.fill(pillar, positions.add(startpos, pos(-width + ((2*width) * (i%2)), 0, depth * (i//2))), positions.add(startpos, pos(-width + ((2*width) * (i%2)), height, depth * (i//2))))
    blocks.fill(shelves, positions.add(startpos, pos(width-1, 0, 1)), positions.add(startpos, pos(width-1, height+1, depth-1)))
    blocks.fill(shelves, positions.add(startpos, pos(-width+1, 0, 1)), positions.add(startpos, pos(-width+1, height+1, depth-1)))
    blocks.fill(lights, positions.add(startpos, pos(-width+2, height+3, 1)), positions.add(startpos, pos(-width+2, height+3, depth-1)))
    blocks.fill(lights, positions.add(startpos, pos(width-2, height+3, 1)), positions.add(startpos, pos(width-2, height+3, depth-1)))

    for i in range(librarytext.length):
        blocks.place(librarytext[i], positions.add(startpos, pos(2-i, 5, -1)))
    blocks.fill(pillar, positions.add(startpos, pos(-2, 0, -1)), positions.add(startpos, pos(2, 4, -1)))    
    blocks.fill(AIR, positions.add(startpos, pos(-1, 0, 0)), positions.add(startpos, pos(1, 3, -1)))
    blocks.fill(floor, positions.add(startpos, pos(-width, -1, 0)), positions.add(startpos, pos(width, -1, depth)))

    for i in range(width/3):
        blocks.fill(shelves, positions.add(startpos, pos(-3*i, 0, 4)), positions.add(startpos, pos(-3*i, height+1, depth-4)))
        blocks.fill(shelves, positions.add(startpos, pos(3*i, 0, 4)), positions.add(startpos, pos(3*i, height+1, depth-4)))

    for i in range(width/6):
        blocks.fill(lights, positions.add(startpos, pos(-6*i, height+2, 4)), positions.add(startpos, pos(-6*i, height+2, depth-4)))
        blocks.fill(lights, positions.add(startpos, pos(6*i, height+2, 4)), positions.add(startpos, pos(6*i, height+2, depth-4)))
        for j in range(depth//5-1):
            blocks.fill(pillar, positions.add(startpos, pos(-6*i, 0, 4+5*j)), positions.add(startpos, pos(-6*i, height+width-i*5, 4+5*j)))
            blocks.fill(pillar, positions.add(startpos, pos(6*i, 0, 4+5*j)), positions.add(startpos, pos(6*i, height+width-i*5, 4+5*j)))

    for i in range((height+width)//5):
        blocks.replace(window, houseblock, positions.add(startpos, pos(-width, 2+i*5, 0)), positions.add(startpos, pos(width, 2+i*5, 0)))
        blocks.replace(window, houseblock, positions.add(startpos, pos(-width, 2+i*5, depth)), positions.add(startpos, pos(width, 2+i*5, depth)))


player.on_chat("run", on_on_chat)
