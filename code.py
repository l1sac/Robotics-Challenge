from hub import light_matrix
from motor import velocity
import runloop
import motor_pair
from hub import port
import color_sensor
import distance_sensor
import color
import motor
import asyncio
import time
from hub import sound
score = 0
motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
detection_count = 0
detection_threshold = 5
async def main():
    global score, detection_count
    
    while True:
        if distance_sensor.distance(port.A) < 800 : 
            detection_count += 1
            if detection_count > detection_threshold: # beep after the 5 detected cans
                sound.beep(200, 500, 25)
                detection_count = 0

        if color_sensor.color(port.B) == color.BLACK: # if black it will turn in one direction
            await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 100, 100, 100)

        elif color_sensor.color(port.B) == color.WHITE: # if white it will turn in the other direction
            await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -100, 100, 100)

        elif color_sensor.color(port.B) == color.GREEN: # score counter
            score += 1
            light_matrix.write(str(score))
            motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -50, 100, 100)
            # await asyncio.sleep(1)
            continue

        elif color_sensor.color(port.B) == color.RED: # if detect anything else other than white, black and green (red) it will stop and beep
            motor_pair.stop(motor_pair.PAIR_1)
            await sound.beep(440, 500, 100)
            await sound.beep(500, 500, 100)
            await sound.beep(440, 500, 100)
            await sound.beep(500, 500, 100)
            await sound.beep(440, 500, 100)
            await runloop.sleep_ms(10000)
runloop.run(main())
