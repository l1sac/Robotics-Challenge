from hub import light_matrix
from motor import velocity
import runloop
import motor_pair
from hub import port
import color_sensor
import color
import motor

score = 0
black = color_sensor.color(port.B) == color.BLACK
not_black = color_sensor.color(port.B) != color.BLACK
motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
async def main():
    def follow_line():
        if black == True:
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)
        if not_black == True:
            motor_pair.move(motor_pair.PAIR_1, 90, velocity=280)

# time.sleep(0.05) can put it to ensure accuracy

    def square_counter():
        if color_sensor.color(port.B) == color.GREEN:
            light_matrix.write("!")
            light_matrix.write(f'{score} + 1')

runloop.run(main())
