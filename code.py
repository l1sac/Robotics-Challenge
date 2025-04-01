from hub import light_matrix, port
from motor import velocity
import runloop
import motor_pair
import color_sensor
import time

motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
color_sensor_port = port.B  # Ensure this is the correct port

BLACK_THRESHOLD = 45  # Adjust this value
BASE_SPEED = 280
PROPORTIONAL_CONSTANT = 1.0  # Adjust this value

async def main():
    while True:
        reflection = color_sensor.reflection(color_sensor_port)

        error = reflection - BLACK_THRESHOLD
        steering_adjustment = int(error * PROPORTIONAL_CONSTANT)

        motor_pair.move(motor_pair.PAIR_1, 0, velocity=BASE_SPEED, steering=steering_adjustment)

        await runloop.sleep_ms(5)

runloop.run(main())
