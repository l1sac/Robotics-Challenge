from hub import light_matrix
from motor import velocity
import runloop
import motor_pair
from hub import port
import color_sensor
import color
import motor
import time

score = 0
motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

async def main():
    await motor_pair.move_for_time(motor_pair.PAIR_1, 5000,0 , velocity=280)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0, velocity=280)
    await motor_pair.move_for_time(motor_pair.PAIR_1, 15000, 0, velocity= 280)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0, velocity=280)
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2500,0 , velocity=280)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0, velocity=280)
    await motor_pair.move_for_time(motor_pair.PAIR_1, 12500, 0, velocity= 280)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0, velocity=280)
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2500,0 , velocity=280)
    while True:
        global score
        if color_sensor.color(port.B) == color.RED:
            motor_pair.stop(motor_pair.PAIR_1)
        elif color_sensor.color(port.B) == color.GREEN:
            score += 1
            light_matrix.write(str(score))
runloop.run(main())
