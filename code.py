
python
Copy
from spike import PrimeHub, Motor, ColorSensor
import time

# Initialize the Hub, Motors, and Color Sensor
hub = PrimeHub()
left_motor = Motor('A')  # Left motor connected to port A
right_motor = Motor('B')  # Right motor connected to port B
color_sensor = ColorSensor('D')  # Color sensor connected to port D

# Thresholds for the line detection
WHITE = 100  # Color sensor detects white surface as high intensity
BLACK = 10   # Color sensor detects black line as low intensity

# Speed settings
base_speed = 30
turn_speed = 20

# Function to follow the line
def follow_line():
    while True:
        color_value = color_sensor.get_reflected_light()

        if color_value < BLACK:  # Detects the line (black)
            # Turn slightly to the left to follow the line
            left_motor.run_for_degrees(base_speed, -90)
            right_motor.run_for_degrees(base_speed, 90)
        elif color_value > WHITE:  # Detects the white surface
            # Turn slightly to the right to keep the line
            left_motor.run_for_degrees(base_speed, 90)
            right_motor.run_for_degrees(base_speed, -90)
        else:
            # Move forward when the robot is centered on the line
            left_motor.run_for_degrees(base_speed, 0)
            right_motor.run_for_degrees(base_speed, 0)

        time.sleep(0.05)  # Small delay to prevent overloading the processor

# Start following the line
follow_line()
