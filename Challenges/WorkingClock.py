# How to use the code: 
# 
# Open MakeCode > Copy the Code and insert it in a python file for MakeCode
# 
# First: Use the createhands command and let the hands made out of froglight be created. 
# To use the createhands command, open the chat and write "hands" (without quotation marks
# Create them in an empty space, ideally high up in the sky. 
# 
# Second: create the clock. Write "clock" in the chat, and the clock will be created. YOu can change the size of the clock.
# The code is not perfect, but it works. 

outradius = 20
radius = 15
inradius = 13
c = 60
pi = 3.14159265359

def createclock():
    startpos = player.position()
    blocks.fill(GRAY_CONCRETE, positions.add(startpos, pos(0, 0, 2)), positions.add(startpos, pos(52, 52, 2)), FillOperation.REPLACE)
    for i in range(12):
        value = (2*pi*i)/(12)
        if((i+11)%12+1) >= 10:
            blocks.print(str((i+11)%12+1), WHITE_CONCRETE, positions.add(startpos, pos(-Math.sin(value)*outradius+28, Math.cos(value)*outradius+26, 1)), WEST)
        else:
            blocks.print(str((i+11)%12+1), WHITE_CONCRETE, positions.add(startpos, pos(-Math.sin(value)*outradius+25, Math.cos(value)*outradius+25, 1)), WEST)

    while True:
        asktime = gameplay.time_query(DAY_TIME)
        blocks.load_structure("secondhand" + ((int((asktime+6000)/12000*60)%60)), positions.add(startpos, pos(8, 11, 0)))
        blocks.load_structure("firsthand" + ((int(asktime/1000*60)%60)), positions.add(startpos, pos(8, 11, -1)))
player.on_chat("clock", createclock)

def createhands(): 
    startpos = player.position()
    secondpos = positions.add(startpos, pos(40, 0, 0))
    for i in range(c):
        value = (2*pi*i)/(c)
        for j in range(radius):
            blocks.place(PEARLESCENT_FROGLIGHT, positions.add(startpos, pos(-Math.sin(value)*j, Math.cos(value)*j, 2*i)))
        for j in range(inradius):
            blocks.place(VERDANT_FROGLIGHT, positions.add(secondpos, pos(-Math.sin(value)*j, Math.cos(value)*j, 2*i)))
        blocks.save_structure("firsthand"+i, positions.add(startpos, pos(-15, -15, 2*i)), positions.add(startpos, pos(15, 15, 2*i)))
        blocks.save_structure("secondhand"+i, positions.add(secondpos, pos(-15, -15, 2*i)), positions.add(secondpos, pos(15, 15, 2*i)))
player.on_chat("hands", createhands)
