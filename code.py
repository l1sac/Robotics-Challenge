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
        reflection = color_sensor.reflection(port.B)

        if reflection < 45:
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)
        elif 45 < reflection < 60:
            score += 1
            light_matrix.write(str(score))
        else:
            
            await motor_pair.move_for_degrees(motor_pair.PAIR_1, 60, -90, velocity=100 )

            if color_sensor.reflection(port.B) < 45:
                continue

            await motor_pair.move_for_degrees(motor_pair.PAIR_1, -180, -90, velocity=100 )
            
            if color_sensor.reflection(port.B) < 45:
                continue
        await runloop.sleep_ms(5)

runloop.run(main())
