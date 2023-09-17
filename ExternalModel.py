import sys
import python_actr
from ExternalMotorModule import *
from RTModule import *
from python_actr.actr import *
from random import randrange, uniform


class MyAgent(ACTR):

# BUFFERS
    focus=Buffer()
    b_context = Buffer()
    b_unit_task = Buffer()
    b_method = Buffer()
    b_operator = Buffer()
    b_DM = Buffer()
    b_motor = Buffer()
    b_visual = Buffer()

    motor = ExternalMotorModule(b_motor)
    DM = Memory(b_DM)

    # initial buffer contents
    b_context.set('status:unoccupied')
    b_visual.set('code:00')



########### create productions for choosing planning units ###########
#TODO: Change this to a look - to do this predoctions in this step are removed

    def START_start(b_context='status:unoccupied'):
        b_unit_task.set('unit_task:START state:running')
        b_context.modify(status='planning_unit_start')
        print ('Look at code to determin new planning unit and unit task')
        ####################################
        # Planning unit start choices contain a color cue, represents prosesed visual info
        choices = ['code:AK color:purple',
                'code:RP color:blue',
                'code:HW color:green']
        x=random.choice(choices)
        motor.referee_action('display', 'state', x)
        #################################### referee
        motor.see_code()


    def START_(b_context='status:planning_unit_start',
                 b_unit_task='unit_task:START state:running',
                 b_method='state:finished',
                 b_visual='code:?code color:?color'):
        b_context.modify(status='occupied')
        b_unit_task.set('unit_task:?code state:start type:ordered position:start')
        print ("Starting " + color + " planning unit with " + code + " unit task")

# Planning unit set up has been removed

########## unit task management productions ###########

    def request_second_unit_task(b_unit_task='unit_task:?unit_task state:finished type:ordered position:start',
                                 b_visual='second:?second'):
      b_unit_task.set('unit_task:?second state:start type:ordered position:second')
      print ('fast - start second unit task ' + second)

    def request_third_unit_task(b_unit_task='unit_task:?unit_task state:finished type:ordered position:second',
                                 b_visual='third:?third'):
      b_unit_task.set('unit_task:?third state:start type:ordered position:third')
      print ('fast - start third unit task ' + third)

    def request_fourth_unit_task(b_unit_task='unit_task:?unit_task state:finished type:ordered position:third',
                                 b_visual='fourth:?fourth'):
      b_unit_task.set('unit_task:?fourth state:start type:ordered')
      print ('fast - start fourth unit task ' + fourth)

##  manage the sequence if it is an ordered planning unit stored in DM
##            not used in this model (removed for simplicity)


## these manage the sequence if it is an ordered planning unit stored in buffer


## these manage planning units that are finished ###################
#TODO: Look part of PU first condition - use as before. Check for color at ut change

    def last_unit_task_ordered_plan(b_unit_task='unit_task:finished state:start type:ordered',
                                    b_visual='color:?color'):

        print ('finished planning unit =');
        print (color)

        b_unit_task.set('unit_task:START state:running')
        b_context.modify(status='planning_unit_start')
        print ('Look at code to determin new planning unit and unit task')
        ####################################
        # Planning unit start choices contain a color cue, represents prosesed visual info
        choices = ['code:AK color:purple',
                'code:RP color:blue',
                'code:HW color:green']
        x=random.choice(choices)
        motor.referee_action('display', 'state', x)
        #################################### referee
        b_visual.clear() # Done here, simultating what visual buffer would do before seeing code
        motor.see_code()


#################
##### AK UT #####
#################

# AK unit task AK-WM-SU-ZB-FJ

## add condition to fire this production

    def AK_ordered(b_unit_task='unit_task:AK state:start type:ordered'):
        b_unit_task.modify(state='begin')
        print ('start unit task AK')

    def AK_start(b_unit_task='unit_task:AK state:begin position:?position'):
        b_unit_task.set('unit_task:AK state:running position:?position')
        focus.set('AK')
        target='responce'
        content='AK-AK-1234'
        motor.enter_response(target, content)

    def AK_WM(b_unit_task='unit_task:AK state:running',
              vision_finst='state:finished',
              focus='AK'):
        focus.set('WM')
        target='responce'
        content='AK-WM-1432'
        motor.enter_response(target, content)

    def AK_SU(b_unit_task='unit_task:AK state:running',
              vision_finst='state:finished',
              focus='WM'):
        focus.set('SU')
        target='responce'
        content='AK-SU-4123'
        motor.enter_response(target, content)

    def AK_ZB(b_unit_task='unit_task:AK state:running',
              vision_finst='state:finished',
              focus='SU'):
        focus.set('ZB')
        target='responce'
        content='AK-ZB-2143'
        motor.enter_response(target, content)

    def AK_FJ(b_unit_task='unit_task:AK state:running',
              vision_finst='state:finished',
              focus='ZB'):
        focus.set('done')
        target='responce'
        content='AK-FJ-3214'
        motor.enter_response(target, content)

    def AK_finished_ordered(b_unit_task='unit_task:AK state:running position:?position',
                            vision_finst='state:finished',
                            focus='done'):
        print ('finished unit task AK(ordered)')
        b_unit_task.set('unit_task:AK state:finished type:ordered position:?position')



########################
##### RP Unit Task #####
########################

#                    YP-FJ
# RP unit task RP-SU<
#                    ZB-WM

    def RP_ordered(b_unit_task='unit_task:RP state:start type:ordered'):
        b_unit_task.modify(state='begin')
        print ('start unit task RP')

    def RP_start(b_unit_task='unit_task:RP state:begin position:?position'):
        b_unit_task.set('unit_task:RP state:running position:?position')
        focus.set('RP')
        target='responce'
        content='RP-RP-4321'
        motor.enter_response(target, content)

    def RP_SU(b_unit_task='unit_task:RP state:running',
              vision_finst='state:finished',
              focus='RP'):
        focus.set('SU')
        target='responce'
        content='RP-SU-4123'
        motor.enter_response(target, content)

    ### Unkown code

    def RP_identify2(b_unit_task='unit_task:RP state:running',
                     vision_finst='state:finished',
                     focus='SU',
                     b_visual='color:?color'):
        ############################### referee
        choices = ['code:YP','code:ZB']
        x=random.choice(choices)
        motor.referee_action('display', 'state', x+' color:'+color)
        ############################### referee
        motor.see_code()
        focus.set('code_seen')
        print ('waiting to see if YP or ZB')

    def RP_YP(b_unit_task='unit_task:RP state:running',
              vision_finst='state:finished',
              focus='code_seen',
              b_visual='code:YP'):
        focus.set('YP')
        target='responce'
        content='RP-YP-3412'
        motor.enter_response(target, content)

    def RP_FJ(b_unit_task='unit_task:RP state:running',
              vision_finst='state:finished',
              focus='YP'):
        focus.set('done')
        target='responce'
        content='RP-FJ-3214'
        motor.enter_response(target, content)

    def RP_ZB(b_unit_task='unit_task:RP state:running',
              vision_finst='state:finished',
              focus='code_seen',
              b_visual='code:ZB'):
        focus.set('ZB')
        target='responce'
        content='RP-ZB-2143'
        motor.enter_response(target, content)

    def RP_WM(b_unit_task='unit_task:RP state:running',
              vision_finst='state:finished',
              focus='ZB'):
        focus.set('done')
        target='responce'
        content='RP-WM-1432'
        motor.enter_response(target, content)

    def RP_finished_ordered(b_unit_task='unit_task:RP state:running position:?position',
                            vision_finst='state:finished',
                            focus='done'):
        print ('finished unit task RP(ordered)')
        b_unit_task.set('unit_task:RP state:finished type:ordered position:?position')

########################
##### HW Unit Task #####
########################

#                     / FJ
# HW unit task HW-YP--- ZB
#                     \ SU

    def HW_ordered(b_unit_task='unit_task:HW state:start type:ordered'):
        b_unit_task.modify(state='begin')
        print ('start unit task HW')

    ## the first production in the unit task must begin this way
    def HW_start(b_unit_task='unit_task:HW state:begin position:?position'):
        b_unit_task.set('unit_task:HW state:running position:?position')
        focus.set('HW')
        target='responce'
        content='HW-HW-2341'
        motor.enter_response(target, content)

    def HW_YP(b_unit_task='unit_task:HW state:running',
              vision_finst='state:finished',
              focus='HW'):
        focus.set('YP')
        target='responce'
        content='HW-YP-3412'
        motor.enter_response(target, content)

    ### Unkown code

    def HW_identify3(b_unit_task='unit_task:HW state:running',
                     vision_finst='state:finished',
                     focus='YP',
                     b_visual='color:?color'):
        ############################### referee
        choices = ['code:FJ','code:SU','code:ZB']
        x=random.choice(choices)
        motor.referee_action('display', 'state', x+' color:'+color)
        ############################### referee
        motor.see_code()
        focus.set('code_seen')
        print ('waiting to see if FJ, SU, or ZB')


    #### FJ or SU or ZB then end

    def HW_FJ(b_unit_task='unit_task:HW state:running',
              vision_finst='state:finished',
              focus='code_seen',
              b_visual='code:FJ'):
        focus.set('done')
        target='responce'
        content='HW-FJ-3214'
        motor.enter_response(target, content)


    def HW_SU(b_unit_task='unit_task:HW state:running',
              vision_finst='state:finished',
              focus='code_seen',
              b_visual='code:SU'):
        focus.set('done')
        target='responce'
        content='HW-SU-4123'
        motor.enter_response(target, content)


    def HW_ZB(b_unit_task='unit_task:HW state:running',
              vision_finst='state:finished',
              focus='code_seen',
              b_visual='code:ZB'):
        focus.set('done')
        target='responce'
        content='HW-ZB-2143'
        motor.enter_response(target, content)

    def HW_finished_ordered(b_unit_task='unit_task:HW state:running position:?position',
                            vision_finst='state:finished',
                            focus='done'):
        print ('finished unit task HW(ordered)')
        b_unit_task.set('unit_task:HW state:finished type:ordered position:?position')
