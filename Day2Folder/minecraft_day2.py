# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def choptree(height):
    for i in range (height):
        agent.destroy(FORWARD)
        agent.move(UP,height)
    agent.move(DOWN,height)
    agent.collect_all()

player.on_chat("chop",choptree)

#####################teleport to player###################################################

def Teleport():
    agent.teleport_to_player()

player.on_chat("come",Teleport)