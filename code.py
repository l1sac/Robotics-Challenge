from hub import light_matrix
from motor import velocity
import runloop
import motor_pair
from hub import port
import color_sensor
import distance_sensor
import color
import motor
import time
from app import sound

global score, detection_count, was_on_green
# variables
score = 0
detection_threshold = 5
detection_count = 0
was_on_green = False
movement_motors = motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
target_reflection = 50 # adjust needs to be the average between white n black
KP = 1.0
base_speed = 40
reflection = color_sensor.reflection(port.B)

while True: 
    motor.run_for_time(port.E, 10000, 500) # can knocker
    error = reflection - target_reflection
    turn_rate = int(KP * error)
    if distance_sensor.distance(port.A) < 150: # detect when the distance is less than 15 cm
            detection_count += 1
            if detection_count > 5: # only beeps (substitute for quack sound) when the detection_count is above 5
                sound.play('Squeaky Toy', 80, 50)
                detection_count = 0 # resets the detection_count

    
    if 30 < reflection < 60: #needs adjustment, this is for green square counter 
        if not was_on_green:
                score += 1
                light_matrix.write(str(score))
                #keeps moving after it senses green
                motor_pair.move(motor_pair.PAIR_1, turn_rate, velocity=base_speed)
                was_on_green = True
                #stops after sensing a certain amount of green squares
                if score == 11:
                    light_matrix.clear()
    
    if < reflection < : # if the colour sensed is red it will stop and play a success tune
        motor_pair.stop(motor_pair.PAIR_1)
        sound.play('Emotional Piano')
    else:
        motor_pair.move(motor_pair.PAIR_1, turn_rate, velocity=base_speed)
    
