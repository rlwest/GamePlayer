##############################
##### (c) E. Greve, 2019 #####
##### FOUR BUTTON PLAYER #####
### SGOMS production model ###
##############################

import sys
#sys.path.append('/Users/robertwest/python_actrSuite')
sys.path.append('Users/User/Documents/GitHub/GamePlayer/')

import python_actr
from random import randrange, uniform
from SimplePython3versionPU_DMBased import MyAgent
from Manager import Manager
log = python_actr.log()
#log=python_actr.log(html=True)
from python_actr.actr import *

class hyrule (python_actr.Model):

### objects for task preformance
    response = python_actr.Model(isa='response', state='state')
    display = python_actr.Model(isa='diplay', state='RP')
    response_entered = python_actr.Model(isa='response_entered', state='no')
    vision_finst = python_actr.Model(isa='motor_finst', state='re_set')

######## run model #########
link = MyAgent()         # name the agent
zelda = Manager()        # name the Manager
env = hyrule()           # name the environment
env.agent = link         # put the agent in the environment
python_actr.log_everything(env)  # print out what happens in the environment
env.run()                # run the environment
python_actr.finished()           # stop the environment
