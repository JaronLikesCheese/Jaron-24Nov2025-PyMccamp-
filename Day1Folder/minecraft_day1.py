# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def Teleport():
    agent.teleport_to_player()

player.on_chat("come",Teleport)
 

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
    agent.move(DOWN,steps)

player.on_chat("mu",move_up)

def turn_left():
    agent.turn(LEFT)

player.on_chat("tl",turn_left)

def turn_right():
    agent.turn(RIGHT)

player.on_chat("tr",turn_right)

###########################################################
def obby1():
    agent.move(FORWARD,4)
    agent.turn(LEFT)
    agent.move(FORWARD,4)
    agent.turn(RIGHT)
    agent.move(FORWARD,3)

player.on_chat("o1",obby1)

def obby2():
    agent.move(FORWARD,4)
    agent.turn(LEFT)
    agent.move(FORWARD,4)
    agent.turn(RIGHT)
    agent.move(FORWARD,3)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,3)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    

player.on_chat("o2",obby2)