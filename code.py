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

async def main():
    global score
    while True:
        reflection = color_sensor.reflection(port.B)
        if distance_sensor.distance(port.A) < 800: # beep when the distance is less than 8 cm
            sound.beep(100, 500, 25)

        if reflection < 25: # if black it will turn in one direction
            motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 50, 100, 50)

        elif 70 < reflection < 100: # if white it will turn in the other direction
            motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 50, 50, 100)

        elif 30 < reflection < 60: # score counter
            score += 1
            light_matrix.write(str(score))
            await runloop.sleep_ms(5000)

        else: # if detect anything else other than white, black and red (green) it will stop and beep
            motor_pair.stop(motor_pair.PAIR_1)
            await sound.beep(440, 500, 100)
            await sound.beep(500, 500, 100)
            await sound.beep(440, 500, 100)
            await runloop.sleep_ms(10000)
runloop.run(main())
