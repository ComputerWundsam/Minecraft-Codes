def on_on_chat(stairwidth):
    while agent.inspect(AgentInspection.BLOCK, DOWN) != GRASS:
        agent.set_item(STONE_BRICKS, 1, 1)
        agentplaceblock(DOWN)
        agent.set_item(STONE_BRICK_STAIRS, stairwidth, 1)
        for index in range(stairwidth):
            moveagent(RIGHT, 1)
            checkforblockbreak(DOWN)
            agentplaceblock(DOWN)
        moveagent(RIGHT, 1)
        agent.set_item(STONE_BRICKS, 1, 1)
        agentplaceblock(DOWN)
        moveagent(BACK, 1)
        moveagent(DOWN, 1)
        agent.move(LEFT, stairwidth+1)
player.on_chat("run", on_on_chat)

def moveagent(direction, value):
    checkforblockbreak(direction)
    agent.move(direction, value)

def agentplaceblock(direction):
    checkforblockbreak(direction)
    agent.place(direction)

def checkforblockbreak(direction):
    if(agent.detect(AgentDetection.BLOCK, direction)):
        agent.destroy(direction)
