setblocks = [BLACK_CONCRETE_POWDER, RED_CONCRETE_POWDER, GRAY_CONCRETE_POWDER, BLUE_CONCRETE_POWDER, GREEN_CONCRETE_POWDER, CYAN_CONCRETE_POWDER, LIGHT_BLUE_CONCRETE_POWDER, YELLOW_CONCRETE_POWDER, WHITE_CONCRETE_POWDER ]

def on_on_chat():
    startpos = player.position()
    blocks.place(TORCH, positions.add(startpos, pos(0, 0, 0)))
    for i in range(picture.length):
        for j in range(picture[i].length):
            blocks.place(IRON_BLOCK, positions.add(startpos, pos(j, i+j+1, i)))
            blocks.place(TORCH, positions.add(startpos, pos(j+1, i+j+1, i)))
        for j in range(picture[i].length):
            blocks.place(setblocks[picture[i][j]], positions.add(startpos, pos(picture[i].length-1-j, (picture[i].length-1+i)-j+1, i)))
        blocks.place(TORCH, positions.add(startpos, pos(0, i+1, i+1)))
player.on_chat("Miku", on_on_chat)


picture = [[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2,1,2,2,2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,1,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,1,1,1,2,0,0,2,4,4,4,4,4,4,4,4,4,4,4,3,4,8,8,
  8,8,8,8,8,8,2,2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,2,1,1,6,7,2,3,4,5,6,5,5,5,5,5,5,5,5,5,5,5,4,4,
  4,8,8,8,2,0,1,1,2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,2,1,1,4,7,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,
  5,4,4,2,0,0,2,1,1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,2,1,1,0,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
  5,5,5,3,0,0,2,1,1,2,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,2,1,1,0,3,4,6,5,5,5,5,5,5,5,5,5,6,5,5,5,5,5,5,5,5,5,
  5,5,5,5,3,5,7,2,1,1,2,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,2,1,1,0,3,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,6,
  5,5,5,5,5,3,7,4,1,1,2,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,2,1,1,2,3,3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,6,6,6,5,6,
  5,5,5,5,5,4,4,6,0,1,1,2,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,2,1,1,2,4,3,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,6,6,6,6,
  5,5,5,4,5,5,3,3,3,1,1,2,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,2,1,1,2,3,5,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,6,5,5,6,5,5,
  5,5,5,5,4,4,3,4,5,0,1,1,2,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,0,1,0,3,6,6,6,6,6,6,6,6,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
  5,5,5,5,5,4,3,4,5,4,2,1,1,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,0,0,5,6,6,6,6,5,5,5,5,3,5,6,6,6,5,5,5,5,5,5,5,5,5,5,5,
  5,5,5,6,5,4,4,3,5,5,0,1,1,2,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,2,2,6,6,6,5,5,5,5,5,5,3,5,6,5,6,5,5,4,5,5,5,5,6,5,5,6,
  5,5,5,5,6,5,4,3,4,5,4,2,1,1,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,3,4,6,6,6,5,5,5,5,5,3,6,4,5,5,5,5,6,3,5,5,5,5,5,5,4,5,
  5,5,5,5,5,5,4,3,3,5,5,0,1,1,2,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,3,5,5,5,5,5,4,5,5,3,7,7,3,5,5,5,5,5,3,3,5,5,5,5,5,4,5,
  5,5,5,5,5,5,4,3,3,5,5,0,1,1,2,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,3,5,5,5,5,5,4,5,5,4,7,7,3,5,5,5,6,5,2,4,4,6,5,3,5,5,4,
  6,5,5,5,5,5,5,3,3,4,3,1,1,2,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,4,3,4,6,5,5,5,4,5,4,7,7,7,4,4,5,5,5,5,2,7,4,5,5,3,3,5,4,
  5,5,5,5,5,5,5,3,3,3,0,1,0,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,3,3,3,5,5,5,5,3,4,7,7,7,7,7,3,4,5,6,5,4,7,7,3,4,3,4,4,4,
  4,5,5,5,5,5,5,3,3,0,1,0,3,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,4,3,4,5,5,5,5,0,3,6,7,7,7,7,4,4,5,6,5,4,7,7,7,4,3,7,4,3,
  3,6,5,5,5,5,5,3,0,1,1,3,5,4,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,4,4,4,5,5,5,4,3,0,2,0,0,4,7,7,3,5,6,5,4,7,7,7,7,3,7,7,3,
  3,5,5,5,5,5,5,3,0,1,2,5,5,4,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,4,5,4,5,5,5,4,0,7,7,0,0,0,2,7,3,4,5,5,4,7,7,7,7,7,4,7,7,
  2,5,5,5,5,5,5,3,0,0,4,5,5,4,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,4,5,5,4,4,6,5,3,2,7,2,3,0,3,4,7,7,3,5,6,4,7,7,7,2,0,0,0,4,
  4,5,5,5,5,5,5,4,3,4,4,5,6,4,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,4,5,4,4,4,5,5,3,2,7,3,3,3,4,7,7,7,4,3,5,4,7,7,0,0,0,0,2,2,
  0,5,5,5,5,5,6,4,4,4,4,5,6,4,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,4,5,4,5,4,5,5,3,2,7,4,4,4,4,3,7,7,7,3,4,4,7,4,3,3,3,7,4,7,
  0,4,5,5,4,5,6,4,5,3,4,5,6,4,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,4,5,4,5,3,4,5,3,2,7,6,5,6,6,3,7,7,7,7,3,4,6,7,3,3,3,6,4,7,
  2,4,5,5,4,4,5,5,4,3,4,5,5,5,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,4,5,4,3,3,3,6,4,4,7,7,6,4,4,7,7,7,7,7,7,3,4,7,3,5,5,4,4,7,
  2,4,5,5,3,3,5,5,4,3,4,5,5,5,3,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,4,5,4,3,3,4,5,4,2,7,7,7,7,7,7,7,7,7,7,7,7,4,7,4,6,6,5,7,7,
  5,5,5,5,0,0,3,4,4,3,4,5,5,5,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,4,5,5,4,4,3,8,4,5,0,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,4,4,7,7,7,
  4,5,6,4,0,0,8,8,4,3,4,5,5,5,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,4,5,5,4,4,3,8,3,5,0,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
  4,6,5,2,1,2,8,8,8,3,4,5,6,5,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,4,5,5,4,4,3,8,8,4,3,0,2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
  4,5,4,0,1,8,8,8,8,4,4,5,6,5,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,4,5,5,4,4,4,8,8,4,4,2,0,4,4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,2,
  5,5,2,0,2,8,8,8,8,3,4,5,5,5,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,4,5,5,4,3,8,8,8,8,4,8,2,2,4,4,2,4,7,7,7,7,7,7,7,7,7,7,4,2,4,
  5,4,8,8,8,8,8,8,8,3,4,4,5,5,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,5,5,5,4,3,8,8,8,8,8,8,8,2,3,2,8,8,4,5,2,2,2,4,2,2,2,8,8,8,3,
  4,8,8,8,8,8,8,8,8,4,4,4,6,5,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,4,5,5,4,4,3,8,8,8,8,8,8,8,8,2,2,8,4,2,6,4,3,6,6,4,6,8,8,8,4,8,
  8,8,8,8,8,8,8,8,8,4,4,4,5,5,5,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,4,5,5,4,4,3,8,8,8,8,8,8,8,8,8,8,2,7,7,2,4,4,4,4,7,7,2,8,8,8,8,
  8,8,8,8,8,8,8,8,8,4,4,4,5,5,5,4,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,4,5,5,4,4,3,8,8,8,8,8,8,8,8,8,2,2,4,7,7,4,4,7,7,7,7,1,2,8,8,8,
  8,8,8,8,8,8,8,8,8,3,4,4,5,5,5,3,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,4,5,5,4,4,3,8,8,8,8,8,8,8,8,8,0,0,4,7,7,4,4,7,7,2,7,1,2,8,8,8,
  8,8,8,8,8,8,8,8,8,3,3,3,6,5,5,4,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,5,5,5,3,4,3,8,8,8,8,8,8,8,8,2,0,0,4,7,7,5,4,7,7,7,2,3,2,2,8,8,
  8,8,8,8,8,8,8,8,8,3,3,3,6,5,6,4,8,8,8,8,8,8,8,8],
 [8,8,8,8,4,5,5,5,3,4,3,8,8,8,8,8,8,8,2,0,0,0,5,7,5,5,4,7,7,7,2,0,0,0,8,8,
  8,8,8,8,8,8,8,8,8,4,3,3,5,5,6,4,8,8,8,8,8,8,8,8],
 [8,8,8,8,3,5,5,5,3,4,3,8,8,8,8,8,8,2,0,0,0,2,6,7,4,5,4,7,7,7,7,0,0,0,2,8,
  8,8,8,8,8,8,8,8,8,4,3,3,5,5,5,4,8,8,8,8,8,8,8,8],
 [8,8,8,8,4,5,5,5,3,4,3,8,8,8,8,8,2,0,0,0,0,4,6,7,2,5,4,7,7,7,6,0,0,0,0,2,
  8,8,8,8,8,8,8,8,8,3,3,4,5,5,5,4,8,8,8,8,8,8,8,8],
 [8,8,8,8,3,5,5,6,3,4,3,8,8,8,8,8,3,0,0,0,2,2,7,7,3,5,4,7,7,7,7,4,0,0,0,2,
  8,8,8,8,8,8,8,8,8,3,3,4,5,5,5,5,4,8,8,8,8,8,8,8],
 [8,8,8,8,3,5,5,5,4,4,3,8,8,8,8,4,3,3,0,0,4,7,7,7,4,5,4,7,7,7,7,4,2,0,3,3,
  2,8,8,8,8,8,8,8,8,3,3,5,5,6,5,5,3,8,8,8,8,8,8,8],
 [8,8,8,8,3,5,5,5,5,3,3,8,8,8,8,7,7,2,3,2,4,7,7,7,4,5,4,7,7,7,7,6,0,0,3,3,
  3,3,8,8,8,8,8,8,8,4,3,5,5,5,5,5,4,8,8,8,8,8,8,8],
 [8,8,8,8,3,5,6,5,5,3,3,8,8,8,8,4,4,2,8,8,2,6,7,7,0,0,2,7,7,6,6,4,0,0,2,2,
  3,4,8,8,8,8,8,8,8,4,3,5,5,5,5,5,4,8,8,8,8,8,8,8],
 [8,8,8,8,3,4,5,5,5,3,3,8,8,8,8,8,8,8,8,2,0,3,6,2,0,0,0,7,6,4,0,0,0,0,3,3,
  3,2,8,8,8,8,8,8,8,4,3,5,5,5,5,5,4,8,8,8,8,8,8,8],
 [8,8,8,8,3,4,5,5,5,4,3,8,8,8,8,8,8,8,4,0,0,0,0,0,0,0,0,2,3,0,0,0,0,0,0,4,
  7,4,8,8,8,8,8,8,8,3,4,5,5,5,5,5,4,8,8,8,8,8,8,8],
 [8,8,8,8,4,4,4,5,5,5,3,3,8,8,8,8,8,8,4,3,3,0,0,0,0,0,0,0,0,0,0,3,3,3,2,8,
  4,8,8,8,8,8,8,8,8,3,5,6,5,5,5,5,4,8,8,8,8,8,8,8],
 [8,8,8,8,8,3,4,5,5,5,4,3,8,8,8,8,8,8,8,8,3,4,4,3,0,3,3,0,3,4,4,4,4,3,8,8,
  8,8,8,8,8,8,8,8,8,3,5,5,4,5,5,6,4,8,8,8,8,8,8,8],
 [8,8,8,8,8,4,4,4,5,5,5,3,8,8,8,8,8,8,8,8,8,3,4,4,3,4,4,3,3,4,4,4,2,8,8,8,
  8,8,8,8,8,8,8,8,8,4,6,5,4,5,5,5,4,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,3,3,4,5,5,3,8,8,8,8,8,8,8,8,8,8,4,4,4,3,2,4,7,7,7,5,2,8,8,8,
  8,8,8,8,8,8,8,8,3,5,5,5,3,5,5,5,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,3,3,4,5,4,3,8,8,8,8,8,8,8,8,8,3,3,3,3,2,2,4,4,3,3,8,8,8,8,
  8,8,8,8,8,8,8,8,4,5,5,4,3,5,5,4,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,3,3,4,4,3,4,8,8,8,8,8,8,8,8,2,2,2,2,2,2,3,3,2,0,8,8,8,8,
  8,8,8,8,8,8,8,4,5,5,4,4,4,5,4,4,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,3,3,3,4,3,8,8,8,8,8,8,8,8,2,3,2,2,2,2,2,2,2,0,8,8,8,8,
  8,8,8,8,8,8,8,4,5,4,4,3,5,4,4,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,4,4,4,3,3,8,8,8,8,8,8,8,2,2,2,2,2,8,3,2,2,2,8,8,8,8,
  8,8,8,8,8,8,4,5,4,4,4,3,4,4,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2,2,2,2,2,8,0,2,2,2,8,8,8,8,
  8,8,8,8,8,4,4,4,4,3,3,3,4,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2,3,2,2,2,8,2,2,2,2,8,8,8,8,
  8,8,8,8,8,3,3,3,4,8,4,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,4,3,3,3,8,8,2,2,2,2,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,3,3,4,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
 [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,
  8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]]
