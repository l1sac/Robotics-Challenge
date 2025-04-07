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

# --- Configuration ---
LINE_THRESHOLD = 35  # Adjust this value based on your sensor readings for the line
KP = 1.0             # Proportionality constant - tune this value
BASE_SPEED = 50      # Base speed for the motors

async def main():
    global score
    while True:
        reflection = color_sensor.reflection(port.B)
        distance = distance_sensor.distance(port.A)

        if distance < 800:
            sound.beep(100, 500, 25)

        error = reflection - LINE_THRESHOLD  # Calculate the error (how far from the line)

        # Calculate motor adjustments based on the error
        turn_adjustment = KP * error

        left_speed = BASE_SPEED - turn_adjustment
        right_speed = BASE_SPEED + turn_adjustment

        # Limit speeds to a reasonable range (optional)
        max_speed = 100
        min_speed = 10
        left_speed = max(min(left_speed, max_speed), -max_speed)
        right_speed = max(min(right_speed, max_speed), -max_speed)

        motor_pair.start(motor_pair.PAIR_1, left_speed, right_speed)

        if 30 < reflection < 60: # score counter (keep this logic)
            score += 1
            light_matrix.write(str(score))
            await runloop.sleep_ms(5000)
        elif not (20 < reflection < 80): # If significantly off the line, stop and indicate (adjust range as needed)
            motor_pair.stop(motor_pair.PAIR_1)
            await sound.beep(880, 500, 100) # Higher frequency indicates lost line
            await runloop.sleep_ms(2000)

        await runloop.sleep_ms(10) # Small delay for the loop

runloop.run(main())
