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
score = 0
motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
detection_threshold = 5
detection_count = 0
was_on_green = False
async def main():
    global score, detection_count, was_on_green
    while True:
        if distance_sensor.distance(port.A) < 800: # beep when the distance is less than 8 cm
            detection_count += 1
            if detection_count > 5:
                await sound.beep(200, 500, 25)
                detection_count = 0

        if color_sensor.color(port.B) == color.BLACK: # if black it will turn in one direction
             motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 40, 100, 60)

        elif color_sensor.color(port.B) == color.WHITE: # if white it will turn in the other direction
            motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 40, 60, 100)

        if color_sensor.color(port.B) == color.GREEN:
            if not was_on_green:
                score += 1
                light_matrix.write(str(score))
                was_on_green = True
        else:
            was_on_green = False

        if color_sensor.color(port.B) == color.RED : # if detect anything else other than white, black and red (green) it will stop and beep
            motor_pair.stop(motor_pair.PAIR_1)
            await sound.beep(440, 500, 100)
            await sound.beep(500, 500, 100)
            await sound.beep(440, 500, 100)
            await sound.beep(500, 500, 100)
            await sound.beep(440, 500, 100)
            await runloop.sleep_ms(10000)
runloop.run(main())
