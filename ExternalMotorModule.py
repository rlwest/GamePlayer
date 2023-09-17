import sys
import python_actr
from python_actr.actr import *
from random import randrange, uniform

########################
##### MOTOR MODULE #####
########################

class ExternalMotorModule(python_actr.Model): # defines actions in the environment

##### This instantly causes changes in the environment
##### It is not a proper part of the agent
    def referee_action(self, env_object, slot_name, slot_value):
        x = self.parent.parent[env_object]
        setattr(x, slot_name, slot_value)
        print('[referee]')
        print('object=',env_object)
        print('slot=',slot_name)
        print('value=',slot_value)

##### This sees the code, which is a value in the state slot of the display object
    def see_code(self):
        self.parent.parent.vision_finst.state = 'busy' # register that the vision system is busy
        yield 0.47
        print ('[vision - looking]')
        code = self.parent.parent.display.state # get the code from the state slot of the display object

        # process state retrived from display
        visual_memory = {'purple':'first:AK second:HW third:RP fourth:finished',
                         'blue':'first:RP second:HW third:AK fourth:finished',
                         'green':'first:HW second:RP third:AK fourth:finished'}
        retrived_visual_memory = ' '+visual_memory[code.split()[1].split(':')[1]]
        print ('[vision - I see the code is..',code,']')
        code = code + retrived_visual_memory

        # put code into visual buffer code slot
        self.parent.b_visual.set(code)
        self.parent.b_method.set('state:finished')
        self.parent.parent.vision_finst.state = 'finished'

##### This enters the code
    def enter_response(self, env_object, slot_value):
        self.parent.parent.vision_finst.state = 'busy'
        yield 0.63
##        x = eval('self.parent.parent.' + env_object)
##        x.state = slot_value
##        print (env_object);
        print ('[motor - entering',slot_value, ']')
        self.parent.parent.vision_finst.state = 'finished'

#### This resets the finst state indicating the action is finished
#### Currently using the vision finst for all actions (so no interleaving or parallal)

    def vision_finst_reset(self):
        self.parent.parent.vision_finst.state = 're_set' # reset the vision_finst
        print('[motor module] vision_finst reset')
