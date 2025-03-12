from hub import light_matrix
from motor import velocity
import runloop
import motor_pair
from hub import port
import color_sensor
import color
import motor

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    if color_sensor.color(port.B) == color.BLACK:
        light_matrix.write("!")
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=280)
    if color_sensor.color(port.B) != color.BLACK:
        motor_pair.move(motor_pair.PAIR_1, 360, velocity=280)
    
runloop.run(main())
