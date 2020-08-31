import maestro
import time

# These are the motor controller limits, measured in Maestro units.
# These default values typically work fine and align with maestro's default limits.
# Vaules should be adjusted so that center stops the motors and the min/max values
# limit speed range you want for your robot.
MIN_L = 992
MIN_R = 992
MIN_C = 992
CENTER_L = 1500
CENTER_R = 1500
CENTER_C = 1500
MAX_L = 1900
MAX_R = 1900
MAX_C = 1900
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
        self.head.setSpeed(CH_L, 0)
        # Right side (when looking face on)
        self.head.setAccel(CH_R, 0)
        self.head.setSpeed(CH_R, 0)
        # Center or head rotation motor
        self.head.setAccel(CH_C, 0)
        self.head.setSpeed(CH_C, 0)
        # Motor min/center/max values
        self.minL = MIN_L
        self.minR = MIN_R
        self.centerL = CENTER_L
        self.centerR = CENTER_R
        self.maxL = MAX_L
        self.maxR = MAX_R

    def _move_head(self, where, speed):
        print("Well, here we are")
        if where == "right":
            self.head.setSpeed(0, 60)  # set speed of servo 1
            self.head.setSpeed(1, 60)
            self.head.setSpeed(2, 30)
            # self.head.runScriptSub(0)
            self.head.setTarget(0, 5488 )  # set servo to move to center position
            self.head.setTarget(1, 5934 )  # set servo to move to center position
            self.head.setTarget(2, 5856 )  # set servo to move to center position
            time.sleep(.3)
        elif where == "left":
            self.head.setAccel(0, 200)  # set servo 0 acceleration to 4
            self.head.setAccel(1, 200)  # set servo 0 acceleration to 4
            self.head.setAccel(2, 180)  # set servo 0 acceleration to 4
            self.head.setSpeed(0, 0)  # set speed of servo 1
            self.head.setSpeed(1, 0)
            self.head.setSpeed(2, 0)
            self.head.setTarget(0, 5190 )  # set servo to move to center position
            self.head.setTarget(1, 6843 )  # set servo to move to center position
            self.head.setTarget(2, 7697 )  # set servo to move to center position
            time.sleep(.3)
            self.head.setTarget(0, 7553 )  # set servo to move to center position
            self.head.setTarget(1, 5868 )  # set servo to move to center position
            # self.head.setTarget(2, 7697 )  # set servo to move to center position
            # self.head.setSpeed(1, 10)  # set speed of servo 1
            time.sleep(.7)
            self.head.setTarget(0, 5190 )  # set servo to move to center position
            self.head.setTarget(1, 6843 )  # set servo to move to center position
            # self.head.setTarget(2, 7697 )  # set servo to move to center position
            time.sleep(.3)
            self.head.setSpeed(0, 170)  # set speed of servo 1
            self.head.setSpeed(1, 170)
            self.head.setTarget(0, 5488 )  # set servo to move to center position
            self.head.setTarget(1, 5934 )  # set servo to move to center position
            # self.head.setTarget(2, 7697 )  # set servo to move to center position
            time.sleep(.3)

    def move(self, look, speed):
        if look == "right":
            self._move_head("right", speed)
        elif look == "left":
            self._move_head("left", speed)

    def close(self):
        self.head.close()



