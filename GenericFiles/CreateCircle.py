pi = 3.14159265359
radius = 5

for i in range(radius*pi)
  blocks.fill(IRON_BLOCK, positions.add(startpos, pos(0, radius, 0)), positions.add(startpos, pos(Math.sin(i/radius)*radius, radius, Math.cos(i/radius)*radius)))
