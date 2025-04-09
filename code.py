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
from hub import sound

# variables
score = 0
motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
detection_threshold = 5
detection_count = 0
was_on_green = False

# main loop
async def main():
    global score, detection_count, was_on_green
    while True:
        motor.run_for_time(port.E, 10000, 500)
        if distance_sensor.distance(port.A) < 150: # detect when the distance is less than 15 cm
            detection_count += 1
            if detection_count > 5: # only beeps (substitute for quack sound) when the detection_count is above 5
                await sound.beep(200, 500, 25)
                detection_count = 0 # resets the detection_count

        if color_sensor.color(port.B) == color.BLACK: # if it senses black it will turn right
            motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 40, 160, 120)

        elif color_sensor.color(port.B) == color.WHITE: # if it senses white it will turn left
            motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 40, 120, 160)

        if color_sensor.color(port.B) == color.GREEN: # score counter
            if not was_on_green:
                score += 1
                light_matrix.write(str(score))
                #keeps moving after it senses green
                motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 0, 80, 80)
                was_on_green = True
                #stops after sensing a certain amount of green squares
                if score == 10:
                    light_matrix.clear()
        else:
            was_on_green = False

        if color_sensor.color(port.B) == color.RED : # if the colour sensed is red it will stop and play a success tune
            motor_pair.stop(motor_pair.PAIR_1)
            await sound.beep(440, 500, 100)
            await sound.beep(500, 500, 100)
            await sound.beep(440, 500, 100)
            await sound.beep(500, 500, 100)
            await sound.beep(440, 500, 100)
            await runloop.sleep_ms(10000)
runloop.run(main())
