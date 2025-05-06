from hub import light_matrix
from motor import velocity
import runloop
import motor_pair
from hub import port
import motor

from hub import sound

motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
async def main():
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2076, 0, velocity=360) # up to first can works !
    #await motor.run_for_time(port.E, 2000, velocity=360) # knock over can
    #await runloop.sleep_ms(1200) # remove can
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2500, 0, velocity=360) # up to first gs works
    await light_matrix.write('1')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1350, 0, velocity=360) # up to middle of first circle works
    #await motor.run_for_time(port.E, 2000, velocity=360) # knock over can
    #await runloop.sleep_ms(1200) # remove can
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 195, -90, velocity = 200) # turn 90 degrees
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1300, 0, velocity=360) # to second gs
    await light_matrix.write('2')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 4800, 0, velocity=360) # to third gs
    await light_matrix.write('3')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1029, 0, velocity=360) # to third can
    #await motor.run_for_time(port.E, 2000, velocity=360) # knock over can
    #await runloop.sleep_ms(1200) # remove can
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1100, 0, velocity=360) # to fourth gs
    await light_matrix.write('4')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 6000, 0, velocity=360) # to corner
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 195, -90, velocity = 200) # turn
    await motor_pair.move_for_time(motor_pair.PAIR_1, 3200, 0, velocity=360) # to corner
    #await motor.run_for_time(port.E, 2000, velocity=360) # knock over can
    #await runloop.sleep_ms(1200)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 195, -90, velocity = 200) # turn
    await motor_pair.move_for_time(motor_pair.PAIR_1, 4000, 0, velocity=360) # to can
    #await motor.run_for_time(port.E, 2000, velocity=360) # knock over can
    #await runloop.sleep_ms(1200) # remove can
    await motor_pair.move_for_time(motor_pair.PAIR_1, 3228, 0, velocity=360) # to duck
    await sound.beep(440, 500, 100)
    await sound.beep(440, 500, 100)
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2829, 0, velocity=360) # to 5th gs
    await light_matrix.write('5')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1490, 0, velocity=360) # to middle of second circle
    #await motor.run_for_time(port.E, 2000, velocity=360) # knock over can
    #await runloop.sleep_ms(1200) # remove can
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 195, 90, velocity = 200) # turn 90 degrees
    await motor_pair.move_for_time(motor_pair.PAIR_1, 475, 0, velocity=360) # to sixth gs
    await light_matrix.write('6')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2627, 0, velocity=360) # to corner
    #await motor.run_for_time(port.E, 2000, velocity=360) # knock over can
    #await runloop.sleep_ms(1200) # remove can
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 195, 90, velocity = 200) # turn 90 degrees
    await motor_pair.move_for_time(motor_pair.PAIR_1, 6000, 0, velocity=360) # up to 7th gs
    await light_matrix.write('7')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1298, 0, velocity=360) # up to 8th can
    ##await motor.run_for_time(port.E, 2000, velocity=360) # knock over can
    await runloop.sleep_ms(1200) # remove can
    await motor_pair.move_for_time(motor_pair.PAIR_1, 2500, 0, velocity=360) # up to 8th gs
    await light_matrix.write('8')
    await motor_pair.move_for_time(motor_pair.PAIR_1, 3500, 0, velocity=360) # up to red end
    await sound.beep(440, 500, 100)
    await sound.beep(500, 500, 100)
    await sound.beep(440, 500, 100)
    await sound.beep(500, 500, 100)
    await sound.beep(440, 500, 100)
runloop.run(main())
