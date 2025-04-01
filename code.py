from hub import light_matrix, port
from motor import velocity
import runloop
import motor_pair
import color_sensor
import time

# Initialization
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
color_sensor_port = port.C

# Calibration (Adjust these values)
BLACK_THRESHOLD = 45
BASE_SPEED = 280
PROPORTIONAL_CONSTANT = 1.0
GREEN_THRESHOLD = 70  # Adjust this based on your sensor readings for green

async def main():
    while True:
        reflection = color_sensor.reflection(color_sensor_port)

        if reflection > GREEN_THRESHOLD:
            # Green marker detected
            motor_pair.stop(motor_pair.PAIR_1)
            light_matrix.write("Green!")
            await runloop.sleep_ms(2000)  # Stop for 2 seconds
            light_matrix.clear()
        else:
            # Line following logic
            error = reflection - BLACK_THRESHOLD
            turn_adjustment = error * PROPORTIONAL_CONSTANT

            left_speed = BASE_SPEED - turn_adjustment
            right_speed = BASE_SPEED + turn_adjustment

            motor_pair.move(motor_pair.PAIR_1, 0, velocity=int(max(min(left_speed, 1000), -1000)), steering=int(turn_adjustment*2))

        await runloop.sleep_ms(5)

runloop.run(main())
