# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def choptree(height):
    for i in range (height):
        agent.destroy(FORWARD)
        agent.move(UP,1)
    
    agent.collect_all()


  



player.on_chat("chop",choptree)

#####################teleport to player###################################################

def Teleport():
    agent.teleport_to_player()

player.on_chat("come",Teleport)

#############################################
 

#  agent.move(BACK, steps)
#  agent.move(UP, steps)
#  agent.move(DOWN, steps)

#  # TURN COMMANDS

#  agent.turn(LEFT)
#  agent.turn(RIGHT)

def move_forward(steps):
    agent.move(FORWARD, steps)

player.on_chat("mf",move_forward)

def move_back(steps):
    agent.move(BACK,steps)

player.on_chat("mb",move_back)

def move_down(steps):
    agent.move(DOWN,steps)

player.on_chat("md",move_down)

def move_up(steps):
    agent.move(UP,steps)

player.on_chat("mu",move_up)

def turn_left():
    agent.turn(LEFT)

player.on_chat("tl",turn_left)

def turn_right():
    agent.turn(RIGHT)

player.on_chat("tr",turn_right)





def chopmore(height):
    for i in range (height):
        agent.destroy(FORWARD)
        agent.move(UP,1)
        agent.move(FORWARD,1)
        agent.destroy(FORWARD)
    
    agent.collect_all()

  



player.on_chat("chopmore",chopmore)




def chopdown(height):
    for i in range (height):
        agent.destroy(FORWARD)
        agent.move(DOWN,1)
    
    agent.collect_all()

  



player.on_chat("cd",chopdown)




##################################################
def mine(blocks):
    for count in range(blocks):
        agent.move(FORWARD,1)
        agent.destroy(FORWARD)

    agent.collect_all()
player.on_chat("m",mine)

  
    