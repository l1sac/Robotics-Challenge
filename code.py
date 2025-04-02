from hub import light_matrix, port
from motor import velocity
import runloop
import motor_pair
import color_sensor
import time

# Initialization
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
light_matrix.write("!")
color_sensor_port = port.B
score = 0
color = 6
async def main():
    while True:
        global score
        global color
        if color_sensor.color(port.B) == color:
            motor_pair.stop(motor_pair.PAIR_1)
            score += 1
            light_matrix.write(str(score))
            await runloop.sleep_ms(2000)
        else:
            motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, 1000, 500)
        await runloop.sleep_ms(5)

runloop.run(main())
