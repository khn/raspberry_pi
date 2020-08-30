import maestro

# These are the motor controller limits, measured in Maestro units.
# These default values typically work fine and align with maestro's default limits.
# Vaules should be adjusted so that center stops the motors and the min/max values
# limit speed range you want for your robot.
MIN_L = 4000
MIN_R = 4000
MIN_C = 4000
CENTER_L = 6000
CENTER_R = 6000
CENTER_C = 6000
MAX_L = 8000
MAX_R = 8000
MAX_C = 8000
# Sets what pins each motor is connected to on the Maestro board
CH_L = 0
CH_R = 1
CH_C = 2


class Head:

    def __init__(self):
        self.head = maestro.Controller()
        # Init motor accel/speed params
        # Left side (when looking face on)
        self.head.setAccel(CH_L, 0)
        self.head.setSpeed(CH_L, 60)
        # Right side (when looking face on)
        self.head.setAccel(CH_R, 0)
        self.head.setSpeed(CH_R, 60)
        # Center or head rotation motor
        self.head.setAccel(CH_C, 0)
        self.head.setSpeed(CH_C, 60)
        # Motor min/center/max values
        self.minL = MIN_L
        self.minR = MIN_R
        self.centerL = CENTER_L
        self.centerR = CENTER_R
        self.maxL = MAX_L
        self.maxR = MAX_R

    def _move_head(self, where, speed):
        if where == "right":
            self.head.runScriptSub(1)
        elif where == "left":
            self.head.setAccel(0, 4)  # set servo 0 acceleration to 4
            self.head.setTarget(0, 6000)  # set servo to move to center position
            self.head.setSpeed(1, 10)  # set speed of servo 1
            x = self.head.getPosition(1)  # get the current position of servo 1
            self.head.close()
        pass

    def move(self, look, speed):
        if look == "right":
            self._move_head("right_side", speed)

        pass




