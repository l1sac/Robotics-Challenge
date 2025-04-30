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
colour = color_sensor.color(port.B)

async def main():
    global detection_count, was_on_green, score
    while colour != color.RED:
        motor.run_for_time(port.E, 10000, 500) # can knocker
        if colour == color.BLACK:
            motor_pair.move(motor_pair.PAIR_1, 75)
        elif colour == color.GREEN: #needs adjustment, this is for green square counter
            if not was_on_green:
                score += 1
                light_matrix.write(str(score))
                was_on_green = True
                #keeps moving after it senses green
                motor_pair.move(motor_pair.PAIR_1, -75)
                #stops after sensing a certain amount of green squares
                if score == 11:
                    light_matrix.clear()
                    motor_pair.move(motor_pair.PAIR_1, 0)        
        else:
            motor_pair.move(motor_pair.PAIR_1, -75)

        if distance_sensor.distance(port.A) < 150: # detect when the distance is less than 15 cm
            detection_count += 1
            if detection_count > 5:
                sound.play('Squeaky Toy', 80, 50)
                detection_count = 0 # resets the detection_count

    while colour == color.RED:
        motor_pair.stop(motor_pair.PAIR_1)
        sound.play('Emotional Piano', 80, 50)

runloop.run(main())
