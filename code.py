
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
black = color_sensor.color(port.B) == color.BLACK
not_black = color_sensor.color(port.B) != color.BLACK
motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

def follow_line():
    while True:
        if color_sensor.color(port.B) == color.BLACK:
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)
        else:
            time.sleep_ms(15)
            motor_pair.move_for_degrees(motor_pair.PAIR_1, -90, -90, velocity=280)
            time.sleep_ms(20)

        global score
        if color_sensor.color(port.B) == color.GREEN:
            score += 1
            light_matrix.write(str(score))

# time.sleep(0.05) can put it to ensure accuracy

#def square_counter():
    
async def main():
    while True:
        follow_line()
        #square_counter()
        #await runloop.sleep_ms(50)

runloop.run(main())
