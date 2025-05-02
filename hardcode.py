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
import asyncio

motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

async def main():
    global score
    await motor_pair.move_for_time(motor_pair.PAIR_1, 4845, 0, velocity=360) # up to first gs
    motor.run_for_time(port.E, 4845, velocity=360)
    await light_matrix.write('1')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1418, 0, velocity=360) # up to middle of first circle
    motor.run_for_time(port.E, 1418, velocity=360)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 90, velocity = 200) # turn 90 degrees
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1384, 0, velocity=360) # to second gs
    await light_matrix.write('2')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 5536, 0, velocity=360) # to third gs
    await light_matrix.write('3')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2560, 0, velocity=360) # to fourth gs
    motor.run_for_time(port.E, 2560, velocity=360)
    await light_matrix.write('4')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 6643, 0, velocity=360) # to corner
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 90, velocity = 200) # turn
    await motor_pair.move_for_time(motor_pair.PAIR_1, 4152, 0, velocity=360)
    motor.run_for_time(port.E, 4152, velocity=360)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 90, velocity = 200) # turn
    await motor_pair.move_for_time(motor_pair.PAIR_1, 11487, 0, velocity=360) # to fifth gs
    motor.run_for_time(port.E, 6000, velocity=360)
    await light_matrix.write('5')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1418, 0, velocity=360), # up to middle of second circle
    motor.run_for_time(port.E, 1418, velocity=360)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 90, velocity = 200) # turn 90 degrees
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1384, 0, velocity=360) # to sixth gs
    await light_matrix.write('6')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2837, 0, velocity=360)
    motor.run_for_time(port.E, 2837, velocity=360)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 200, 90, velocity = 200) # turn 90 degrees
    await motor_pair.move_for_time(motor_pair.PAIR_1, 6712, 0, velocity=360) # up to 7th gs
    await light_matrix.write('7')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 3218, 0, velocity=360) # up to 8th gs
    motor.run_for_time(port.E, 3218, velocity=360)
    await light_matrix.write('8')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 4186, 0, velocity=360) # up to red end
    await sound.play('Emotional Piano')
runloop.run(main())
