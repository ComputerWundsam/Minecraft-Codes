walls = PLANKS_OAK
pillars = LOG_OAK
blade = WOOL
window = GLASS_PANE
width = 8
height = 8
reps = 4
bdist = 7

def makewindmill():
    startpos = positions.add(player.position(), pos(0, 0, -5 ))
    loops.pause(5000)
    for i in range(reps):
        blocks.fill(walls, positions.add(startpos, pos(i, 0+height*i, i)), positions.add(startpos, pos(width-i, height+height*i, width-i)), FillOperation.HOLLOW)
        blocks.fill(pillars, positions.add(startpos, pos(i, 0+height*i, i)), positions.add(startpos, pos(width-i, 0+height*i, width-i)), FillOperation.HOLLOW)
        blocks.fill(pillars, positions.add(startpos, pos(i, height+height*i, i)), positions.add(startpos, pos(width-i, height+height*i, width-i)), FillOperation.HOLLOW)
        for j in range(4):
            blocks.fill(pillars, positions.add(startpos, pos(i + ((width-(2*i))*(j%2))  , 0+height*i, i + (((width-(2*i))*(j//2))))), 
                positions.add(startpos, pos(i + (((width-(2*i)))*(j%2)), height+height*i, i + ((width-(2*i))*(j//2)))))
    blocks.place(OAK_DOOR, positions.add(startpos, pos(width, 1, width/2,)))
    makewindows(positions.add(startpos, pos(width/2, 0, width/2,)))
    makewings(positions.add(startpos, pos(width/2, height*reps-2, width/2,)))

def makewindows(windowpos):
    for i in range((height*reps/4)):
        blocks.replace(window, walls, positions.add(windowpos, pos(-width, i*height + height/2, 0)), positions.add(windowpos, pos(width, i*height + height/2, 0)))
        blocks.replace(window, walls, positions.add(windowpos, pos(0, i*height + height/2, -width)), positions.add(windowpos, pos(0, i*height + height/2, width)))
     
def makewings(wingpos):
    blocks.fill(pillars, wingpos, positions.add(wingpos, pos(bdist, 0, 0)))
    blocks.fill(pillars, positions.add(wingpos, pos(bdist, -20, 0)), positions.add(wingpos, pos(bdist, 20, 0)))
    blocks.fill(pillars, positions.add(wingpos, pos(bdist, 0, -20)), positions.add(wingpos, pos(bdist, 0, 20)))
    for i in range(9):
        blocks.fill(blade, positions.add(wingpos, pos(bdist, 3+2*i, 1)), positions.add(wingpos, pos(bdist, 4+2*i, 1+i)))
        blocks.fill(blade, positions.add(wingpos, pos(bdist, -(3+2*i), -1)), positions.add(wingpos, pos(bdist, -(4+2*i), -(1+i))))
        blocks.fill(blade, positions.add(wingpos, pos(bdist, -1, 3+2*i)), positions.add(wingpos, pos(bdist, -(1+i), 4+2*i)))
        blocks.fill(blade, positions.add(wingpos, pos(bdist, 1, -(3+2*i))), positions.add(wingpos, pos(bdist, 1+i, -(4+2*i))))
player.on_chat("run", makewindmill)
