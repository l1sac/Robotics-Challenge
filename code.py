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
    global score
    while True:
        if color_sensor.reflection(port.B) < 15:
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)
        elif 20 < color_sensor.reflection(port.B) < 40:
            score += 1
            light_matrix.write(str(score))
        else:
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 120, -90, velocity=100, stop=motor.BRAKE)
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, -240, -90, velocity=100, stop=motor.BRAKE)
        await runloop.sleep_ms(5)
runloop.run(main())
